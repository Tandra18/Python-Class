import tkinter as tk
from tkinter import filedialog

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "w", encoding='utf-8') as file:
            file.write(text_area.get("1.0", tk.END))

root = tk.Tk()
root.title("Save File Example")

text_area = tk.Text(root, wrap="word", height=15)
text_area.pack(padx=10, pady=10)

save_btn = tk.Button(root, text="Save File", command=save_file)
save_btn.pack(pady=5)

root.mainloop()
