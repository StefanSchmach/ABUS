import json
import pathlib as Path
import os

print("Hello")
a = 1
print(a)
b = 5 + a
print(b)

a = "A1"
if a in ["A1"]:
    print("hallo")
else:
    print("bye")


url = "abc#1234"
data = url.split("#")
print(data[0])
print(data[1])

with open("TestConfig.json" , "r") as config_file:
    data = json.load(config_file)

width = data['width']
height = data["height"]

ABC = width + height

print(width)
print(height)
print(ABC)

#os.mkdir("C:/Hello")

FilePath = "H:/Example.json"
if os.path.exists(FilePath):
    print("Datei existiert!")
else:
    json_obj = {}
    json_obj ['TestausPython'] = []
    json_obj ['TestausPython'].append({
            'name' : 'Stefan',
            'Alter': 1
        })
    with open('H:\Example.json', 'w') as jsonFile:
        json.dump(json_obj, jsonFile)