"""
Title: ePy Bench GUI
Language: Python 2.7
Version: Alpha test

This program is a part of PSIT project 2014 @ITKMITL.
Developed by Sakan Promlainak and Tanakrit Tangdamrongsap
"""

import Tkconstants, tkFileDialog
import tkMessageBox
import ttk
import multiprocessing
import time
import math
import sys
import AboutGUI as ab
from Tkinter import *
from multiprocessing.dummy import Pool
from decimal import *

##---ePy_MC Mod --------------------------------------------------------------##

def one_div(num):
    return Decimal(1)/num

def e_cal(l, cores):
    
    """
    e calculator in multi thread mode
    this function will recive digits of float
    and calculate and print status during working.
    
    This function will return value of e.
    """
    global PROGRESSED
    end = {100:80, 500:264, 1000:464, 2000:824, 5000:1784, 10000:3264, 20000:5992,
           50000:13536}
    p = Pool(cores)
    getcontext().prec = l+1
    e = Decimal(0)
    i = 0
    temp = 0
    temp_fact = 0
    c = 0
    prog_stat = 0
    while active_stat.get():
        fact = p.map(math.factorial, xrange(i, i+cores)) #parallel process factorial
        e += sum(p.map(one_div, fact)) #processed factorial will total in here
        x = float((i-temp_fact))/end[l]
        prog_stat += x
        PROGRESSED = prog_stat
        progressbar.step(x)
        progressbar.grid(row=5, columnspan=2)
        root.update()
        temp_fact = i
        i += cores
        c += 1
        if e == temp:
            break
        temp = e
    progressbar.step(-prog_stat)
    progressbar.grid(row=5, columnspan=2)
    root.update()
    p.close()
    p.join()
    return e

def e_cal_sc(l):
    
    """
    e calculator in single thread mode
    this function will recive digits of float
    and calculate and print status during working.
    
    This function will return value of e.
    """
    global PROGRESSED
    end = {100:72, 500:255, 1000:465, 2000:810, 5000:1784, 10000:3264, 20000:5992,
           50000:13536}
    getcontext().prec = l+1
    e = Decimal(0)
    i = 0
    temp = 0
    temp_fact = 0
    c = 0
    prog_stat = 0
    while active_stat.get():
        fact = math.factorial(i)
        e += Decimal(1)/fact
        x = float((i-temp_fact))/end[l]
        prog_stat += x
        PROGRESSED = prog_stat
        progressbar.step(x)
        progressbar.grid(row=5, columnspan=2)
        root.update()
        temp_fact = i
        i += 1
        c += 1
        if e == temp:
            break
        temp = e
    progressbar.step(-prog_stat)
    progressbar.grid(row=5, columnspan=2)
    root.update()
    return e

##----------------------------------------------------------------------------##

def p():
    global E, TIMER_NUM, PROGRESSED, SCORE
    ran = False
    
    try:
        dig = int(digit_select_box.get())
        B.config(state=DISABLED)
        ran = True
        if dig not in [100,500,1000,2000,5000,10000,20000,50000]:
            tkMessageBox.showerror( "Error", "Invalid digit number.")
            B.config(state=NORMAL)
            return None
        else:
            if tkMessageBox.askyesno( "Warning", "Are you ready to calculate "+str(dig)+" digits of e?"):
                stop_b.config(state=NORMAL)
                t = time.time()
                if int(cores.get()) == 0:
                    t = time.time()
                    E = e_cal_sc(dig)
                else:
                    t = time.time()
                    E = e_cal(dig, multiprocessing.cpu_count())
                if active_stat.get():
                    TIMER_NUM = str(time.time()-t)
                    TIMER.set(TIMER_NUM+" sec.")
                    SCORE.set(str(int(score(dig, float(TIMER_NUM))))+'P')
                else:
                    TIMER.set("- sec.")
                    SCORE.set("-")
                active_stat.set(True)
                B.config(state=NORMAL)
            else:
                B.config(state=NORMAL)
    except:
        if ran:
            tkMessageBox.showerror( "Error", "You had force stop or somthing else error.")
            progressbar.step(-PROGRESSED)
            progressbar.grid(row=5, columnspan=2)
            root.update()
        else:
            tkMessageBox.showinfo( "Error", "Please select value!")
    B.config(state=NORMAL)
    stop_b.config(state=DISABLED)

def force_stop():
    active_stat.set(False)

def score(digit ,t_sec):
    '''
    Base score system
    '''
    try:
        std_score = {100:0.05, 500:0.15, 1000:0.3, 2000:0.7, 5000:4.4,10000:25, 20000:154, 50000:2043}
        return (std_score[digit]/t_sec)*8000
    except:
        return '[N/A]'

def export():
    try:
        global E, TIMER_NUM
        if tkMessageBox.askyesno( "Export?", "Do you really want to export result file?\n (Will replace old file!)"):
            if SCORE.get() == '-':
                tkMessageBox.showerror( "Error", "You have been force stop it! Start benchmark again to proceed this.")
            else:
                f = open("ePy_output.txt", "w")
                f.write("ePy had burned your computer for %s sec. \n" % TIMER_NUM)
                f.write("And your score is %s. \n" % SCORE.get())
                f.write("Here is your computer's value of e ("+str(len(str(E))-2)+" digits):\n")
                for i in xrange(len(str(E))):
                    if i % 80 == 0:
                        f.write("\n")
                    f.write("%s" % (str(E)[i]))
                f.close()
                tkMessageBox.showinfo( "Operation Complete", "Exported file (ePy_output.txt) is in same folder of this program.")
    except:
        tkMessageBox.showerror( "Error", "You haven't started it yet.")

if __name__ == "__main__":
    root = Tk()
    root.title("ePy Bench")
    root.resizable(width=FALSE, height=FALSE)

    #Global_Var#
    PROGRESSED = 0
    TIMER = StringVar()
    TIMER.set("[N/A] sec.")
    SCORE = StringVar()
    SCORE.set("[N/A]P")
    E = 0
    #/Global_Var#

    #GUI#
    active_stat = BooleanVar(root)
    active_stat.set(True)

    cores = IntVar()
    c = Checkbutton(root, text="Multicore processing", variable=cores)
    c.grid(row=1, columnspan=2)

    cores_l = Label(root, text="Number of digits:")
    cores_l.grid(row=0, column=0)

    digit_select_box = Spinbox(root, values=(100,500,1000,2000,5000,10000,20000,50000), width=8)
    digit_select_box.grid(row=0, column=1)

    B = Button(root, text ="      Start      ", command = p)
    B.grid(row=2, column=0)

    stop_b = Button(root, text ='  Force Stop  ', command=force_stop)
    stop_b.config(state=DISABLED)
    stop_b.grid(row=2, column=1, sticky='W')

    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, maximum=1.0, mode="determinate", variable=PROGRESSED)
    progressbar.grid(row=5, columnspan=2)
    
    b_score = Label(root, textvariable=SCORE)
    b_score.config(font=('',20,'bold'))
    b_score.config(fg='red')
    b_score.grid(row=3, columnspan=2)
    
    stat = Label(root, textvariable=TIMER)
    stat.grid(row=4, columnspan=2)
    
    #MENUBAR#
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Export current test result", command=export)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="About", command=ab.about_pop)
    filemenu.add_command(label="Help", command=ab.help_pop)
    menubar.add_cascade(label="Help", menu=filemenu)
    
    root.config(menu=menubar)
    #/MENUBAR
    
    root.mainloop()
    #/GUI#
    exit()
