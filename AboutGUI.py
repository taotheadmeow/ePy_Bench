"""
About ePy GUI
This is prototype file of About
"""
from Tkinter import *
import tkMessageBox
##"""Use for show detail of program and  the name of producers"""
def about_pop():
    tkMessageBox.showinfo("About ePy Bench",
                          "Developed by \n"
                          "Mr.Tanakrit Tangdamrongsap 57070044 \n"
                          "Mr.Sakan Promlainak 57070110 \n\n"
                          "This program is for benchmarking and performance testing.\n"
                          "Use for testing speed of your computer by test with runtime of e value. \n\n"
                          "If you found bug... sent report to s7070110@kmitl.ac.th."
                          )

def help_pop():
    tkMessageBox.showinfo("Help",
                          "How to use \n"
                          "1. Select the number of digit of e value. \n"
                          "2. Select multicore processing if you want. \n"
                          "3. Press 'Start' button. \n"
                          "4. Wait for result. \n"
                          "5. Check your computer speed.\n\n"
                          "ps. If process is too long you can press 'Force Stop' to stop the process."
                          )

if __name__ == '__main__':
    root = Tk()
    about_pop()
    help_pop()
    root.mainloop()
    
    
