import tkinter as tk
import json

#from refresh import *
from userInfo import *
from id import *

user1 = NewUser("John")
user2 = NewUser("Alex")
user3 = NewUser("Peter")
user4 = NewUser("Jose")
print(user4.getID())
print(user1.getID())

f = open('info.json')
File = json.load(f)
root = tk.Tk()
root.geometry("1920x1080")
root.configure(bg = "black")

root.title("Dashboard")

for i in range(len(File)):
    word = File[str(i)]["name"], ":",  File[str(i)]["id"]
    w = tk.Label(root, text=word, bg = "black", fg = "white")
    if((i % 2) > 0):
        w.grid(row=i, column = 0)
    else:
        w.grid(row=i+1, column = 4)
    


root.mainloop()
