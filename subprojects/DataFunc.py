#Modules and Offstes
import pymem
from pymem import Pymem
from win32api import GetSystemMetrics
from numpy import array,matmul
from struct import unpack as unpack_st
from collections import namedtuple
from pymem.exception import MemoryReadError
from recordclass import recordclass
import requests
from requests import packages, get
#-
LocalPlayerOffset = 0x30E11FC
ObjectPosition = 0x01DC
PosX = ObjectPosition
PosY = ObjectPosition + 0x8
PosZ = ObjectPosition + 0x4
oViewProjMatrices = 0x310E5F0
NameOfChampion = 0x2AC4
oObjectManager = 0x2491B40
oObjectMapRoot = 0x28
oObjectMapNodeNetId = 0x10
oObjectMapNodeObject = 0x14

requests.packages.urllib3.disable_warnings()

#Data and Functions
LOL = Pymem('League of Legends.exe')

print('Waiting for Global Names get...')

GAME_DATA_ENDPOINT = 'https://127.0.0.1:2999/liveclientdata/allgamedata'
CHAMPION_INFO_ENDPOINT = 'https://raw.communitydragon.org/latest/game/data/characters/{champion}/{champion}.bin.json'


def clean_champion_name(name):
    return name.split('game_character_displayname_')[1].lower()

class ChampionStats():
    def __init__(self):
        game_data = get(GAME_DATA_ENDPOINT, verify=False).json()
        champion_names = [clean_champion_name(player['rawChampionName']) for player in game_data['allPlayers']]
        self.champion_data = {}
        for champion in champion_names:
            champion_response = get(CHAMPION_INFO_ENDPOINT.format(champion=champion)).json()
            self.champion_data[champion] = {k.lower(): v for k, v in champion_response.items()}

    def names(self):
        return self.champion_data.keys()

Node = recordclass('Node', 'address, next')

def linked_insert(current_node, next_address):
    next_node = Node(next_address, current_node.next)
    current_node.next = next_node

def int_from_buffer(data, offset):
    return int.from_bytes(data[offset:offset + 4], 'little')

def float_from_buffer(data, offset):
    f, = unpack_st('f', data[offset:offset + 4])
    return f
Object = namedtuple('Object', 'name, x, y, z')

def read_object(LOL, address):
    data = LOL.read_bytes(address, 0x3400)
    params = {}
    params['name'] = LOL.read_string(int_from_buffer(data, NameOfChampion), 50)
    params['x'] = float_from_buffer(data, PosX)
    params['y'] = float_from_buffer(data, PosY)
    params['z'] = float_from_buffer(data, PosZ)

    return Object(**params)

def find_object_pointers(mem, max_count=800):
    object_pointers = mem.read_uint(mem.base_address + oObjectManager)
    root_node = Node(mem.read_uint(object_pointers + oObjectMapRoot), None)
    addresses_seen = set()
    current_node = root_node
    pointers = set()
    count = 0
    while current_node is not None and count < max_count:
        if current_node.address in addresses_seen:
            current_node = current_node.next
            continue
        addresses_seen.add(current_node.address)
        try:
            data = mem.read_bytes(current_node.address, 0x18)
            count += 1
        except MemoryReadError:
            pass
        else:
            for i in range(3):
                child_address = int_from_buffer(data, i * 4)
                if child_address in addresses_seen:
                    continue
                linked_insert(current_node, child_address)
            net_id = int_from_buffer(data, oObjectMapNodeNetId)
            if net_id - 0x40000000 <= 0x100000:
                pointers.add(int_from_buffer(data, oObjectMapNodeObject))
        current_node = current_node.next
    return pointers

def find_champion_pointers(mem, champion_names):
    pointers = find_object_pointers(mem)
    champion_pointers = set()
    for pointer in pointers:
        try:
            o = read_object(mem, pointer)
        except (MemoryReadError, UnicodeDecodeError):
            pass
        else:
            if o.name.lower() in champion_names:
                champion_pointers.add(pointer)
    return champion_pointers

def list_to_matrix(floats):
    m = array(floats)
    return m.reshape(4, 4)

def find_view_proj_matrix(mem):

    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    data = mem.read_bytes(mem.base_address + oViewProjMatrices, 128)
    view_matrix = list_to_matrix([float_from_buffer(data, i * 4) for i in range(16)])
    proj_matrix = list_to_matrix([float_from_buffer(data, 64 + (i * 4)) for i in range(16)])
    view_proj_matrix = matmul(view_matrix, proj_matrix)
    return view_proj_matrix.reshape(16), width, height

def world_to_screen(view_proj_matrix, width, height, x, y, z):
    
    clip_coords_x = x * view_proj_matrix[0] + y * view_proj_matrix[4] + z * view_proj_matrix[8] + view_proj_matrix[12]
    clip_coords_y = x * view_proj_matrix[1] + y * view_proj_matrix[5] + z * view_proj_matrix[9] + view_proj_matrix[13]
    clip_coords_w = x * view_proj_matrix[3] + y * view_proj_matrix[7] + z * view_proj_matrix[11] + view_proj_matrix[15]

    if clip_coords_w < 1.:
        clip_coords_w = 1.

    M_x = clip_coords_x / clip_coords_w
    M_y = clip_coords_y / clip_coords_w

    out_x = (width / 2. * M_x) + (M_x + width / 2.)
    out_y = -(height / 2. * M_y) + (M_y + height / 2.)

    if 0 <= out_x <= width and 0 <= out_y <= height:
        return out_x, out_y

    return None, None


champion_stats = ChampionStats()
champion_pointers = find_champion_pointers(LOL, champion_stats.names())

