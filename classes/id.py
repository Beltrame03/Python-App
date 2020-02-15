import csv

class Id:


    def __init__(self):
        self.id = newId()

    def __repr__(self):
        return(self.id)

    def __add__(self, x):
        return str(int(self.id) + x)

def newId():
    return '00000000'
    with open('id.csv', mode='a+') as csv_file:
        getId()
    csv_file.close()

def getId():
    '''o = open('id.csv')
    csv_o = csv.reader(o)
    for row in csv_o:
        print(row['id'])'''
