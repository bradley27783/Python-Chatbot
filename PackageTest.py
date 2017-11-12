def checkMod():
        print('Checking packages...')
        from imp import find_module
        import pip
        while True:
            try:
                checkpafy = find_module('pafy')
            except ImportError:
                print('Essential package missing: pafy')
                installoption = input('Would you like to install the required package? (y/N) ')
                if installoption == 'y':
                    pip.main(['install', 'pafy'])
                else:
                    choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                    if choice2 == 'y':
                        print("Okay Goodbye :) ")
                        exit()
                    else:
                        checkMod()
            try:
                checkyoutubedl = find_module('youtube-dl')
            except ImportError:
                print('Essential package missing: youtube-dl')
                installoption = input('Would you like to install the required packages? (y/N) ')
                if installoption == 'y':
                    pip.main(['install', 'youtube-dl'])
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
                    pip.main(['install', 'Billboard'])
                else:
                    choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                    if choice2 == 'y':
                        print("Okay Goodbye :) ")
                        exit()
                    else:
                        checkMod()
            try:
                checkvlc = find_module('python-vlc')
            except ImportError:
                print('Essential package missing: python-vlc')
                installoption = input('Would you like to install the required packages? (y/N) ')
                if installoption == 'y':
                    pip.main(['install', 'python-vlc'])
                else:
                    choice2 = input("This package is required for the program to run are you sure you would like to quit? (y/N) ")
                    if choice2 == 'y':
                        print("Okay Goodbye :) ")
                        exit()
                    else:
                        checkMod()
            print("You're all set!")
            return()
                
                

checkMod()
