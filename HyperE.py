'''
ePy Bench: Multicore Edition
Just a stupid CPU benchmark.

This Program will calculate value of "e".
Developed by Sakan Promlainak.
Thanks to Stackoverflow for basic algorithm.

Ver. Alpha
GO faster with Multicore Processing

Last Updated:
10 Nov. 2014
5:36 PM
'''
from decimal import *
import math
import time
import sys
import multiprocessing
from multiprocessing.dummy import Pool

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
        fact = p.map(math.factorial, range(i, i+cores))
        e += sum(p.map(one_div, fact))
        i += cores
        c += 1
        if c % 1 == 0:
            sys.stdout.write("\r%i loops passed." % (c) )
            sys.stdout.flush()
            #print i, "loops passed."
        if e == temp:
            break
        temp = e
    sys.stdout.write("\r%i loops passed.\n" % (c) )
    p.close()
    p.join()

    return e

## OLD CODE IGNORE IT.
##def burner(digit):
##    global ALL_TIME, E
##    start_time = time.time()
##    e_con = e_cal(digit)
##    timer = str(time.time() - start_time)
##    ALL_TIME.append(timer)
##    E = str(e_con)


def main():
    '''main'''
    digit = input('Enter the digits. >>> ')+1
    print 'Burning your CPU... (Calculating', digit-1, 'digits of e...)'
    
##  Start burn.
    start_time = time.time()
    e_con = e_cal(digit, multiprocessing.cpu_count())
    timer = str(time.time() - start_time)
##  End of burning.
    
    print ("Your PC uses %s seconds for calculate" % timer), digit-1, "digits of e."
    print ("You can see value of e in ePy_output.txt. "\
           +"It's in same folder of this program.")
    
##  File Export
    f = open("ePy_output.txt", "w")
    f.write("ePy had burned your computer for %s sec. \n" % timer)
    f.write("Here is your computer's value of e ("+str(len(str(e_con))-2)+" digits):\n")
    f.write("%s" % str(e_con))
    f.close()
    end = raw_input("\nPress Enter to Exit")

main()

