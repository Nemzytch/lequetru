from pyairtable import Table
import os
import time

API_KEY= "key181wgNDrYM2bms"
table = Table(API_KEY, 'appHnr7cu8j1HlMC2', 'YUUMI')


#open account.txt each line is a account split by ":"


with open('accounts.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        account = line.split(':')
        print(account)
        table.create({'Account': account[0], 'Password': account[1],'HWID':"None"})
        time.sleep(0.5)


