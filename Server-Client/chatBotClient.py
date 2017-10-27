import socket

def clientBackbone():
    host = "127.0.0.1"
    port = 5001
        #credentials needed to connect to the server
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
        #crucial bit of coding
    message=input("This is where the user types: ")
        #we initialise it here in order to prevent an error
    while message != "end":    #keeps the conversation open until the user types end
          thisSocket.send(message.encode())
              #send the message to the server
          receivedMess = thisSocket.recv(1024).decode()
        
          # This is the same deal like with the server, this is where we will input the actual "music"
          # At the moment I will just put a placeholder print function, to see that it works
        
          print("The ChatBot said: " + str(receivedMess))
          message = input("This is where the user types: ")
              #we ask the user to input some more text, keep the conversation open
    thisSocket.close()
        #when the user types end, the loop breaks, and the connection closes
    print("I hope you enjoyed our services!")
        #this is where we print a final statement to the user

if 1 == 1:
  clientBackbone()
        
        

        