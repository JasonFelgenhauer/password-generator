from tkinter import *
import secrets
import string

# Function for generate password


def generate_password():
    alphabet = string.ascii_letters + string.digits
    random_pass = ''.join(secrets.choice(alphabet) for i in range(20))
    password.delete(0, END)
    password.insert(0, random_pass)


# Create window
root = Tk()
root.title('Password Generator')
root.geometry('800x400')
root.minsize(800, 400)
root.iconbitmap('./assets/img/password.ico')
root.config(background='#13293D')

# Create frame
frame = Frame(root, bg='#13293D')
frame.pack(expand=YES)

# Create border white
border_1 = Frame(frame, background='#FFFFFC', padx=5, pady=5)
border_1.pack()

# Create title
title = Label(border_1, text='PASSWORD', font=('Arial', 40), fg='#FFFFFC', bg='#13293D',)
title.pack()

# Create button
button = Button(border_1, text='GENERATE', fg='#13293D', bg='#FFFFFC', font=('Arial', 20), bd=0, activebackground='#13293D', activeforeground='#FFFFFC', command=generate_password)
button.pack(fill=X)

# Create password text
password = Entry(frame, bg='#6CCFF6', fg='#13293D', font=('Arial', 15), bd=0)
password.pack(pady=50, fill=X)

root.mainloop()