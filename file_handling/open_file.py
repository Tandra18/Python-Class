# file = open('D:\details.txt','r')
# content = file.read()
# print(content)
# file.close()


# with open('D:\details.txt','r') as file:
#     content = file.read()
#     print(content)



# with open('D:\details.txt','w') as file:
#     file.write("Zaw Ye Naung is so handsome!")
#
# with open('D:\details.txt','a') as file:
#     file.write("He also play football.")
#
# with open('D:\details.txt','r') as file:
#     content = file.read()
#     print(content)

# try:
#     with open(r'D:\fruits.txt','x') as file:
#         file.write("apple, banana, orange")
#
# except FileExistsError:
#     print("File name already exists!")


# with open(r'D:\fruits.txt','r+') as file:
#     content = file.read()
#     print("Original : ",content)
#
#     file.write(" are my favorite!")
#     file.seek(0)
#     print("Updated : ",file.read())

# with open(r'D:\fruits.txt','w+') as file:
#     file.write("I don't like other fruits!")
#     file.seek(0)
#     print(file.read())


# with open(r'D:\fruits.txt','a+') as file:
#     file.write("I like apple, banana and orange!")
#     file.seek(0)
#     print(file.read())
#

# import os
#
# if os.path.exists(r'D:\details.txt'):
#     os.remove(r'D:\details.txt')
#     print("File deleted!")
# else:
#     print("File doesn't exist!")

# import os
#
# if os.path.exists(r'D:\my folder'):
#     os.rmdir(r'D:\my folder')
#     print("Folder deleted!")
# else:
#     print("Folder not found!")

import os
import shutil

if os.path.exists(r'D:\my folder'):
    shutil.rmtree(r'D:\my folder')
    print("Folder deleted!")
else:
    print("Folder not found!")

os.makedirs(r'D:\my folder')
print("Folder recreated successfully.")

