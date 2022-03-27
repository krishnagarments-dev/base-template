# Template of simple tkinter login page
from tkinter import *

root = Tk()
root.title("Login")
root.resizable(False, False)

head = Label(root,text="Login")
head.grid(row=0,columnspan=4)

lblusr = Label(root,text="Username")
lblusr.grid(row=1,column=0)

usr = Entry(root)
usr.grid(row=1,column=1)

lblpass = Label(root,text="Password")
lblpass.grid(row=2,column=0)

passwd = Entry(root,show="*")
passwd.grid(row=2,column=1)

# Login
login = Button(root,text="Login")
login.grid(row=3,column=0)

# Cancel
cancel = Button(root,text="Cancel",command=root.destroy)
cancel.grid(row=3,column=1)

root.mainloop()