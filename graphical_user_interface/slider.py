import tkinter as tk

def show_value(value):
    label.config(text=f"Value is : {value}")
root = tk.Tk()
root.title("Slider")

scale = tk.Scale(root,from_=0,to=100,orient='horizontal',command=show_value)
scale.pack()

label = tk.Label(root,text="")
label.pack()

root.mainloop()

