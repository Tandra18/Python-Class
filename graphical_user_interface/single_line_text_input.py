import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x300")

entry = tk.Entry(root)
entry.pack(pady=10)

label = tk.Label(root, text="Enter something!")
label.pack(pady=10)

def show_input():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

button = tk.Button(root, text="Submit", command=show_input)
button.pack()

root.mainloop()