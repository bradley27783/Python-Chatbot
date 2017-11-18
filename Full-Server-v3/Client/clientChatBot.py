import socket,sys,time

def clientBackbone():
    host = "127.0.0.1"
    port = 5009
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
    
    print("You can now start chatting with Zach!")
        #we initialise it here in order to prevent an error
    
    thisSocket.send(" ".encode())
    
    infoString= thisSocket.recv(1024).decode()
    
    userInfoList=infoString.split(" ")
    
    if userInfoList[0] == "" or userInfoList == " ":
        print("It seems it's the first time you've ever logged in!")
        while True:
            terminalName = input("Input a name which the chatbot will call you: ") 
            if " " in terminalName or terminalName=="":
                print("Sorry, usernames can't be blank or contain spaces.")
            else:
                break
        terminalName= "   456   " + terminalName
        thisSocket.send(terminalName.encode())
        
        terminalName= thisSocket.recv(1024).decode()
        print("Everything is in order! Thanks.")
    else:
        terminalName=userInfoList[0]
    
    while True:    #keeps the conversation open until the user types end
        
        message = input(terminalName + ": ")
        
        if message == "end":
            break
            
        from youtube import getMusic
        from manualplaylistCreator import manualCreatePlaylist
        
        if "music" in message and "play" in message:
            getMusic()
        elif "create" in message and "playlist" in message:
            pass#manualCreatePlaylist()
        else:
            message="Whoops we haven't coded that in yet"
            
        thisSocket.send(message.encode())
              #send the message to the server
                              
        receivedMess = thisSocket.recv(1024).decode()
                     
        print("Zach: ",end="") 
        print(receivedMess)    #Name of ChatBot
               
        
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
        
        

        