'''
ePy GUI
this is GUI of ePy

Version: InDev
'''
from Tkinter import *
import tkMessageBox
import ttk
import multiprocessing
import time
from multiprocessing.dummy import Pool
from decimal import *
import math
import sys

root = Tk()
TIMER = StringVar()
### ePy_MC Mod ###

def one_div(fact):
    return Decimal(1)/fact

def e_cal(l, cores):
    '''
    e calculator
    this function will recive digits of float
    and calculate and print status during working.
    
    This function will return value of e.
    '''
    p = Pool()
    getcontext().prec = l
    e = Decimal(0)
    i = 0
    temp = 0
    c = 0
    while True:
        fact = p.map(math.factorial, range(i, i+cores)) #parallel process factorial
        e += sum(p.map(one_div, fact)) #processed factorial will total in here
        i += cores
        c += 1
        sys.stdout.write("\r%i loops passed." % (c) ) #Print Loop status
        sys.stdout.flush()
        #print i, "loops passed."
        if e == temp:
            break
        temp = e
    sys.stdout.write("\r%i loops passed.\n" % (c) )
    sys.stdout.flush()
    p.close()
    p.join()

    return e

###  ###



root.title("ePy bench")

Lb1 = Listbox(root)
Lb1.insert(1, "100")
Lb1.insert(2, "500")
Lb1.insert(3, "1000")
Lb1.insert(4, "2000")
Lb1.insert(5, "5000")
Lb1.insert(6, "10000")
Lb1.insert(7, "20000")
Lb1.insert(8, "50000")
   
def p():
    ran = False
    try:
        dig = Lb1.curselection()
        dig = int(Lb1.get(int(dig[0])))
        B.config(state=DISABLED)
        ran = True
        tkMessageBox.showinfo( "Warning", 'Are you ready to calculate '+str(dig)+' digits of e?')
        t = time.time()
        e_cal(dig, multiprocessing.cpu_count())
        TIMER.set(str(time.time()-t)+' sec.')
        B.config(state=NORMAL)
    except:
        if ran:
            tkMessageBox.showinfo( "Error", "You had force stop or somthing else error.")
        else:
            tkMessageBox.showinfo( "Error", "Please select value!")
        B.config(state=NORMAL)

B = Button(root, text ="Start", command = p)
Q = Button(root, text ="Quit", command = root.mainloop)
progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200)

progressbar.pack(side="bottom")
w = Spinbox(root, from_=0, to=multiprocessing.cpu_count())
w.pack()

stat = Label(root, textvariable=TIMER)
TIMER.set('N/A')

Lb1.pack()
B.pack()
stat.pack()

root.mainloop()
