import tkinter as tk

def on_press(event):
    if event.keysym == "Escape":
        root.destroy()

root = tk.Tk()
root.title("Escape")
root.geometry("300x400")

root.bind("<Escape>",on_press)
root.mainloop()

