def musicPlayer():

    import os
    from os.path import join
    import vlc
    import time

    lookfor= input("Search for... ")
    search = lookfor + str('.mp3')
    print("searching...")
    for root, dirs, files in os.walk('/Users'):
        root
        if search in files:
            if True:
                file = join(root, search)
                print(file)
                choicePlay = input("Would you like to play this file? (Y/n) ")
                if choicePlay == 'Y':
                    song = vlc.MediaPlayer(file)
                    song.play()
                if choicePlay == 'n':
                    exit()
                    user_stop = input("Type STOP to stop playing... ")
                    if user_stop == "STOP":
                        song.stop()
                        exit()
            else:
                print("Sorry I couldn't find the file :(")
                break
musicPlayer()
