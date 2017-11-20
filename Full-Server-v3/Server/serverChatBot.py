
import socket,sys,time

def serverBackbone():
    """Function which initializes the chatbot server."""
    host = "127.0.0.1"
        #this is the sever's IP, clients needs it to connect
    port = 5009
        #server's port, needs to be the same as the client's
    thisSocket = socket.socket()
    thisSocket.bind((host,port))  
        #programming mumble jumble which makes the whole thing work
    thisSocket.listen(3)
        #number of clients that can connect to the server, 3 at the moment
    conn, addr = thisSocket.accept()
        #addr here is the ip address of the user, conn=connect
    print("Client connected.")
    n=0
                  
    from accountServerSide import accountServerSide, infoHub, clientInfoRegister
    dictionary={}
    while n==0 or n==1:
        receiveMess = conn.recv(1024).decode()
            
        receiveMess= receiveMess.split("       ")    #splits at 7 spaces, creates list 
    
        dictionary["username"]=receiveMess[0]    
        dictionary["password"]=receiveMess[1]    
        dictionary["login"]=receiveMess[2]
            
        username = dictionary["username"]
            
        n=accountServerSide(dictionary)    
            
               
        if n == 2:
            returnMess="Wrong"
            n=0
            conn.send(returnMess.encode())
            continue      #wrong credentials
        if n == 7:
            returnMess="Confirmed"    #when the user logs in, pull the userInfoList for him 
            userInfoList= infoHub(username,"","","")
        else: 
            returnMess=str(n)
            
        conn.send(returnMess.encode())
        
    receiveMess = conn.recv(1024).decode()
    
    informationString=""
    
    for word in userInfoList:   #transform the list into a format that we can send over 
        informationString= informationString + " " + word
    informationString=informationString[1:]  #the first character is a blank, delete that 
    
    conn.send(informationString.encode())  
   
        
    
    while True:
        receiveMess = conn.recv(1024).decode()
        if "   456   " in receiveMess:  #this means that the user doesn't have a terminal name 
            
            receiveMess=receiveMess[9:]  #this is the future terminal name 
            infoHub(username,receiveMess,"","")  #index it 
            
            userInfoList[0]=receiveMess #ammend the list
            
            conn.send(userInfoList[0].encode())  #send the terminal name back
            continue
        if not receiveMess:
            break    
        returnMess = receiveMess    
        print(userInfoList[0] + " wrote: " + str(receiveMess)) #prints to the server terminal for good measure 
        conn.send(returnMess.encode())
            
    conn.close()

    
if __name__=="__main__":
    serverBackbone()
        
        