from asyncore import write
from cgi import test
from email.message import Message
import imp
import json
import json
from lib2to3.pgen2.token import AWAIT
from re import A
from time import time
from unicodedata import name
from django.db import connection
from lcu_driver import Connector
from requests import request
import time

connector = Connector()

Summoner_id = "none"
text = "Hello summoner,\n\nWe hope you will have fun with your new account! Feel free to join our discord and leave a comment about your experience with NoxuSmurfs, a Prime capsule is rewarded for this!\n\nAny question or problem with one of our accounts? You can contact us on our discord server, a room is dedicated to this :)\n\nDiscord link : https://discord.gg/k7XcvqJ3Ra"

async def Message(connection):
    global Summoner_id
    
    Message = await connection.request("get", "/lol-chat/v1/friend-requests")
    Message_json = await Message.json()
    
    for friends in Message_json:
        Summoner_id = friends["id"]
        if Message.status != 200:
            pass
        else:
            await connection.request("post", "/lol-chat/v1/friend-requests", data = {"id": Summoner_id, "direction": "in"})
            time.sleep(1)
            await connection.request("post",f"/lol-chat/v1/conversations/{Summoner_id}/messages", data={"body": text})
            
        print("Message envoyé à " + Summoner_id)

#connection 
@connector.ready
async def connect(connection):
    await Message(connection)
    print("Connected")

@connector.close
async def disconnect(connection):
    print("Disconnected")

@connector.ws.register("/lol-chat/v1/friend-requests/")
async def update(connection, event):
    await Message(connection)

connector.start()