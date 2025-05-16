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
import  copy
info = {
    "name": "Zaw Ye Naung",
    "age": 24,
    "class": {
        "programming": "Python",
        "language": "English"
    }
}
new_dict = copy.deepcopy(info)
new_dict["class"]["maths"] = "Stochastics"
print(f"Original {info}")
print(f"Copy {new_dict}")



#
# info = {
#     "name": "Zaw Ye Naung",
#     "age": 24
# }
# copy = dict(info)
# print(copy)
#

