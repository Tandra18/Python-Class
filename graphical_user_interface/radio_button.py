import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x200")

def show_choice():
    label.config(text=f"Selected: {choice.get()}")

choice = tk.StringVar(value="Option 1")

tk.Radiobutton(root, text="Option 1", variable=choice, value="Option 1").pack()
tk.Radiobutton(root, text="Option 2", variable=choice, value="Option 2").pack()

tk.Button(root, text="Submit", command=show_choice).pack(pady=10)
label = tk.Label(root, text="Enter your choice")
label.pack()

root.mainloop()
