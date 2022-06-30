import clientConnect
from logger import logger
import tkinter


completeAccountList = []
with open("accountList.txt", "r") as f:
    accountList = f.readlines()
    print(accountList)
for accounts in accountList:
    AccountName, Username, Password = accounts.split(":")
    print(AccountName)
    completeAccountList.append((AccountName, Username, Password.strip()))
print(completeAccountList)


root = tkinter.Tk()
root.title("Account Logger")
root.geometry("300x300")
accountListBox = tkinter.Listbox(root)
for account in completeAccountList:
    accountListBox.insert(tkinter.END, account[0])
accountListBox.pack()
connectButton = tkinter.Button(root, text="Connect", command=lambda: clientConnect.stay_connected(completeAccountList[accountListBox.curselection()[0]][1], completeAccountList[accountListBox.curselection()[0]][2]))
connectButton.pack()
root.mainloop()
