#
# info = {
#     "name": "Zaw Ye Naung",
#     "age": 24,
#     "phone": "09000000000"
# }
# print(info)
# print(info["age"])
#
# x = info.get("name")
# print(x)
#
# y = info.keys()
# print(y)
#
# info["address"] = "insein"
# print(y)
# print(info)
#

#from keys
keys = ['Saloon','SUV']
cars = dict.fromkeys(keys,[])
cars['Saloon'].append("Belta")
cars['Saloon'].append("Crown")
print(cars)