import tkinter as tk

root = tk.Tk()
root.title("My first Tkinter App")
root.geometry("400x300")

label = tk.Label(root,text="Hello Tkinter!")
label.pack()
#
# def greeting():
#     label.config(text="Hello Everyone!")
#
# button = tk.Button(root,text="Click me",command=greeting)
# button.pack()

root.mainloop()

