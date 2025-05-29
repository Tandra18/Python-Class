import tkinter as tk

def show_selected():
    selected = listbox.get(listbox.curselection())
    label.config(text=f"You selected : {selected}")

root = tk.Tk()
root.title("Listbox")
root.geometry("300x200")
root.configure(bg='lightblue')

listbox = tk.Listbox(root,width=20,height=4)
items = ["apple","banana","cherry","orange"]

for x in items:
    listbox.insert(tk.END,x)

listbox.pack()

btn = tk.Button(root,text="Show Selection",command=show_selected)
btn.pack(pady=10)

label = tk.Label(root,text="Choose!")
label.pack()
root.mainloop()