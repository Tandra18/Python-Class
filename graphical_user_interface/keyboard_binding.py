import tkinter as tk

def on_press(event):
    print(f"You pressed {event.keysym}")

root = tk.Tk()
root.title("Keyboard Binding")
root.geometry("300x300")

root.bind("<Key>",on_press)
root.mainloop()

