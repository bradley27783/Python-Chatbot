#Whatever the user enters is stored in a variable called 'name'.
name = input("What's your name?")

print("Hello" + name + "!")
print(name[0].upper()+name[1:].lower())

#This is the Greetings function
greetings_keywords = ["Hi", "Hello", "Hi there", "Hello there"]
greetings_responses = ["Hey", "How are you doing?", "What mood are you in?", "What music you want to listen to?"]
def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in greetings_keywords:
            return random.choice(greetings_responses)
        else:
            return("I did not understand what you said")
        
#This is Goodbeye respond function
end_keywords=["end", "I have to go", "close"]
goodbeye_keywords=["Goodbeye!", "See you later!", "Come back soon!"]
def check_for_goodbye
    for word in sentence.words:
        if word.lowe() in end_keywords:
            return random.choice(goodbeye_keywords)

#this function will ask the user what music he wants to listen to and will navigate him to the latest playlists e.g
x = input("What type of music you listen to?")
music_type_keywords = ["pop", "hip-hop", "Top"]
if any(keyword in x for keyword in music_type_keywords):
    print("I can play the Top")
   

 #If the user is french it will play top French tracks playlist.
Language/Nationality = {"english", "french", "german",}
    
def check_for_Nationality(sentence):
    for word in sentence.words:
        if word.lower() in Language/Nationality:
            
        else: 
        return random.choice(Random music)
            print(random.choice)      

    
def emotion(message):
  #Takes the user's message and outputs a response
  emotions = ["afraid","angry","sad","disgusted","happy","surprised","eager","okay","good","fine"]
  i = -1
  sentMsg=""
  for word in emotions:
   i = + 1
  if i <4:
      if word in message:
        if "?" in message:
            sentMsg="No, I'm actually quite fine, thank you :)"
        else:
            sentMsg="I am sorry you are " + str(emotions[i]) +" :("
  elif i>=4:
    if word in message:
    if "?" in message:
        sentMsg="Yeah, sure am!"
    else:
        sentMsg="Glad you're feeling " + str(emotions[i]) +"!"
    if sentMsg=="":
        sentMsg="Sorry, we haven't coded that in yet. :/"
        v=1
    
    return(sentMsg) 