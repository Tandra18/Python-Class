import csv
import re

file_path = r'D:\contacts.csv'

def init_file():
    try:
        with open(file_path,'r') as file:
            pass
    except FileNotFoundError:
        with open(file_path,'w',newline='',encoding='utf-8') as file:
            print("Creating a new 'contacts.csv' file!")
            contacts_data = csv.writer(file)
            contacts_data.writerow(['Name','Phone','Email'])

def add_contact():
    while True:
        name = input("Enter name : ").strip().title()

        while True:
            phone = input("Enter phone : ").strip()
            phone_reg = re.match(r"09\d{8}", phone)
            if phone_reg:
                break
            else:
                print("Phone number must starts with '09' and have 11 digits! ")

        while True:
            email = input("Enter email : ").lower().strip()
            email_regex = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email, flags=re.IGNORECASE)
            if email_regex:
                break
            else:
                print("Please enter a valid email : ")


        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            contact_data = csv.writer(file)
            contact_data.writerow([name, phone, email])
        print("Contact added!")

        choice = input("Do you want to add one more? (yes/no) : ").lower()
        if choice == 'yes':
            pass
        elif choice == 'no':
            break
        else:
            print("Please inter 'yes' or 'no' !")


def view_contacts():
    with open(file_path,'r') as file:
        contacts_data = csv.reader(file)
        next(contacts_data)
        print("\n *** Contact List ***:")

        for i,row in enumerate(contacts_data):
            print(f"Id = {i}  | Name = {row[0]}, Phone = {row[1]}, Email = {row[2]}")

    while True:
        back = input("\nEnter 'esc' to go back to menu : ").lower()
        if back == 'esc':
            main()
        else:
            print("Invalid input!")

def main():
    init_file()
    while True:
        print("\n *** Contact Book Menu *** ")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Exit")

        choice = int(input("\nChoose options (1-3) : "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            print("\nGoodbye !")
            break
        else:
            print("Invalid choice. Try again !\n")

if __name__ == '__main__':
    main()