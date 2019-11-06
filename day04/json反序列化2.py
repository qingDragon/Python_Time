import json
f = open("test.txt","r")

data = json.loads(f.read())
print(data.get("name"))

f.close()