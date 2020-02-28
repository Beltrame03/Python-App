import json

class Id:
    def __init__(self, name):
      self.id = newId(name)

    def __repr__(self):
      return(self.id)
    
    def getID(self):
      return self.id
    


def newId(name):

  #Get number of items in JSON file and increment by 1 by default -> Index is +1 and then it works somehow idk ngl
    l = 0
    items = {}
    f = open('info.json')
    oldFile = json.load(f)
    x = 1
    while (x == 1):
      try:
        print(oldFile[str(l)])
        l += 1
      except:
        x = 0

    for i in range(l):
      items[str(i)] = oldFile[str(i)]
 
    newId = oldFile[str(l-1)]['id']
    id = int(newId) + 1
    items[str(l)] = {"name": name, "id": id}

   
    with open('info.json', 'w') as f:
        json.dump(items, f)
    return id