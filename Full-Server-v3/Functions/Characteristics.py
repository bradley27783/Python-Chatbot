#Whatever the user enters is stored in a variable called 'name'.
name = input("What's your name?")
print("Hello " + name[0].upper()+name[1:].lower() + "!")

#This is the Greetings function
def check_for_greeting(sentence):
    #If any of the words in the user's input was a greeting, return a greeting response
    greetings_keywords = ["Hi", "Hello", "Hi there", "Hello there"]
    greetings_responses = ["Hey", "How are you doing?", "What mood are you in?", "What music you want to listen to?"]
    for word in sentence.words:
        if word.lower() in greetings_keywords:
            return random.choice(greetings_responses)
        else:
            return("I did not understand what you said")
        
#This is Goodbeye respond function
def check_for_goodbeye(sentence):
    end_keywords=["end", "I have to go", "close"]
    goodbeye_keywords=["Goodbeye!", "See you later!", "Come back soon!"]
    for word in sentence.words:
        if word.lower() in end_keywords:
            return random.choice(goodbeye_keywords)