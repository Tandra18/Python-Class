myclass = {
    "student_1": {
        "name": "pyae pyae",
        "age": 20,
        "uni": "TTU"
    },
    "student_2": {
        "name": "hsu lei hnin",
        "age": 21,
        "uni": "TTU"
    },
    "student_3": {
        "name": "thin nandar",
        "age": 22,
        "uni": "TCU"
    }
}
print(myclass)
print(myclass["student_1"]["name"])

for x, y in myclass.items():
    print("\n" + x)
    for z in y:
        print(z + f" : {y[z]}")
