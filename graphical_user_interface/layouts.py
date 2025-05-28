import tkinter as tk

def submit():
    name = entry_username.get().strip().title()
    pwd = entry_pwd.get()
    label_result.config(text=f"Name : {name}\nPwd : {pwd}")

root = tk.Tk()
root.title("Layout Example")
root.geometry("300x300")
root.resizable(False,False)

frame_header = tk.Frame(root,bg='lightblue')
frame_header.pack(fill='x')

tk.Label(frame_header,text="Login Form",bg="yellow").pack()

frame_form = tk.Frame(root,bg='red')
frame_form.pack(fill='x')

tk.Label(frame_form,text="username",bg='violet').grid(row=0,column=0)
entry_username = tk.Entry(frame_form)
entry_username.grid(row=0,column=1,pady=5)

tk.Label(frame_form,text="password",bg='violet').grid(row=1,column=0)
entry_pwd = tk.Entry(frame_form)
entry_pwd.grid(row=1,column=1,pady=5)

frame_button = tk.Frame(root,height=50,width=100,bg='green')
frame_button.pack(fill='x')

btn_sign_in = tk.Button(frame_button,text="Sign In",command=submit,bg='lightblue')
btn_sign_in.place(x=80,y=10)

btn_sign_up = tk.Button(frame_button,text="Sign Up",command=submit,bg='lightblue')
btn_sign_up.place(x=160,y=10)

label_result = tk.Label(root,text='',fg='white',bg='black')
label_result.pack(pady=10,fill='x')

root.mainloop()