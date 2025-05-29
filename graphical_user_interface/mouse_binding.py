import tkinter as tk

def on_click(event):
    if event.num == 1:
        print(f"Left clicked at ({event.x}, {event.y})")
    if event.num == 3:
        print(f"Right clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Mouse Binding")
root.geometry("300x200")

frame = tk.Frame(root,width=300,height=200,bg="lightblue")

left_click = frame.bind("<Button-1>",on_click)
right_click = frame.bind("<Button-3>",on_click)
frame.pack()

root.mainloop()