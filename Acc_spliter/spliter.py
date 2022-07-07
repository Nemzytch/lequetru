from time import time
import tableActions

def spliter():
    with open("Account_to_split.txt", "r") as f:
        for lines in f:
            line = lines.strip().split(":")
            tableActions.add_account(line[0], line[1], line[2])
    
spliter()