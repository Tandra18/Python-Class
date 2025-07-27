from tkinter import *
from tkinter import messagebox
from PIL import Image as PilImage, ImageTk
from db import get_connection
from upload_photo import load_photo
from create import create_employee
from update import update_employee
from delete import delete_employee
from export_pdf import export_pdf
import io
from datetime import datetime

conn = get_connection()
cur = conn.cursor()
root = Tk()
root.title("Employee Manager")

fields = {
    "Name": StringVar(),
    "Age": StringVar(),
    "DOB": StringVar(),
    "Sex": StringVar(value=""),
    "Education": StringVar(),
    "Marital Status": StringVar(value=""),
    "Blood Type": StringVar(value=""),
    "Phone": StringVar(),
    "Email": StringVar(),
    "Address": StringVar()
}

sex_options = ["", "Male", "Female"]
marital_options = ["", "Single", "Married", "Divorced", "Widowed"]
blood_options = ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

photo_data = None
selected_id = None

def view_all():
    listbox.delete(0, END)
    cur.execute("SELECT employee_id, name FROM employees")
    for row in cur.fetchall():
        listbox.insert(END, f"{row[0]} - {row[1]}")

def load_selected(event):
    global selected_id, photo_data
    if not listbox.curselection():
        return
    emp_id = int(listbox.get(listbox.curselection()).split(" - ")[0])
    selected_id = emp_id
    cur.execute("SELECT * FROM employees WHERE employee_id = %s", (emp_id,))
    row = cur.fetchone()
    if row:
        _, photo_data, name, age, dob, sex, edu, marital, blood, phone, email, addr = row
        fields["Name"].set(name)
        fields["Age"].set(str(age))
        fields["DOB"].set(dob.strftime("%d.%m.%Y"))
        fields["Sex"].set(sex)
        fields["Education"].set(edu)
        fields["Marital Status"].set(marital)
        fields["Blood Type"].set(blood)
        fields["Phone"].set(phone)
        fields["Email"].set(email)
        fields["Address"].set(addr)
        if photo_data:
            img = PilImage.open(io.BytesIO(photo_data)).resize((100, 100))
            photo_label.img = ImageTk.PhotoImage(img)
            photo_label.configure(image=photo_label.img)

def clear_fields():
    global selected_id, photo_data
    for var in fields.values():
        var.set("")
    selected_id = None
    photo_data = None
    photo_label.configure(image="")
    photo_label.img = None

row_idx = 0
for label, var in fields.items():
    Label(root, text=label).grid(row=row_idx, column=0, sticky=W)
    if label == "Sex":
        OptionMenu(root, var, *sex_options).grid(row=row_idx, column=1, sticky=W)
    elif label == "Marital Status":
        OptionMenu(root, var, *marital_options).grid(row=row_idx, column=1, sticky=W)
    elif label == "Blood Type":
        OptionMenu(root, var, *blood_options).grid(row=row_idx, column=1, sticky=W)
    else:
        Entry(root, textvariable=var, width=30).grid(row=row_idx, column=1)
    row_idx += 1

Button(root, text="Load Photo", command=lambda: set_photo(load_photo(photo_label))).grid(row=0, column=2)
photo_label = Label(root)
photo_label.grid(row=1, column=2, rowspan=3)

def set_photo(data):  # helper to update photo_data
    global photo_data
    photo_data = data

Button(root, text="Create", command=lambda: create_employee(cur, conn, fields, photo_data, clear_fields, view_all)).grid(row=11, column=0)
Button(root, text="Update", command=lambda: update_employee(cur, conn, selected_id, fields, photo_data, clear_fields, view_all)).grid(row=11, column=1)
Button(root, text="Delete", command=lambda: delete_employee(cur, conn, selected_id, clear_fields, view_all)).grid(row=12, column=0)
Button(root, text="Export PDF", command=lambda: export_pdf(cur)).grid(row=12, column=1)

listbox = Listbox(root, width=50)
listbox.grid(row=13, column=0, columnspan=2)
listbox.bind("<<ListboxSelect>>", load_selected)

view_all()
root.mainloop()
