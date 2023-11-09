from tkinter import*
from PIL import ImageTk,Image #use command ->pip install pillow to isntall this libraray

root= Tk(); #object of tk library 
root.title("Login form")# adding title 
#root.iconbitmap('logo.jpeg')#adding logo
# root.minsize(500,500)#fix the size of windows you can use maxsize
#for particular size use -> geometry(200x300)
root.geometry('350x500')
img=Image.open('logo.jpeg')
resize_image=img.resize((70,70))
img=ImageTk.PhotoImage(resize_image) #use to import image
img=ImageTk.PhotoImage(resize_image)
imag_label=Label(root,image=img) #to show on screen
imag_label.pack(pady=(10,10))#pady ye btata ha k apko upper or neechy sy kitni jaga chaye 
root.mainloop() #use to show screen when we not show screen then 
