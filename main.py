from tkinter import *


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
button = Button(border_1, text='GENERATE', fg='#13293D', bg='#FFFFFC', font=('Arial', 20), bd=0, activebackground='#13293D', activeforeground='#FFFFFC')
button.pack(fill=X)

# Create password text
password = Entry(frame, bg='#6CCFF6', fg='#13293D', font=('Arial', 15), bd=0)
password.pack(pady=50, fill=X)

root.mainloop()