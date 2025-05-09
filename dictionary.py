
info = {
    "name": "Zaw Ye Naung",
    "age": 24,
    "phone": "09261800607"
}
print(info)
print(info["age"])

x = info.get("name")
print(x)

y = info.keys()
print(y)

info["address"] = "insein"
print(y)
print(info)

