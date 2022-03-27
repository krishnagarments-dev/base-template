from tkinter import *

top = Tk()
top.title("Sign Up")
head = Label(top,text="Sign Up")
head.grid(row=0,columnspan=3)

r = 1 # row
cl = 0 # column label
ce = 1 # column entry

# User code
lblusrcode = Label(top,text="User Code")
lblusrcode.grid(row=r,column=cl)

usercode = Entry(top)
usercode.grid(row=r,column=ce)

# Next
r += 1

# User name
lblusr = Label(top,text="Username")
lblusr.grid(row=r,column=cl)

username = Entry(top)
username.grid(row=r,column=ce)

# Next
r += 1

# Password
lblpass = Label(top,text="Password")
lblpass.grid(row=r,column=cl)

password = Entry(top)
password.grid(row=r,column=ce)

# Next
r += 1

# Confirm Password
lblconfirmpass = Label(top,text="Confirm Password")
lblconfirmpass.grid(row=r,column=cl)

confirmpassword = Entry(top)
confirmpassword.grid(row=r,column=ce)

# Next
r += 1

# Buttons

# # Signup
signup = Button(top,text="Sign Up")
signup.grid(row=r,column=0)

# # Cancel
cancel = Button(top,text="Cancel",command=top.destroy)
cancel.grid(row=r,column=1)

top.mainloop()
