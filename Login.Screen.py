# from tkinter import*
# from PIL import ImageTk,Image #use command ->pip install pillow to isntall this libraray

# root= Tk(); #object of tk library 
# root.title("Login form")# adding title 
# #root.iconbitmap('logo.jpeg')#adding logo
# # root.minsize(500,500)#fix the size of windows you can use maxsize
# #for particular size use -> geometry(200x300)
# root.geometry('350x500')
# img=Image.open('logo.jpeg')
# resize_image=img.resize((70,70))
# img=ImageTk.PhotoImage(resize_image) #use to import image
# img=ImageTk.PhotoImage(resize_image)
# imag_label=Label(root,image=img) #to show on screen
# imag_label.pack(pady=(10,10))#pady ye btata ha k apko upper or neechy sy kitni jaga chaye 


# #now we will use flip card -> to use it use label
# text_label=Label(root,text="FlipCart")
# text_label.pack()
# text_label.config(font=('vardana',28))# config is use for font and  size

# enter_mail=Label(root,text='Enter Email')
# enter_mail.pack(pady=(20,5))
# input_mail=Entry(root)
# input_mail.pack(ipady=6,pady=(1,15))
# enter_pass=Label(root,text="Enter Password")
# enter_pass.pack(pady=(20,5))
# input_pass=Entry(root)
# input_pass.pack(ipady=6,pady=(1,15))


# #button

# login_btn=Button(root,text='Login')
# login_btn.pack()
# root.mainloop() #use to show screen when we not show screen then 

from tkinter import *
from tkinter import messagebox  # Import messagebox module for showing dialogs
from PIL import ImageTk, Image  # Use command ->pip install pillow to install this library

def validate_login():
    entered_email = input_mail.get()
    entered_password = input_pass.get()

    if entered_email == "usamanasir786999@gmail.com" and entered_password == "1234":
        message = "Correct Login"
    else:
        message = "Wrong Login"

    messagebox.showinfo("Login Status", message)

root = Tk()
root.title("Login form")
root.geometry('350x500')

img = Image.open('logo.jpeg')
resize_image = img.resize((70, 70))
img = ImageTk.PhotoImage(resize_image)
imag_label = Label(root, image=img)
imag_label.pack(pady=(10, 10))

text_label = Label(root, text="FlipCart")
text_label.pack()
text_label.config(font=('vardana', 28))

enter_mail = Label(root, text='Enter Email')
enter_mail.pack(pady=(20, 5))
input_mail = Entry(root)
input_mail.pack(ipady=6, pady=(1, 15))

enter_pass = Label(root, text="Enter Password")
enter_pass.pack(pady=(20, 5))
input_pass = Entry(root, show="*")  # Password field, characters are hidden
input_pass.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login', command=validate_login)
login_btn.pack()

root.mainloop()
