import Tkinter
import ttk
from AnimatedGIF import *
from Tkinter import *
import tkMessageBox
import tkFileDialog
#from __future__ import absolute_import, division, print_function
import scipy.io.wavfile as wav
from deepspeech.model import Model
import time
import sox
from PIL import Image, ImageTk

parent = Tk()
parent.title('Speech to Text')
#parent.geometry('450x210')


## Definitions to be used.

# Confirmation

def directory():
    filename = tkFileDialog.askopenfilename(initialdir='/home/intern/2018_winter_internship/GUI_practice/models')
    only_filename = ''
    for letter in filename[::-1]:

        if letter == '/':
            break
        only_filename += letter

    audiofile.set(filename)
    audioprint.set(only_filename[::-1])


def helper():

    help = Toplevel(parent)
    help.title("Instruction")
    border = ttk.Frame(help, padding = (3,3,12,12))
    border.grid(row=0,column=0,sticky=(N,W,E,S))
    content = ttk.Frame(border, borderwidth=3, relief='sunken', padding=(3,3,12,12))
    content.grid(row=0,column=0,sticky=(N,W,E,S))

    ttk.Label(content, text="Instruction Steps:", font=14).pack(pady=5)
    ttk.Label(content, text="1. Import an Audio .wav file in the Entry",font=14).pack(pady=5)
    ttk.Label(content, text="2. Click 'Run' and confirm",font=14).pack(pady=5)
    ttk.Label(content, text="2. See the result!",font=14).pack(pady=5)
    ttk.Button(content, text='Got it', command=help.destroy).pack(pady=5)

def end_confirmation():
    if tkMessageBox.askokcancel("Quit","Are you sure?"):
	parent.quit()

#### DeepSpeech coming in! ####
def Deep():
    try:
        if tkMessageBox.askyesno("Confirmation","Would you like to proceed?"):
             
            BEAM_WIDTH = 500
            LM_WEIGHT = 1.75
            WORD_COUNT_WEIGHT = 1.00
            VALID_WORD_COUNT_WEIGHT = 1.00
            N_FEATURES =26
            N_CONTEXT = 9

            ds = Model('models/models.pb', N_FEATURES, N_CONTEXT, 'models/alphabet.txt', BEAM_WIDTH)

	    fs, audio = wav.read(audiofile.get())

	    if fs != 16000:
	    	cbn = sox.Combiner()
            	cbn.convert(samplerate=16000, n_channels=1)
            	cbn.build([str(audiofile.get())],'./','concatenate')
		fs, audio = wav.read('./')

            audio_length = len(audio) * (1/16000)

            resultpage = Toplevel(parent)
            resultpage.title("Result")
	    result_border = ttk.Frame(resultpage, padding=(12,12,12,12))
	    result_border.pack()
            result_page = Frame(result_border, bg = "white")
            result_page.pack() 

            Tkinter.Label(result_page, text="What I've heard from you:",font=14, bg="white").grid(row=1,column=1, sticky=E)
            Tkinter.Label(result_page, textvariable=word,font=12, bg="white").grid(row=2,column=2, sticky=E)

            word.set(ds.stt(audio,fs))

    except ValueError:
        tkMessageBox.showerror("Error!", "Only 16000Hz WAV files supported!")
    except IOError:
        tkMessageBox.showerror("Error!", "No file uploaded!")

# Inputs
audiofile = StringVar() # .wav
audioprint = StringVar()
word = StringVar()

mainframe = Frame(parent, bg='white')
mainframe.pack()

# Labels in frame1
Tkinter.Label(mainframe, text="Speech To Text", font=14, bg='white').grid(row=1,column=2,padx=5,pady=5,sticky=(W,E))
Tkinter.Label(mainframe, text="Import your file:", font=12, bg='white').grid(row=2,column=1,padx=5,pady=5,sticky=W)
Tkinter.Label(mainframe, text="Confirm your file:", font=12, bg='white').grid(row=3,column=1,padx=5,pady=5,sticky=W)
ttk.Button(mainframe, text="Upload!", command= directory).grid(row=2,column=2, padx=5,pady=5,sticky=(W,E))
ttk.Label(mainframe, textvariable=audioprint).grid(row=3,column=2,padx=5,pady=5,sticky=(W,E))
Tkinter.Label(mainframe, text='Copyrights GUGC', font=11, bg='white').grid(row=7, column=2, padx=5, sticky=(N,S,W))

# Logo image
load = Image.open('ghent.gif')
load = load.resize((80,70), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = ttk.Label(mainframe, image=render)
img.image = render
img.place(x=0, y=123)

# logo2
load2 = Image.open('Kakao.gif')
load2 = load2.resize((110,70))
render2 = ImageTk.PhotoImage(load2)

img2 = ttk.Label(mainframe, image=render2)
img2.image = render2
img2.place(x=81, y=123)

runbutton = ttk.Button(mainframe, text="Run", command = Deep)
runbutton.grid(row=4, column=3, sticky=E, padx=5, pady=5)

helpbutton = ttk.Button(mainframe, text="Help ?", command = helper)
helpbutton.grid(row=5, column=3, sticky=E, padx=5, pady=5)

closebutton = ttk.Button(mainframe, text="Close", command=end_confirmation)
closebutton.grid(row=6, column=3, sticky=E, padx=5, pady=5)

parent.mainloop()

