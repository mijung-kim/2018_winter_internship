import Tkinter
import ttk
from Tkinter import *
import tkMessageBox
import tkFont
from PIL import ImageTk, Image

root = Tk()
root.title = 'Put image'

frame = Canvas(bg='black',height=600,width=900)
frame.pack(side='top')
back_image = PhotoImage('/home/intern/2018_winter_internship/GUI_practice/giphy.gif')
image = frame.create_image(900. 50, anchor= NE, image=back_image) 

frame.pack()
root.mainloop()


