#Library consists of keys and values. All the help keywords for the clients.
chatbot_help_dict = {"playlist":"Type in Playlist Main, to search for a Playlist",
                     "album":"To go into album go into your library first, and then choose an artist album",
                     "fact":"For chatbot to display fact type artist name and fact e.g 'drake fact'",
                     "exit": "To close the chatbot type close",
                     "interact": "To interact with the chatbot type any sentences",
                     "username":"create a unique username when the chatbot asks you to",
                     "password":"create a memorable password for your account",
                     "Y/N":"Y stands for yes and N stands for No if the chatbot asks you replay with Y or N"
                    }        
#Help Function which displays the key values
def check_for_help(help_word):
    if "playlist" in help_word.lower():                 #changes the user input to lower case letters.
        return(chatbot_help_dict.get("playlist"))       #Gives the value of specified key.
    if "album" in help_word.lower():                    #changes the user input to lower case letters.
        return(chatbot_help_dict.get("album"))          #Gives the value of specified key.
    if "fact" in help_word.lower():                     #changes the user input to lower case letters.
        return(chatbot_help_dict.get("fact"))           #Gives the value of specified key.    
    if "exit" in help_word.lower():                     #changes the user input to lower case letters.
        return(chatbot_help_dict.get("exit"))           #Gives the value of specified key.    
    if "interact" in help_word.lower():                 #changes the user input to lower case letters.
        return(chatbot_help_dict.get("interact"))       #Gives the value of specified key.    
    if "username" in help_word.lower():                 #changes the user input to lower case letters.
        return(chatbot_help_dict.get("password"))       #Gives the value of specified key.    
    if "Y/N" in help_word.lower():                      #changes the user input to lower case letters.
        return(chatbot_help_dict.get("Y/N"))            #Gives the value of specified key.                
    if "help_full" in help_word.lower():
        return chatbot_help_dict.items()   
    
    return("Enter a Key word or 'help_full' for the list of all inputs") #prints a message if word not found in the dictionary.

print (check_for_help("playlist")) #This is a test code which cannot be implemented in the final chatbot.