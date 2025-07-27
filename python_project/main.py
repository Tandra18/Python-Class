from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image as PilImage, ImageTk
from db import get_connection
from upload_photo import load_photo
from create import create_employee
from update import update_employee
from delete import delete_employee
from export_pdf import export_pdf
import io
from datetime import datetime

# Database setup
conn = get_connection()
cur = conn.cursor()

# Root Window
root = Tk()
root.title("Employee Manager")
root.geometry("900x650")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TEntry", font=("Segoe UI", 10))
style.configure("TCombobox", font=("Segoe UI", 10))

# Data Fields
fields = {
    "Employee ID": StringVar(),
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

# Default blank image (white 80x100)
blank_img = PilImage.new("RGB", (80, 100), color="white")
blank_tk = ImageTk.PhotoImage(blank_img)

# Functions
def view_all():
    listbox.delete(0, END)
    cur.execute("SELECT employee_id, name FROM employees ORDER BY employee_id")
    for row in cur.fetchall():
        listbox.insert(END, f"{row[0]} - {row[1]}")

def search_by_name():
    name_query = search_var.get().strip()
    if name_query == "":
        view_all()
        return
    listbox.delete(0, END)
    cur.execute("SELECT employee_id, name FROM employees WHERE name ILIKE %s", (f"%{name_query}%",))
    results = cur.fetchall()
    if results:
        for row in results:
            listbox.insert(END, f"{row[0]} - {row[1]}")
    else:
        messagebox.showinfo("No Results", f"No employee found with name '{name_query}'.")

def load_selected(event):
    global selected_id, photo_data
    if not listbox.curselection():
        return
    emp_id = int(listbox.get(listbox.curselection()).split(" - ")[0])
    selected_id = emp_id
    cur.execute("SELECT * FROM employees WHERE employee_id = %s", (emp_id,))
    row = cur.fetchone()
    if row:
        employee_id, photo_data, name, age, dob, sex, edu, marital, blood, phone, email, addr = row
        fields["Employee ID"].set(str(employee_id))
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
            img = PilImage.open(io.BytesIO(photo_data)).resize((80, 100))
            photo_label.img = ImageTk.PhotoImage(img)
            photo_label.configure(image=photo_label.img)

def clear_fields():
    global selected_id, photo_data
    for var in fields.values():
        var.set("")
    selected_id = None
    photo_data = None
    photo_label.configure(image=blank_tk)
    photo_label.img = blank_tk

def set_photo(data):
    global photo_data
    photo_data = data
    if data:
        img = PilImage.open(io.BytesIO(data)).resize((80, 100))
        photo_label.img = ImageTk.PhotoImage(img)
        photo_label.configure(image=photo_label.img)

# Title
title_label = Label(root, text="Employee Manager", font=("Segoe UI", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)

# --- Search Box ---
search_frame = ttk.Frame(root, padding=(10, 5))
search_frame.pack(fill=X, padx=10)

search_var = StringVar()
ttk.Label(search_frame, text="Search by Name:").pack(side=LEFT, padx=(0, 5))
ttk.Entry(search_frame, textvariable=search_var, width=30).pack(side=LEFT)
ttk.Button(search_frame, text="Search", command=search_by_name).pack(side=LEFT, padx=(5, 10))
ttk.Button(search_frame, text="Show All", command=view_all).pack(side=LEFT)

# --- Main Layout ---
main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=BOTH, expand=True)

# --- Form Frame ---
form_frame = ttk.LabelFrame(main_frame, text="Employee Information", padding=10)
form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

row_idx = 0
for label, var in fields.items():
    ttk.Label(form_frame, text=label + ":").grid(row=row_idx, column=0, sticky=W, pady=5)
    if label in ["Sex", "Marital Status", "Blood Type"]:
        options = sex_options if label == "Sex" else marital_options if label == "Marital Status" else blood_options
        ttk.Combobox(form_frame, textvariable=var, values=options, width=27, state="readonly").grid(row=row_idx, column=1)
    elif label == "Employee ID":
        ttk.Entry(form_frame, textvariable=var, width=30, state="readonly").grid(row=row_idx, column=1)
    else:
        ttk.Entry(form_frame, textvariable=var, width=30).grid(row=row_idx, column=1)
    row_idx += 1

# --- Photo Frame ---
photo_frame = ttk.LabelFrame(main_frame, text="Photo", padding=10)
photo_frame.grid(row=0, column=1, sticky="n", padx=10, pady=10)

photo_label = Label(photo_frame, bg="white", width=80, height=100, relief=SOLID, bd=1)
photo_label.pack()
photo_label.configure(image=blank_tk)
photo_label.img = blank_tk

ttk.Button(photo_frame, text="Load Photo", command=lambda: set_photo(load_photo(photo_label))).pack(pady=5)

# --- Buttons ---
btn_frame = ttk.Frame(main_frame, padding=10)
btn_frame.grid(row=1, column=0, columnspan=2)

ttk.Button(btn_frame, text="Create", width=15,
           command=lambda: create_employee(cur, conn, fields, photo_data, clear_fields, view_all)).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Update", width=15,
           command=lambda: update_employee(cur, conn, selected_id, fields, photo_data, clear_fields, view_all)).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Delete", width=15,
           command=lambda: delete_employee(cur, conn, selected_id, clear_fields, view_all)).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="Export PDF", width=15,
           command=lambda: export_pdf(cur)).grid(row=0, column=3, padx=5)

# --- Listbox Frame ---
list_frame = ttk.LabelFrame(root, text="Employee List", padding=10)
list_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

listbox = Listbox(list_frame, font=("Segoe UI", 10), width=90, height=8)
listbox.pack(fill=BOTH, expand=True)
listbox.bind("<<ListboxSelect>>", load_selected)

view_all()
root.mainloop()
