import tkinter as tk
#from refresh import *
from userInfo import *
from id import *

user1 = NewUser("John")
user2 = NewUser("Alex")
user3 = NewUser("Peter")
user4 = NewUser("Jose")
print(user4.getID())
print(user1.getID())

'''
print(user)'''


'''
root = tk.Tk()
root.geometry("500x500")
root.configure(bg = "black")

root.title("Dashboard")

text = ["hiu", "bye"]
for i in range(len(text)):
    w = tk.Label(root, text=text[i], bg = "black", fg = "white")
    w.pack()

root.mainloop()
'''