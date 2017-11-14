
import socket,sys,time

def serverBackbone():
    """Function which initializes the chatbot server."""
    host = "127.0.0.1"
        #this is the sever's IP, clients needs it to connect
    port = 5008
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
    while True: #repeats the loop forever, until being told otherwise
       
          
          #   This is where the main body of our chatbot will be, where we call other functions, and so on
          #   At the moment I am printing some things back to the user for us to see that it does work
          #   In the future though, we need to figure out ways to actually get the music playing, and do that
        
        from accountServerSide import accountServerSide
        dictionary={}
        while n==0 or n==1:
            receiveMess = conn.recv(1024).decode()
            
            receiveMess= receiveMess.split("       ")
            print(receiveMess)
            dictionary["username"]=receiveMess[0]
            dictionary["password"]=receiveMess[1]
            dictionary["login"]=receiveMess[2]
            
            n=accountServerSide(dictionary)
            
               
            if n == 2:
                returnMess="Wrong"
                n=0
                conn.send(returnMess.encode())
                continue
            if n == 7:
                returnMess="Confirmed"
            else: 
                returnMess=str(n)
            
            conn.send(returnMess.encode())
        print("Achieved!")   
        
        receiveMess = conn.recv(1024).decode()
        if not receiveMess:
            break    
            
        print("The user wrote: " + str(receiveMess))
        
            
    conn.close()

    
if __name__=="__main__":
    serverBackbone()
        
        