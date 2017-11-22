def functionCaller(message):
  l = ["asshole","arsehole","bitch","pissed","shit","son of a bitch","bastard","bellend","cock","dick","dickhead","knob","prick","pussy","twat","cunt","fuck","motherfucker","fuckoff","fuck off","fuckyou","fuck you","hello","hi","goodmorning","goodafternoon","goodevening","hey","i have to go","close","i am out","farewell","see you later","see ya later","peace","fact","youtube","search","playlist"]
  creator = ["create","creator"]
  i = -1
  c = -1
  message = message.lower()
  for word in l:
    i+=1
    if word in message:
      if i in range(0,22):
        return 1   #This is the curseCounter
      if i in range(22,28):
        return 2   #This is the check_for_greetings
        
      if i in range(28,35):
        return 3   #This is the check_for_goodbye
        
      if i in range(35,36):
        return 4   #This checks for the word Fact or Facts
      
      if i in range(36,38):
        return 5     #This checks for anything to do with youtube and runs the function to play music
      
      if i in range(38,40):   #Finds the values 'playlist/s'
        for createword in creator:
          c+=1
          if createword in message:     #Finds for additional words in the sentence, this is needed cause teh word 'playlist/s' is conflicting
            if c in range(0,2):
              return 6    #This is for the playlistcreator
        else:
          return 7    #This is to play a playlist
        
        
        
        
  else:
    return "What you have inputted wasn't found in my database\nTry typing 'help' for assistance"
                  
print(functionCaller("PLaYlisT"))