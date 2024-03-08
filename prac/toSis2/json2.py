import json

file = open("/Users/yerassyl/vscode/kbtu/pp2/labs/lab4/json/sample-data.json")

lst = []
data = json.load(file)

for i in data['imdata']:

    x = i["l1PhysIf"]["attributes"]

    lst.append({
        "id": x.get("id"),
        "layer": x.get("layer"),
        "usage": x.get("usage")
    })

for x in lst:
    print(x["id"], x["layer"], x["usage"])