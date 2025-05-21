# import calculator
# from calculator import division
# from modules import text_analysis
#
# result1 = calculator.add(4,5)
# print(f"Addition is {result1}.")
#
# result2 = division(5,2)
# print(f"Division is {result2}.")
#
# import dictionary
# from dictionary import subjects
#
# address = dictionary.person['address']
# print(f"Address is {address}.")
#
# minor_sub = subjects['minor']
# print(f"Minor subject is {minor_sub}.")
#
# import text_analysis as ta
# from text_analysis import char_count as cc
#
# introduce = ta.word_count("I am Zaw Ye Naung")
# about = cc("I am a software developer")
# print(f"There are {introduce} words in introduce.")
# print(f"There are {about} characters in about.")

# import platform
#
# print(platform.system())
# print(platform.version())
# print(platform.platform())
# print(platform.processor())
# print(platform.architecture())
# print(platform.uname())

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