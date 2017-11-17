def manualcreatePlaylist(message):
    '''Takes the users message as a str and adds in to a list'''
    print("You humans are strange. Why do you need to listen to Music?\n ERROR! BOT RESETTING!\n"+(".")*10+"\n Sorry about that. Feel free to start adding songs")
    while True:
        if message == "done":
            print("Are you happy with the songs?  Y/N")
            print(playlist)
            if message == "Y":
                break
            if message == "N":
                print("Your playlist has been reset. Please input your songs")
                playlist.clear()
                continue
        else:
            print("Song Name: ")
            playlist = []
            playlist.append(message)

    print("You can now add a name for the playlist: ")
    playlist.insert(0, message)
    f = open("playlists.txt", "a")
    f.write("\n"+playlist)
    f.close