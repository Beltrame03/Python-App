from tkinter import *
from userInfo import *
import tkinter as tk
import os
import socket
import time
import threading


class newWindow:
  
  def __init__(self, size):
    self.size = size

  def buildWindow(self):
    def newClass():
      acct = newAccount()
      acct.new()
    def adminLogin():
      admin = adminWindow()
      admin.adminLogin()

    def collect(*args):
      a=username.get()
      b=id.get()
      username.set("")
      id.set("")
      user = oldUser(a, b)

      if(user.checkInfo()):
        homepage()


      else:
        failure = tk.Tk()
        failure.title("Incorrect")
        tk.Label(failure, text="Username or ID are incorrect").pack()
        failure.mainloop()

    root = tk.Tk()
    root.geometry(self.size)
    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="ID").grid(row=1)


    username = tk.StringVar()
    id = tk.StringVar()

    e1 = tk.Entry(root, textvariable=username)
    e2 = tk.Entry(root, textvariable=id)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    b1 = tk.Button(root, text="Submit", command=collect)
    b1.grid(row=1, column=2)

    b2 = tk.Button(root, text="New Account", command=newClass)
    b2.grid(row=3, column=1)
    root.title("Login")

    b3 = tk.Button(root, text="Administrative Login", command=adminLogin)
    b3.grid(row=3, column=0)
    root.title("Login")
  
    root.mainloop()


class newAccount:
  
  def __init__(self):
    pass

  def new(self):

      def newAcctCollect(*args):
        a =name.get()
        user = NewUser(a)
        new.destroy()

      global new
      new = tk.Toplevel()
      new.title("Registration")
      new.geometry("400x100")
      tk.Label(new, text="Username").grid(row=0)

      name = StringVar()

      e1 = tk.Entry(new, textvariable=name)

      e1.grid(row=0, column=1)
      
      b1 = tk.Button(new, text="Submit", command=newAcctCollect)
      b1.grid(row=0, column=2)



def homepage():


  def send(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (socket.gethostname(), 1234)
    s.connect(addr)
    msg = message
    s.send(str.encode(msg))

  def printdata():
    f = open('messages.json')
    messages = json.load(f)
    l = 0
    for i in messages:
      item = (messages[i]["message"])
      tk.Label(homepage, text=item).grid(row=l+1, column=0)
      l += 1

  def getMessage(*args):
    send(message.get())
    message.set("")
    time.sleep(0.1)
    printdata()

def main():
    
    tk.Label(homepage, text="Username").grid(row=0)

    message = StringVar()

    e1 = tk.Entry(homepage, textvariable=message)

    e1.grid(row=0, column=1)
    
    b1 = tk.Button(homepage, text="Submit", command=getMessage)
    b1.grid(row=0, column=2)


  global homepage
  homepage = tk.Toplevel()
  homepage.title("Homepage")
  homepage.geometry("1920x1080")

  t1 = threading.Thread(target = main)
  t2 = threading.Thread(target = printdata)

  t1.start()
  t2.start()

  t1.join()
  t2.join()

class adminWindow:
  def __init__ (self):
    pass
  
  def adminLogin(self):
    def adminLogin(*args):
      a=ADusername.get()
      b=ADid.get()
      ADusername.set("")
      ADid.set("")
      if(a == 'josh'):
        if(b == '0'):
          return True
      return False


    admin = tk.Toplevel()
    admin.geometry("400x200")
    tk.Label(admin, text="Username").grid(row=0)
    tk.Label(admin, text="ID").grid(row=1)


    ADusername = tk.StringVar()
    ADid = tk.StringVar()

    e1 = tk.Entry(admin, textvariable=ADusername)
    e2 = tk.Entry(admin, textvariable=ADid)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    b1 = tk.Button(admin, text="Submit", command=adminLogin)
    b1.grid(row=1, column=2)