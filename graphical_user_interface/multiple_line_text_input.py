import tkinter as tk

root = tk.Tk()
root.title("Multiple line input")
root.geometry("400x400")

def get_text():
    content = text.get("1.0",tk.END).strip()
    label.config(text=f"Text entered:\n{content}")


text = tk.Text(root,height=5,width=40)
text.pack(pady=10)

button = tk.Button(root,text="Get Text",command=get_text)
button.pack()

label = tk.Label(root,text="",justify="left")
label.pack(pady=10)

root.mainloop()