import tkinter as tk

root = tk.Tk()
root.title("Drawing App")
root.geometry("600x600")

def draw_red_dot(event):
    x,y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')

def draw_blue_dot(event):
    x,y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

def on_key(event):
    if event.keysym == 'c':
        canvas.delete('all')
    if event.keysym == 'Escape':
        root.destroy()

canvas = tk.Canvas(root,bg='white')
canvas.pack(fill='both',expand=True)

canvas.bind("<Button-1>", draw_red_dot)
canvas.bind("<B1-Motion>", draw_red_dot)
canvas.bind("<Button-3>", draw_blue_dot)
canvas.bind("<B3-Motion>", draw_blue_dot)

root.bind("<Key>", on_key)
root.mainloop()