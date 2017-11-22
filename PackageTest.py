def checkMod():
        print('Checking packages...')
        import platform
        import os
        from imp import find_module
        import pip

        def darwinInstall():
                print(oscheck)
                while True:
                    try:
                        checkpafy = find_module('pafy')
                    except ImportError:
                        print('Essential package missing: pafy')
                        installoption = input('Would you like to install the required package? (y/N) ')
                        if installoption == 'y':
                                pafyinstallcmd = 'sudo -H pip install pafy'
                                os.system(pafyinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkyoutubedl = find_module('youtube_dl')
                    except ImportError:
                        print('Essential package missing: youtube-dl')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            youtubedlinstallcmd = 'sudo -H pip install youtube_dl'
                            os.system(youtubedlinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkbillboard = find_module('Billboard')
                    except ImportError:
                        print('Essential package missing: Billboard')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            billboardinstallcmd = 'sudo -H pip install billboard.py'
                            os.system(billboardinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkvlc = find_module('vlc')
                    except ImportError:
                        print('Essential package missing: python-vlc')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            vlcinstallcmd = 'sudo -H pip install python-vlc'
                            os.system(vlcinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    print("You're all set!")
                    return()

        def windowsInstall():
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
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkyoutubedl = find_module('youtube_dl')
                    except ImportError:
                        print('Essential package missing: youtube-dl')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            youtubedlinstallcmd = 'pip install youtube_dl'
                            os.system(youtubedlinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkbillboard = find_module('Billboard')
                    except ImportError:
                        print('Essential package missing: Billboard')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            billboardinstallcmd = 'pip install billboard.py'
                            os.system(billboardinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    try:
                        checkvlc = find_module('vlc')
                    except ImportError:
                        print('Essential package missing: python-vlc')
                        installoption = input('Would you like to install the required packages? (y/N) ')
                        if installoption == 'y':
                            vlcinstallcmd = 'pip install python-vlc'
                            os.system(vlcinstallcmd)
                        else:
                            choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                            if choice2 == 'y':
                                print("Okay Goodbye :) ")
                                exit()
                            else:
                                checkMod()
                    print("You're all set!")
                    return()
                


        oscheck = platform.system()

        if 'Darwin' in oscheck:
                darwinInstall()
                return()

        if 'Windows' in oscheck:
                windowsInstall()
                return()

        if 'Linux' in oscheck:
                darwinInstall()
                return()

                
                

checkMod()
