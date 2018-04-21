import Tkinter
import ttk
from Tkinter import *
from PIL import ImageTk, Image, ImageSequence
from AnimatedGIF import *

window = Tk()
window.title("Know your GPA!")
window.geometry('1300x300')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Variables to be used.
grade_PE = StringVar()
grade_chem = StringVar()
grade_bio = StringVar()
grade_phy = StringVar()
grade_math = StringVar()
grade_his = StringVar()

credit_PE = StringVar()
credit_chem = StringVar()
credit_bio = StringVar()
credit_phy = StringVar()
credit_math = StringVar()
credit_his = StringVar()

finalgpa = StringVar() # Output variables
feedback = StringVar()

# Function that calculates gpa
def gpa(*args):

    try:
        gpe=float(grade_PE.get())
        gchem=float(grade_chem.get())
        gbio=float(grade_bio.get())
        gphy=float(grade_phy.get())
        gmath=float(grade_math.get())
        ghis=float(grade_his.get())

        cpe=float(credit_PE.get())
        cchem=float(credit_chem.get())
        cbio=float(credit_bio.get())
        cphy=float(credit_phy.get())
        cmath=float(credit_math.get())
        chis=float(credit_his.get())

        # Provide standards for scores.
        grade_dict = {'A':4.0, 'B':3.0, 'C':2.0, 'D':1.0, 'F':0.0}
        all_grades = [gpe, gchem, gbio, gphy, gmath, ghis]
        all_credits = [cpe, cchem, cbio, cphy, cmath, chis]
        creditsum = cpe + cchem + cbio + cphy + cmath + chis

        # To be filled
        yourtotal = 0
        count = 0

        while count < len(all_credits):
            # Grade and credit for each subject
            grade = all_grades[count]
            credit = all_credits[count]
            scale = grade_dict[grade]

            # Calculation
            total = credit * scale
            yourtotal += total
            count += 1

        finalgpa = yourtotal / creditsum
	print(finalgpa)
    except ValueError:
        pass

# Make two frames: content and frame.
# The size of the mainframe should be flexible.
content = ttk.Frame(window, padding=(3, 3, 12, 12))
content.grid(column=0,row=0, sticky=(N, S, E, W))
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

border = ttk.Frame(content, borderwidth=3, relief='sunken', width=300, height=100,padding=(3, 3, 12, 12))
border.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
result = ttk.Frame(content, borderwidth=3, relief='sunken', width=200, height=100,padding=(3,3,12,12))
result.grid(column=3,row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
pictureframe = ttk.Frame(content, borderwidth=3, width=300,height=300, padding=(3,3,12,12))
pictureframe.grid(column=6,row=0,columnspan=3,rowspan=2,sticky=(N,S,E,W))

## We want the gif to be iterating (charmander really dancing boiii)
mygif = AnimatedGif(pictureframe, 'DfQqM.gif', 0.1)
mygif.pack()
mygif.start()

## Working on the left-hand side: contents frame.
# First column should have labels of all subjects.
ttk.Label(border, text="Fill your grades!", font=14).grid(row=1,column=1,padx=5,pady=5, sticky=(W,E))
ttk.Label(border, text="PE:",font=12).grid(row=2,column=1,padx=5,sticky=E)
ttk.Label(border, text="Chemistry:",font=12).grid(row=3,column=1,padx=5,sticky=E)
ttk.Label(border, text="Biology:",font=12).grid(row=4,column=1,padx=5,sticky=E)
ttk.Label(border, text="Physics:",font=12).grid(row=5,column=1,padx=5,sticky=E)
ttk.Label(border, text="Mathematics:",font=12).grid(row=6,column=1,padx=5,sticky=E)
ttk.Label(border, text="History:",font=12).grid(row=7,column=1,padx=5,sticky=E)

# Second column: Entries to type in assigned credits.
ttk.Label(border, text="Credits:", font=14).grid(row=1,column=2,padx=5,pady=5,sticky=(W,E))
ttk.Entry(border, textvariable=credit_PE,width=5,font=12).grid(row=2,column=2,padx=2,sticky=(W,E))
ttk.Entry(border, textvariable=credit_chem,width=5,font=12).grid(row=3,column=2,padx=2,sticky=(W,E))
ttk.Entry(border, textvariable=credit_bio,width=5,font=12).grid(row=4,column=2,padx=2,sticky=(W,E))
ttk.Entry(border, textvariable=credit_phy,width=5,font=12).grid(row=5,column=2,padx=2,sticky=(W,E))
ttk.Entry(border, textvariable=credit_math,width=5,font=12).grid(row=6,column=2,padx=2,sticky=(W,E))
ttk.Entry(border, textvariable=credit_his,width=5,font=12).grid(row=7,column=2,padx=2,sticky=(W,E))

# Third column: Comboboxes to select grades.
ttk.Label(border, text="Grade:", font=14).grid(row=1,column=3,padx=5,pady=5,sticky=W)

pebox = ttk.Combobox(border, textvariable=grade_PE,font=12)
pebox['values'] = ('A','B','C','D','F')
pebox.bind('<<ComboboxSelected>>', gpa)
pebox.grid(row=2,column=3,sticky=W)

chembox = ttk.Combobox(border, textvariable=grade_chem,font=12)
chembox['values'] = ('A','B','C','D','F')
chembox.bind('<<ComboboxSelected>>', gpa)
chembox.grid(row=3,column=3,sticky=W) 

biobox = ttk.Combobox(border, textvariable=grade_bio, font=12)
biobox['values'] = ('A','B','C','D','F')
biobox.bind('<<ComboboxSelected>>', gpa)
biobox.grid(row=4,column=3,sticky=W) 

phybox = ttk.Combobox(border, textvariable=grade_phy,font=12)
phybox['values'] = ('A','B','C','D','F')
phybox.bind('<<ComboboxSelected>>', gpa)
phybox.grid(row=5,column=3,sticky=W) 

matbox = ttk.Combobox(border, textvariable=grade_math,font=12)
matbox['values'] = ('A','B','C','D','F')
matbox.bind('<<ComboboxSelected>>', gpa)
matbox.grid(row=6,column=3,sticky=W)
 
hibox = ttk.Combobox(border, textvariable=grade_his,font=12)
hibox['values'] = ('A','B','C','D','F')
hibox.bind('<<ComboboxSelected>>', gpa)
hibox.grid(row=7,column=3,sticky=W)

# Make a Button to run calculation
ttk.Button(border, text='Submit',command=gpa).grid(row=8,column=2,padx=5,pady=5,sticky=(W,E))


## Working on the right-hand side: frame.
ttk.Label(result, text="Result:", font=14).grid(row=1,column=2,padx=5,pady=5,sticky=(W,E))
ttk.Label(result, text="Your gpa is").grid(row=2,column=1,padx=3,sticky=E)
ttk.Label(result, textvariable=finalgpa).grid(row=2,column=2,stick=(W,E))

window.bind('<Return>', gpa) 
window.mainloop()
