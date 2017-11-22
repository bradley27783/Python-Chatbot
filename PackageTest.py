def checkMod():        #This fuction will download and install the required packages for the certain features of the chatbot to work
        print('Checking packages...')
        import platform
        import os
        from imp import find_module
        import pip
        
        oscheck = platform.system()  #Checks the operating system of your computer
        if 'Darwin' in oscheck:
                darwinInstall()   #Runs the darwinInstall function
                return()
        if 'Windows' in oscheck:
                windowsInstall()  #Runs the windowsInstall function
                return()
        if 'Linux' in oscheck:
                darwinInstall()   #Runs the darwinInstall function
                return()
        
        def darwinInstall():   #Only runs if the OS of the computer is macOS or Linux
                print(oscheck)
                while True:
                    try:
                        checkpafy = find_module('pafy')   #Checks if the module named is installed
                    except ImportError:
                        print('Essential package missing: pafy')  #If the module is not found the runs the if statement
                        installoption = input('Would you like to install the required package? (y/N) ') #Asks the user to install or not
                        if installoption == 'y':
                                pafyinstallcmd = 'sudo -H pip install pafy'  #Installs the package using sudo pip
                                os.system(pafyinstallcmd) #Runs the command
                        elif installoption == 'N':  #Reacts to if the user types N and makes sure they want to quit
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':  #Calls the darwinInstall fuction again
                                darwinInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkyoutubedl = find_module('youtube_dl')
                    except ImportError:
                        print('Essential package missing: youtube-dl')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            youtubedlinstallcmd = 'sudo -H pip install youtube_dl'
                            os.system(youtubedlinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                darwinInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkbillboard = find_module('Billboard')
                    except ImportError:
                        print('Essential package missing: Billboard')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            billboardinstallcmd = 'sudo -H pip install billboard.py'
                            os.system(billboardinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                darwinInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkvlc = find_module('vlc')
                    except ImportError:
                        print('Essential package missing: python-vlc')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            vlcinstallcmd = 'sudo -H pip install python-vlc'
                            os.system(vlcinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                darwinInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    print("You're all set!")
                    return()

        def windowsInstall():   #Only runs the function if the operating system is detected as windows
                 print(oscheck)
                 while True:
                    try:
                        checkpafy = find_module('pafy')
                    except ImportError:
                        print('Essential package missing: pafy')
                        installoption = input('Would you like to install the required package? (y/N) ')
                        if installoption == 'y':
                                pafyinstallcmd = 'pip install pafy'
                                os.system(pafyinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                windowsInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkyoutubedl = find_module('youtube_dl')
                    except ImportError:
                        print('Essential package missing: youtube-dl')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            youtubedlinstallcmd = 'pip install youtube_dl'
                            os.system(youtubedlinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                windowsInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkbillboard = find_module('Billboard')
                    except ImportError:
                        print('Essential package missing: Billboard')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            billboardinstallcmd = 'pip install billboard.py'
                            os.system(billboardinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                windowsInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    try:
                        checkvlc = find_module('vlc')
                    except ImportError:
                        print('Essential package missing: python-vlc')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            vlcinstallcmd = 'pip install python-vlc'
                            os.system(vlcinstallcmd)
                        elif installoption == 'N':
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            elif choice2 == 'N':
                                windowsInstall()
                            else:
                                print("Sorry that was not an option, try again")
                        else:
                            print("Sorry that was not an option, try again")
                    else:
                        print("Sorry that was not an option, try again")
                    print("You're all set!")
                    return()
checkMod()
