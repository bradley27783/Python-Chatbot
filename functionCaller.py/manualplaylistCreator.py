def createPlaylist():
    '''Takes the users message as a str and adds in to a list'''
playlist = []
print("You humans are strange. Why do you need to listen to Music?\n ERROR! BOT RESETTING!\n"+(".")*10+"\n Sorry about that feel free to start adding songs")
userInput = ""
while True:
    if userInput == "done": 
        print(playlist)
        userInput = input("Are you happy with the songs?  Y/N: ")
        if userInput == "Y":
            break
        if userInput == "N":
            print("Your playlist has been reset. Please input your songs")
            playlist.clear()
            continue
        else:
            print("I am only a simple bot and I don't understand what you have inputted.\n Returning you to the add songs section")
    else:
        userInput = input("Song Name: ")
        if userInput != "done":
            playlist.append(userInput)


   
nameplaylist = input("You can now add a name for the playlist: ")
playlist.insert(0, nameplaylist)
print(playlist)
f = open("manualplaylists.txt", "a")
doc=" ".join(playlist)
print(doc)
f.write("\n"+doc)
f.close

createPlaylist()