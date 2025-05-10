# info = {
#     "name": "Zaw Ye Naung",
#     "age": 24
# }
# print("Original : ", info)
#
# copy = info  # This is a reference copy
# print(f"Copy : {copy}")
#
# copy["age"] = 30  # Modify copied dictionary
#
# print("Modified copy : ", copy)
# print("Original : ", info)
#

info = {
    "name": "Zaw Ye Naung",
    "age": 24
}
copy = info.copy()
print(copy)

info = {
    "name": "Zaw Ye Naung",
    "age": 24
}
copy = dict(info)
print(copy)


