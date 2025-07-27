from tkinter import messagebox
from datetime import datetime

def create_employee(cur, conn, fields, photo_data, clear_fields, view_all):
    try:
        data = [fields[k].get() for k in fields]
        dob = datetime.strptime(data[2], "%d.%m.%Y").date()
        data[2] = dob

        cur.execute("""
            INSERT INTO employees (photo, name, age, dob, sex, education_background,
                marital_status, blood_type, phone, email, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (photo_data, *data))
        conn.commit()
        messagebox.showinfo("Success", "Employee added.")
        clear_fields()
        view_all()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))
