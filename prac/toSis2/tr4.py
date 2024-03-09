import json

data = '{"name": "John", "age": 30, "city": "New York","number": 8708080808}'

x = json.loads(data)

key = str(input("input key: "))

print(x[key])