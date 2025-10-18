import json

# To convert JSON to Python we can use json.loads()
x = '{"name": "CQ", "age": 22, "city": "Kokomo"}'
y = '{"Purdue": ["Rawls", "HSEE", "Lawson"]}'

xx = json.loads(x)
yy = json.loads(y)

print(type(x))
print(yy)

# Takeaway, you can print entire variable, but can access certain parts
print(xx["name"])
print(yy["Purdue"][1])

# To convert Python to JSON we can use json.dumps()

a = {
    "name": "CQ",
    "age": 22,
    "city": "Kokomo"
}

b = json.dumps(a)

print(type(a))
print(b)

# All data types

all_py = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

all_json = json.dumps(all_py)

print(f"All Data Types Below ------------------------")

print(all_json)

