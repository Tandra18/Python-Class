import tkinter as tk

def click(number):
    entry.insert(tk.END, str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18),
                 borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for btn in buttons:
    action = lambda x=btn: calculate() if x == '=' else click(x)
    tk.Button(root, text=btn, width=5, height=2, font=('Arial', 14),
              command=clear if btn == 'C' else action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

(tk.Button(root, text='C', width=5, height=2,
          font=('Arial', 14), command=clear).grid(row=row, column=0, columnspan=4, pady=5))

root.mainloop()
