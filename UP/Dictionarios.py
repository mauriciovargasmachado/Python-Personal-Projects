

punto = {"x": 15.5, "y": 18.2}

print(punto)

print(punto["x"])
print(punto["y"])

punto["z"] = 85.3

print(punto)

print(punto, punto["z"])

if "x" in punto:
    print("found!!!")

print(punto.get("y"))

print(punto.get("x"), 8.8)

del (punto["y"])

print(punto)
