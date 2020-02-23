from id import *
import csv

class NewUser:

    def __init__(self, name):
        Id1 = Id(name)
        self.name = name
        self.id = Id1
        #writeInfo(self.id, self.name)
    
    def getID(self):
      return self.id.getID()
    def getName(self):
        return self.name
