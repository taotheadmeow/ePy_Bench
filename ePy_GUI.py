"""
Title: ePy Bench GUI

Version: InDev
Developed by Sakan Promlainak

"""
from Tkinter import *
import tkMessageBox
import ttk
import multiprocessing
import time
from multiprocessing.dummy import Pool
from decimal import *
import math
import sys

### ePy_MC Mod ###

def one_div(fact):
    return Decimal(1)/fact

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
    getcontext().prec = l
    e = Decimal(0)
    i = 0
    temp = 0
    temp_fact = 0
    c = 0
    prog_stat = 0
    while True:
        fact = p.map(math.factorial, range(i, i+cores)) #parallel process factorial
        e += sum(p.map(one_div, fact)) #processed factorial will total in here
        x = float((i-temp_fact))/end[l]
        prog_stat += x
        PROGRESSED = prog_stat
        progressbar.step(x)
        progressbar.grid(row=4, columnspan=2)
        root.update()
        temp_fact = i
        i += cores
        c += 1
##        sys.stdout.write("\r%i loops passed.\n" % (c) ) #Print Loop status
##        sys.stdout.flush()
        #print i, "loops passed."
        if e == temp:
            progressbar.step(-prog_stat)
            progressbar.grid(row=4, columnspan=2)
            root.update()
            break
        temp = e
##    sys.stdout.write("\r%i loops passed.\n" % (c) )
##    sys.stdout.flush()
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
    getcontext().prec = l
    e = Decimal(0)
    i = 0
    temp = 0
    temp_fact = 0
    c = 0
    prog_stat = 0
    while True:
        fact = math.factorial(i)
        e += Decimal(1)/fact
        x = float((i-temp_fact))/end[l]
        prog_stat += x
        PROGRESSED = prog_stat
        progressbar.step(x)
        progressbar.grid(row=4, columnspan=2)
        root.update()
        temp_fact = i
        i += 1
        c += 1
##        sys.stdout.write("\r%i loops passed.\n" % (c) ) #Print Loop status
##        sys.stdout.flush()
        #print i, "loops passed."
        if e == temp:
            progressbar.step(-prog_stat)
            progressbar.grid(row=4, columnspan=2)
            root.update()
            break
        temp = e
##    sys.stdout.write("\r%i loops passed.\n" % (c) )
##    sys.stdout.flush()

    return e

###  ###

def p():
    global E
    ran = False
    try:
        dig = int(digit_select_box.get())
        B.config(state=DISABLED)
        ran = True
        if dig not in [100,500,1000,2000,5000,10000,20000,50000]:
            tkMessageBox.showinfo( "Error", "Invalid digit number.")
            B.config(state=NORMAL)
            return None
        else:
            tkMessageBox.showinfo( "Warning", "Are you ready to calculate "+str(dig)+" digits of e?")
            t = time.time()
            if int(cores.get()) == 0:
                t = time.time()
                E = e_cal_sc(dig)
            else:
                t = time.time()
                E = e_cal(dig, multiprocessing.cpu_count())
            TIMER.set(str(time.time()-t)+" sec.")
            B.config(state=NORMAL)
    except:
        if ran:
            tkMessageBox.showinfo( "Error", "You had force stop or somthing else error.")
            progressbar.step(-PROGRESSED)
            progressbar.grid(row=4, columnspan=2)
            root.update()
        else:
            tkMessageBox.showinfo( "Error", "Please select value!")
        B.config(state=NORMAL)
            
if __name__ == "__main__":
    root = Tk()
    PROGRESSED = 0
    TIMER = StringVar()
    TIMER.set("N/A")
    E = 0
    root.title("ePy bench")

    cores = IntVar()
    c = Checkbutton(root, text="Multicore processing", variable=cores)
    c.grid(row=1, columnspan=2)

    cores_l = Label(root, text="Number of digits:")
    cores_l.grid(row=0, column=0, sticky="W")

    digit_select_box = Spinbox(root, values=(100,500,1000,2000,5000,10000,20000,50000), width=8)
    digit_select_box.grid(row=0, column=1, sticky="E")

    ##Lb1 = Listbox(root)
    ##Lb1.insert(1, "100")
    ##Lb1.insert(2, "500")
    ##Lb1.insert(3, "1000")
    ##Lb1.insert(4, "2000")
    ##Lb1.insert(5, "5000")
    ##Lb1.insert(6, "10000")
    ##Lb1.insert(7, "20000")
    ##Lb1.insert(8, "50000")
    ##Lb1.grid(row=1, column=0)

    B = Button(root, text ="Start", command = p)
    B.grid(row=2, columnspan=2)


    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, maximum=1.0, mode="determinate", variable=PROGRESSED)
    progressbar.grid(row=4, columnspan=2)


    stat = Label(root, textvariable=TIMER)
    stat.grid(row=3, columnspan=2)

    root.mainloop()
    exit()
