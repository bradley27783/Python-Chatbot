unavailable#This function a greetings function, this will display a greeting with the users name, the greeting will change depending on the current time.
def check_for_greeting(sentence):
    import datetime #Gets access to the datetime module.
    currentTime = datetime.datetime.now() #This displays the greeting depending on the time and the users name.
    currentTime.hour #current time in hour.
    0
    #if currentTime.hour < 12:
        # print("Good Morning " + user_name + "!")   #If the time is before 12am the chatbot will print a "Good morning" message to the user with his username.
   # elif 12 <= currentTime.hour < 18:
        # print("Good Afternoon " + user_name + "!") #If the time is before 18pm the chatbot will print a "Good Afternoon" message to the user with his username.
   # else:
        # print("Good Evening " + user_name + "!")   #For any other time the chatbot will print a "Good Evening" message to the user with his username.

    #If any of the words in the user's input was a greeting, return a greeting response.
    import random #Gets access to the random module.
    greetings_keywords = ["hi","hi","hello","hi there","hello there","greetings",] #User Input to the Chatbot.
    greetings_response = ["Hey", "How are you doing?", "What mood are you in?", "What music you want to listen to?"] #The chatbot Output .
    i = "!" or "'" or "." or "," #This will check any punctuation that the user might enter in his sentence.
    for i in sentence.lower(): #This is a loop that checks for i.
        for word in greetings_keywords: #If the word that user entered is in the list.
            if word in sentence.lower(): #Then converts users input to all lower case letters.
                return random.choice(greetings_response) #chatbot returns a message depending on what the user has entered.
    return("I did not understand what you said") #If the chatbot does not recognise the message thent it returns with a message.

#print(check_for_greeting("Greetings!", "Tom")) #This is a test code which cannot be implemented in the final chatbot.

#This is users mood/emotion function, it will look for the keywords that the user will enter and search for them in the list then give a reply
def feelings_option(sentence):
    import random
    feeling_keyword = ["fine", "","i want to listen to music", "not bad","ok","exhausted", "bored", "tired", "anything"]
    option_keyword = ["I can play any music you would like", "Do you want me to play Top tracks of the month?", "Type in any playlist or artist?"]
    i = "!" or "'"
    for i in sentence.lower():
        for word in feeling_keyword:
            if word in sentence.lower():
                return random.choice(option_keyword)
        
    return ("I didn't understand what you said")

print(feelings_option("I am fine")) #This is a test code which cannot be implemented in the final chatbot.

#This is the artist function, Searches for any artists that the user has mentioned. Then replys with a message.
def play_artist(sentence):
    import random
    artist = ["drake", "eminem","beatles", "bruno mars","justin timberlake", "rihanna", "pitbull", "avicii","john newman",]
    response = ["Have Fun!", "The music has been successfully added to your playlist Library"]
    i = "!" or "'"
    for i in sentence.lower():
        for word in artist:
            if word in sentence.lower():
                return random.choice(response)
            
    return ("Which artist playlist do you want me to play?") 

print(play_artist("Play Drake!!!")) #This is a test code which cannot be implemented in the final chatbot.

#This is a genre function, which checks for any type of music that user would like to listen to. After user input it returns a message.
def play_genre(sentence):
    import random
    genre = ["pop", "hip hop","beatles", "party","rock","classic", "electronic", "workout", "workout","decades","80","90","70","country","focus","holliday"]
    response = ["Have Fun!", "The music has been successfully added to your playlist Library"]
    i = "!" or "'" or "-"
    for i in sentence.lower():
        for word in genre:
            if word in sentence.lower():
                return random.choice(response)            
       
    return ("I didn't understand what you said")

print(play_genre("pop")) #This is a test code which cannot be implemented in the final chatbot.

#This is Goodbeye respond function, it will check whether the user has said he wants to exit the chatbot, if so the chat bot will reply with a goodbye.
def check_for_goodbye(sentence): 
    import random
    end_keyword = ["i have to go", "close","i am out", "farewell","see you later","peace", "see ya later", "c u later", "bye","later"]
    goodbye_keyword = ["Goodbeye!", "See you later!", "Come back soon!","Have a good day!", "Take Care", "Bye!","OK, have a good day!"]
    i = "!" or "'" or "." or ","
    for i in sentence.lower():
        for word in end_keyword:
            if word in sentence.lower():
                return random.choice(goodbye_keyword)
 
    return ("I didn't understand what you said")

print(check_for_goodbye("I had enough of you close")) #This is a test code which cannot be implemented in the final chatbot.