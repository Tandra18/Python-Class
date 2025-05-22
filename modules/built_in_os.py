import os

print(os.getcwd())
# os.mkdir(r"D:\testing")
print(os.listdir())


if os.path.exists(r"D:\data.txt"):
    print("It exist!")
else:
    print("It doesn't exist!")

print(os.path.isfile(r"D:\data.txt"))
print(os.path.isdir(r"D:\testing"))

os.rmdir(r"D:\testing")
os.remove(r"D:\hello.txt")