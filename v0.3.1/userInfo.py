from id import *
import csv

class NewUser:

    def __init__(self, name):
        if (check1(name)):
          Id1 = Id(name)
          self.name = name
          self.id = Id1
          print("done")
    
    def getID(self):
      return self.id.getID()

    def getName(self):
        return self.name

class oldUser:

  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  def checkInfo(self):
    checker = check(self.name, int(self.id))
    if checker:
      print("user credentials have been accepted")
      return True
    else:
      print("user credentials incorrect")
      return False


def check1(name):
  f = open('info.json')
  File = json.load(f)
  for i in File:
    if (name == File[i]["name"]):
      print("a")
      return False
  print("b")
  return True
        
            


def check(name, id1):
  f = open('info.json')
  files = json.load(f)
  for i in files:
    if(name == files[i]["name"]):
      if(id1 == files[i]["id"]):
        return True
      else:
        pass
    else:
      pass
  return False