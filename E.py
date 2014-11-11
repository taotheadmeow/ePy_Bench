'''
ePy Benchmark.
Just a stupid CPU benchmark.

This Program will calculate value of "e".
Developed by Sakan Promlainak.
Thanks to Stackoverflow for basic algorithm.

Ver. Alpha

Last Updated:
10 Nov. 2014
12:07 AM
'''
from decimal import *
import math
import time
import sys
##from threading import Thread

##ALL_TIME = []
##E = ''

def e_cal(l):
    '''
    e calculator
    this function will recive digits of float
    and calculate and print status during working.
    
    This function will return value of e.
    '''
    getcontext().prec = l
    e = Decimal(0)
    i = 0
    temp = 0
    while True:
        fact = math.factorial(i)
        e += Decimal(1)/fact
        i += 1
        if i % 10 == 0:
            sys.stdout.write("\r%i loops passed." % (i) )
            sys.stdout.flush()
            #print i, "loops passed."
        if e == temp:
            break
        temp = e
    sys.stdout.write("\r%i loops passed.\n" % (i) )

    return e

##def burner(digit):
##    global ALL_TIME, E
##    start_time = time.time()
##    e_con = e_cal(digit)
##    timer = str(time.time() - start_time)
##    ALL_TIME.append(timer)
##    E = str(e_con)


def main():
    digit = input('Enter the digits. >>> ')
    print 'Burning your CPU... (Calculating', digit, 'digits of e...)'
##  Start burn.
    start_time = time.time()
    e_con = e_cal(digit)
    timer = str(time.time() - start_time)
##  End of burning.
    print ("Your PC uses %s seconds for calculate" % timer), digit, "digits of e."
    print ("You can see value of e in ePy_output.txt. "\
           +"It's in same folder of this program.")
    
##  File Export
    f = open("ePy_output.txt", "w")
    f.write("ePy had burned your computer for %s sec. \n" % timer)
    f.write("Here is your computer's value of e:\n")
    f.write("%s" % str(e_con))
    f.close()
    end = raw_input("\nPress Enter to Exit")



main()

