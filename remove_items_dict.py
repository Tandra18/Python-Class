# info = {
#     "name": "Zaw Ye Naung",
#     "age": 24,
#     "phone": "09261800607",
#     "address": "yangon"
# }
# info.pop("age")
# info.popitem()
# print(info)
#

info = {
    "name": "Zaw Ye Naung",
    "age": 24,
    "phone": "09261800607",
    "address": "yangon"
}
del info["address"]
print(info)
info.clear()
print(info)

