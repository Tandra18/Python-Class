import tkinter as tk

root = tk.Tk()
root.title("Radio Button")
root.geometry("600x450")

myanmar_font = ("Pyidaungsu", 15)

def show_choice():
    label.config(text=f"သင် '{choice.get()}' ကိုရွေးချယ်ခဲ့ပါတယ်။"
                      f"\nငါလိုးမစောက်ခြောက်!",font=myanmar_font)

choice = tk.StringVar(value="ဟုတ်")

tk.Label(root, text="ကွက်လပ်ဖြည့်ပါ!",font=myanmar_font).pack(pady=5)
tk.Label(root, text="၁။ _____၊ ကျွန်တော်က ဂေးလေ။  (၁၀ မှတ်)",
         font=myanmar_font).pack(anchor='w',padx=10)

tk.Radiobutton(root, text="ဟုတ်", variable=choice, value="ဟုတ်",
               font=myanmar_font).pack(anchor='w',padx=10)
tk.Radiobutton(root, text="မဟုတ်ပါဘူး", variable=choice, value="မဟုတ်ပါဘူး",
               font=myanmar_font).pack(anchor='w',padx=10)
tk.Radiobutton(root, text="မပြောတတ်ဘူး", variable=choice, value="မပြောတတ်ဘူး",
               font=myanmar_font).pack(anchor='w',padx=10)

tk.Button(root, text="ဝန်ခံမယ်", command=show_choice,
          font=myanmar_font).pack(pady=10)

label = tk.Label(root, text="ဝန်ခံလိုက်ပါ မိတ်ဆွေ!",font=myanmar_font)
label.pack(pady=10)

root.mainloop()
