def musicPlayer():
    
    print("Loading")
    import os
    from os.path import join
    import vlc
    import time
    print("Done...")
    
    lookfor = input("Search for... ")
    print("searching...")
    while True:
        path = os.path.dirname(os.path.realpath(__file__))
        for f_name in os.listdir(path):
            if f_name.startswith(lookfor) and f_name.endswith('.mp3'):
                filename = join(path, f_name)
                print(filename)
                choicePlay = input("Would you like to play this file? (Y/n) ")
                if choicePlay == 'Y':
                    song = vlc.MediaPlayer(filename)
                    song.play()
                    song.get_instance()
                    while True:
                        playercommand = input("Type STOP to stop playing... ")
                        if playercommand == "STOP":
                            song.stop()
                            musicPlayer()
                        else:
                            print("")
                        
                if choicePlay == 'n':
                    musicPlayer()
musicPlayer()
