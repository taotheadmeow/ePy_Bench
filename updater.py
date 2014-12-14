import urllib2
from subprocess import call
import os
import tkMessageBox
def chk_update():
    print 'Checking...'
    while True:
        try:
            response = urllib2.urlopen('https://raw.githubusercontent.com/taotheadmin/ePy_Bench/master/ePy_GUI.py')
            web = response.read()
            file = open('ePy_GUI.py', 'r')
            if web == file.read():
                print 'Your copy is up-to-date.'
                file.close()
            else:
                file.close()
                if tkMessageBox.askyesno("Update?", "Your copy is not up-to-date or modified. Do you want to update or/and synchonize?"):
                    print 'Updating...'
                    file = open('ePy_GUI.py', 'w')
                    file.write(str(web))
                    file.close()
            break
        except:
            yesno = raw_input("Something error!?\nPlease check your internet connection and try again. Try again now? (Y/N)")
            if yesno in ['Y', 'y', 'Yes', 'yes', 'YES']:
                pass
            else:
                break
chk_update()
try:
    os.system("ePy_GUI.py")
except:
    os.system("ePy_GUI.exe")

