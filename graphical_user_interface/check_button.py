import tkinter as tk

root = tk.Tk()
root.title("Check Button")
root.geometry("300x300")

def show_answer():
    result = []
    if var1.get(): result.append("Option A")
    if var2.get(): result.append("Option B")
    label.config(text="Selected: " + ", ".join(result))

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

tk.Checkbutton(root,text="Option A",variable=var1).pack(padx=10)
tk.Checkbutton(root,text="Option B",variable=var2).pack(padx=10)

tk.Button(root,text="Submit",command=show_answer).pack(pady=10)

label = tk.Label(root,text="Choose!")
label.pack(pady=10)

root.mainloop()