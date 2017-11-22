def check_for_greeting(sentence):
  import random
  greetings_keywords = ["hi","hi","hello","hi there","hello there","greetings",] #User Input to the Chatbot.
  greetings_response = ["Hey", "How are you doing?", "What mood are you in?", "What music you want to listen to?"] #The chatbot Output .
  i = "!" or "'" or "." or "," #This will check any punctuation that the user might enter in his sentence.
  for i in sentence.lower(): #This is a loop that checks for i.
      for word in greetings_keywords: #If the word that user entered is in the list.
          if word in sentence.lower(): #Then converts users input to all lower case letters.
              return random.choice(greetings_response) #chatbot returns a message depending on what the user has entered.
  return("I did not understand what you said")