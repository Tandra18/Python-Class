from tkinter import messagebox
from datetime import datetime

def update_employee(cur, conn, selected_id, fields, photo_data, clear_fields, view_all):
    if not selected_id:
        return
    try:
        data = [fields[k].get() for k in fields]
        dob = datetime.strptime(data[2], "%d.%m.%Y").date()
        data[2] = dob

        cur.execute("""
            UPDATE employees SET photo=%s, name=%s, age=%s, dob=%s, sex=%s, education_background=%s,
            marital_status=%s, blood_type=%s, phone=%s, email=%s, address=%s
            WHERE employee_id=%s
        """, (photo_data, *data, selected_id))
        conn.commit()
        messagebox.showinfo("Updated", "Employee updated.")
        clear_fields()
        view_all()
    except Exception as e:
        conn.rollback()
        messagebox.showerror("Error", str(e))
