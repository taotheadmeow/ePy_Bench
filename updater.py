import urllib2
print 'Checking...'
while True:
    try:
        response = urllib2.urlopen('https://raw.githubusercontent.com/taotheadmin/ePy_Bench/master/ePy_GUI.py')
        web = response.read()
        file = open('ePy_GUI.py', 'r')
        if web == file.read():
            print 'Up to date'
            file.close()
        else:
            file.close()
            yesno = raw_input("Your copy is not up-to-date or modified. Do you want to update or/and synchonize? (Y/N)")
            if yesno in ['Y', 'y', 'Yes', 'yes', 'YES']:
                print 'Updating'
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
        
raw_input('Press enter to exit.')
