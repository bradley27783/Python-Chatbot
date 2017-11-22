def createPlaylist():
    '''Takes the users message as a str and adds in to a list'''
playlist = []
print("You humans are strange. Why do you need to listen to Music?\n ERROR! BOT RESETTING!\n"+(".")*10+"\n Sorry about that feel free to start adding songs")
#Since the chatbot has the characteristics of a robot I added this line.
userInput = ""
while True:
    if userInput == "done": #When the user inputs 'done' it asks them if they are happy with the songs.
        print(playlist)
        userInput = input("Are you happy with the songs?  Y/N: ")
        if userInput == "Y":    #If they say yes then we can break the loop
            break
        if userInput == "N":    #If they say no then we reset their playlist and return the addition of songs
            print("Your playlist has been reset. Please input your songs")
            playlist.clear()
            continue
        else:
            print("I am only a simple bot and I don't understand what you have inputted.\n Returning you to the add songs section")
            #This is here just in case the user doesn't listen to the commands and will return the user to adding songs.
    else:
        userInput = input("Song Name: ")
        if userInput != "done":
            playlist.append(userInput)


   
nameplaylist = input("You can now add a name for the playlist: ")
playlist.insert(0, nameplaylist)         #This section of code is to store the playlist in a txt file and with the playlist title being at the start. This is so it can be extracted into a dict
print(playlist)
f = open("manualplaylists.txt", "a") 
doc=" ".join(playlist)
print(doc)
f.write("\n"+doc)     #Each playlist is saved on a newline
f.close

createPlaylist()