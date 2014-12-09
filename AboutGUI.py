"""About_GUI"""
from Tkinter import *
import tkMessageBox
"""Use for show detail of program and  the name of producers"""
tkMessageBox.showinfo("This is the name of producers and detail of this program",
                      "Mr.Tanakrit Tangdamrongsap 57070044 \n"
                      "Mr.Sakan Promlainak 57070110 \n\n"
                      "This program is benchmark.\n"
                      "Use for speed test of your computer by test with runtime of e value. \n\n"
                      "How to use \n\n"
                      "1.Select the number of digit of e value. \n"
                      "2.Select multicore processing if you want. \n"
                      "3.Press 'Start' button. \n"
                      "4.If process is too long you can press 'Force Stop' to stop the process. \n"
                      "5.Check your computer speed.")
root = Tk()
root.mainloop()
