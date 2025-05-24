# file = open('D:\details.txt','r')
# content = file.read()
# print(content)
# file.close()

# with open('D:\details.txt','r') as file:
#     content = file.read()
#     print(content)

with open('D:\details.txt','w') as file:
    file.write("Zaw Ye Naung is so handsome!")

with open('D:\details.txt','a') as file:
    file.write("He also play football.")

with open('D:\details.txt','r') as file:
    content = file.read()
    print(content)