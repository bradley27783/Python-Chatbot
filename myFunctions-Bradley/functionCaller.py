def functionCaller(message):
  '''This function takes the users input as a string, and calls the appropriate function'''
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
                return 6    #This is for the playlistcreator
              
        if i in range(0,22):
          from cursewordDetector import curseCounter         #The curseCounter function is my function 
          msg = curseCounter(l[i])
          return msg   #This is the curseCounter
        if i in range(22,28):
          from checkforGreeting import check_for_greeting    #The checkforGreeting function is not my function it is Adrian Hasiks. I am only importing it
          msg = check_for_greeting(l[i])
          return msg   #This is the check_for_greetings

        if i in range(28,35):
          from checkforGoodbye import check_for_goodbye      #The checkforGoodbye function is not my function it is Adrian Hasiks. I am only importing it
          msg = check_for_goodbye(l[i])
          return msg   #This is the check_for_goodbye

        if i in range(35,36):
          for artist in message:
            a+=1
            if artist in message:
              #from facts2 import facts             #The facts function is not my function it is Kyle Gillets. I am only importing it
              msg = "Facts currently is unavailable"
              return msg   #This checks for the word Fact or Facts
            ##The fact funtion is too hard to implement and will take a while to implement so it's being left out
            else:
              return "Sorry we either don't have that artist in our database or you didn't input one\nPlease try again"
        if i in range(36,38):
          return "This is too hard to implement"     #This checks for anything to do with youtube and runs the function to play music
#I am not importing it here but the YouTube search function is Harjan Gahir's
        if i in range(38,40):
          return "Playlists are currently unavailable"    #This is to play a playlist
        
        
        
        
  else:  #This else statment is used just incase we can't find a keyword
    return "What you have inputted wasn't found in my database\nTry typing 'help' for assistance"
       #help function has not been created due to lack of time           
  return msg