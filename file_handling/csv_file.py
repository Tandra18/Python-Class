# import csv
#
# with open(r'D:\details.csv',newline='',encoding='utf-8') as csvfile:
#     csv_content = csv.reader(csvfile)
#     for row in csv_content:
#         print(row)

# import csv
#
# with open(r'D:\details.csv',newline='',encoding='utf-8') as csvfile:
#     csv_content = csv.DictReader(csvfile)
#     for row in csv_content:
#         print(row)

# import csv
#
# with open(r'D:\exam.csv','w',newline='',encoding='utf-8') as csvfile:
#     csv_content = csv.writer(csvfile)
#     csv_content.writerow(['Name','Subject','Marks'])
#     csv_content.writerow(['Mg Mg','English',73])
#     csv_content.writerow(['Hla Hla','Myanmar',45])

import csv
data = [
    {'Fruits': 'Apple','Price': 800},
    {'Fruits': 'Banana','Price': 1000}
]
with open(r'D:\fruits.csv','w',newline='',encoding='utf-8') as csvfile:
    headers = ['Fruits','Price']
    csv_content = csv.DictWriter(csvfile,fieldnames=headers)

    csv_content.writeheader()
    csv_content.writerows(data)

# import csv
#
# with open(r'D:\details.csv','a+',newline='',encoding='utf-8') as csvfile:
#     updated_data = csv.writer(csvfile)
#     updated_data.writerow(['Yin Mon',32,'Yangon'])
#
#     csvfile.seek(0)
#     for row in csv.reader(csvfile):
#         print(row)
#
