import json
import json
l = 0

items = {}
f = open('mydata.json')
team = json.load(f)
x = 1
while (x == 1):
  try:
    print(team[str(l)])
    l += 1
  except:
    x = 0

for i in range(l):
  items[str(i)] = team[str(i)]
  print(items[str(i)])

print("")
print("")
print("")
print("")
print("")


items[str(l)] = {"health": 43, "level": 2}
print(len(items))

for m in range(len(items)):
  if(m > l):
    break
  else:
    print(items[str(m)])



with open('mydata.json', 'w') as f:
    json.dump(items, f)

f.close()
