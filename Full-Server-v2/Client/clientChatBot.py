import socket,sys,time

def clientBackbone():
    host = "127.0.0.1"
    port = 5008
        #credentials needed to connect to the server
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
        #crucial bit of coding
    from accountClientSide import createUsername,createPassword,accountClientSide
           #imports the functions involved with account management
    print("Welcome to Zach Industries! We will now prompt you with the account manager.")
    
    n=0
   
    while True:
        dictionary=accountClientSide(n)
        
        username=dictionary["username"]
        password=dictionary["password"]
        login=dictionary["login"]
        
        sentMsg= username+ "       " +password + "       " + login
        
        thisSocket.send(sentMsg.encode())
        
        n = thisSocket.recv(1024).decode()
        if n== "Wrong":
            print("Credentials don't match out database.")
            n=0
        if n== "Confirmed":
            print("You have successfullly logged in!")
            break
        else:
            n=int(n)
    
    print("You can now start chatting with Zach! Go on, say something.")
    message = input()
        #we initialise it here in order to prevent an error
    while message != "end":    #keeps the conversation open until the user types end
        from youtube import getMusic
        
        if "music" in message:
            getMusic()
        
        thisSocket.send(message.encode())
              #send the message to the server
        receivedMess = thisSocket.recv(1024).decode()
        
        
          # This is the same deal like with the server, this is where we will input the actual "music"
          # At the moment I will just put a placeholder print function, to see that it works
          
        from userInput import slow_type  #function which makes Zach type like a human
         
        print("Zach: ",end="")   #Name of ChatBot
        slow_type(receivedMess)   #calls the slow_type function 
        message = input(user + ": ")
              #we ask the user to input some more text, keep the conversation open
    thisSocket.close()
        #when the user types end, the loop breaks, and the connection closes
    print("I hope you enjoyed our services!")
        #this is where we print a final statement to the user

if __name__=="__main__":
    try:
        clientBackbone()
    except KeyboardInterrupt:
        print("\nShuting down. See you soon!")
        
        

        