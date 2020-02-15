from id import *
import csv

class NewUser:

    def __init__(self, name, Id = Id()):
        self.name = name
        self.id = Id
        writeInfo(self.id, self.name)

    def getID(self):
        return self.id

    def getName(self):
        return self.name

def writeInfo(id, name):
    with open('user.csv', mode='a+') as csv_file:
        fieldnames = ['name', 'id']
        if(checkName(name)):
            print("1")
            if(checkId(id)):
                print('2')
                writer = csv.writer(csv_file, quoting = csv.QUOTE_ALL)
                writer.writerows([['name', name, 'id', (id + 1)]])
            else:
                print("3")
    csv_file.close()


def checkName(name):
 with open('user.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if(name in row):
             print("User already created")
             return False
 return True


def checkId(id):
    o = open('user.csv')
    csv_o = csv.reader(o)
    for row in csv_o:
        if(id in row):
            print("Id already in database. Making new ID")
            return False
    o.close()
    return True