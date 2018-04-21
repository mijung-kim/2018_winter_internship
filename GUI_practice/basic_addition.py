# Very simple calculator
# Mainly compatible with python 2.7

import Tkinter
import ttk
from Tkinter import *
from PIL import ImageTk, Image
 
# Command - addition
def addition(*args):

    try:
        fint = float(finlet.get())
        sint = float(sinlet.get())
        outlet.set(fint + sint)

    except ValueError:
        pass

# Command - change color

def chcolor(*args):

    try:
        c = newcolor.get()
        window.configure(background = c)

    except ValueError:
        pass

# Make a blank window
window = Tk()
window.title("Color and Addition")
window.geometry('700x200')

# Inputs
finlet = StringVar()
sinlet = StringVar()
outlet = StringVar()
newcolor = StringVar()

# Plan a ttk grid -> setup your window.
ttk.Label(window, text = "Your desired Color?").grid(row=1,column=2, sticky=(W,E))
ttk.Label(window, text = "Select color:").grid(row=2,column=1, sticky=E)

colorvar = ttk.Combobox(window, textvariable=newcolor)
colorvar['values'] = ('black','blue','red','green','yellow','orange','white')
colorvar.bind('<<ComboboxSelected>>', chcolor)
colorvar.grid(row=2,column=2,sticky=(W,E))

ttk.Label(window, text = "Current color:").grid(row=3,column=1, sticky=E)
ttk.Label(window, textvariable=newcolor).grid(row=3,column=2, sticky=(W,E))

ttk.Label(window, text="First Integer:").grid(row=5, column=1, sticky=E)
finlet_entry = ttk.Entry(window, width=7, textvariable=finlet)
finlet_entry.grid(row=5, column=2, sticky =(W,E))

ttk.Label(window, text="Second Integer:").grid(row=6, column=1, sticky=E)
sinlet_entry = ttk.Entry(window, width=7, textvariable=sinlet)
sinlet_entry.grid(row=6, column=2, sticky=(W,E))

ttk.Label(window, text="Result:").grid(row=7, column=1, sticky=E)
ttk.Button(window, text="Add'em!", command = addition).grid(column=3,row=6,sticky=W)
ttk.Label(window, textvariable=outlet).grid(row=6, column=2,sticky=(W,E))

for child in window.winfo_children(): child.grid_configure(padx=5, pady=5)
#for child in mainframe.winfo_children(): child.grid_configrue(padx=5, pady=5)

# Inputs for second frames
#entrint = StringVar()

# Factors calculation.
#ttk.Label(mainframe, text='Factor Calculation').grid(row=1,column=2, sticky=(W,E))
#ttk.Label(mainframe, text='Input Integer:').grid(row=2,column=1,sticky=E)
#int_entry = ttk.Entry(mainframe, textvariable=entrint, width=7)
#int.entry.grid(row=2,column=2,sticky=(W,E))

#ttk.Button(mainframe, text='Go!', command = factor).grid(row=2,column=3,sticky=W)



finlet_entry.focus()
window.bind('<Return>', addition)

window.mainloop()

