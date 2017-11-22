def functionCaller(message):
  l = ["asshole","arsehole","bitch","pissed","shit","son of a bitch","bastard","bellend","cock","dick","dickhead","knob","prick","pussy","twat","cunt","fuck","motherfucker","fuckoff","fuck off","fuckyou","fuck you","hello","hi","goodmorning","goodafternoon","goodevening","hey","i have to go","close","i am out","farewell","see you later","see ya later","peace","fact","youtube","search","playlist"]
  creator = ["create","creator"]
  artists = ['kanye west',"the beetles","rick astley","ed sheeran","taylor swift","eminem",'slim shady',"michael jackson","ellie goulding"]
  i = -1    #Iteration count 'i' is for the list l
  c = -1    #Iteration count 'c' is for the list creator
  a = -1    #Iteration count 'i' is for the list artists
  message = message.lower()
  for word in l:  #This for loop goes through the list 'l' and counts i + 1 for each iteration until it finds the word
    i+=1
    if word in message:
        for createword in creator:    #This for loop iterates through the list 'creator', counting c + 1 for each iteration until it finds the word.
          c+=1
          if createword in message:
             if i in range(38,40) and c in range(0,2):   #Finds the values 'playlist/s' and 'create/creator'
                return "This would run the playlist creator"    #This is for the playlistcreator
              
        if i in range(0,22):
          return "This would run the curseCounter"     #This is the curseCounter
        
        if i in range(22,28):
          from checkforGreeting import check_for_greeting  #This is the check_for_greetings
          return "This would run the greetings function"  

        if i in range(28,35):
          return "This would run the greetings function"      #This is the check_for_goodbye

        if i in range(35,36):
          for artist in message:
            a+=1
            if artist in message:
              return "This would run the Facts function"   #This checks for the word Fact or Facts

            else:
              return "Sorry we either don't have that artist in our database or you didn't input one\nPlease try again"
            
        if i in range(36,38):
          return "This would run the YouTube function"     #This checks for anything to do with youtube and runs the function to play music
        
        if i in range(38,40):
          return "This would run the playlist function"    #This is to play a playlist
        
        
        
        
  else:  #This else statment is used just incase we can't find a keyword
    return "What you have inputted wasn't found in my database\nTry typing 'help' for assistance"
       #help function has not been created due to lack of time           
