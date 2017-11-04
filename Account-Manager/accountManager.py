
#If accountMain is True, then the user has successfully logged in

def accountMain():
    """Manages the bulk of account related operations."""
    while True:
        x=input("Do you have an account?\n1-Yes\n0-No\n")
        if x=="1" or x=="0":
            x=int(x)
            break
        else:
            print("Only 1 or 0 please.")
    while True:    
        if x==0:
            n=createUsername()   #the n lets people stop the account creation
            createPassword(n)   #stops this function 
            if n!=0:		
                print("\nThank you for creating an account!\n")
            x=1
        elif x==1:
            username=input("Username: ")
            password=input("Password: ")
            variable=login(username,password)  #Assigns the return value from the login function
            if variable==4: #4 means login failed
                x=1
            elif variable==7:    #7 means login confirmed 
                return(True)        
            else:
                x=int(variable)   #if x=0, the user creates an account, otherwise he just retries to login
                
            
def createUsername():
    f1= open("user.txt", "r")
        #we open it in read mode
    string1= f1.read()
        #we read it as a stirng
    list1=string1.split()
        #we make it into a list
    #print(list1)
        #checks entries
    f1.close()
        #look into changing this line
 
    while True:
        username=input("What do you want your username to be? ")
        if " " in username or username=="":   
            print("Usernames can't be blank or contain spaces.")
            continue
                    #takes care of naughty users
        n=1  #these variables avoid some errors
        z=1
        for word in list1:   #checks username entry against the database to spot duplicates 
            if username==word:
                print("Sorry, this username is taken.")
                while True:
                    z=input("Do you still want to make an account?\n1-Yes\n0-No\n")
                    if z=="0" or z=="1":
                        z=int(z)
                        break
                    else:
                        print("Only 1 or 0 please.")
                n+=1     #the z here takes care of people who already have an account
        if z==0:   #lets people break the loop and use their existent account 
            return(0)
        if n>1:
            continue
        while True:
            y=input("Are you happy with the username " + username + "?\n1-Yes\n0-No\n")
            if y=="0" or y=="1":
                y=int(y)
                break
            else:
                print("Only 1 or 0 please.")
        if y==0:   #makes sure the username is not mispelled 
            continue 
        f1=open("user.txt","w")
        #open in write mode, deletes file first
        list1.append(username)
        string1=" ".join(list1)
                #turns list into a string, to add to the file
        f1.write(string1)
        f1.close()
        break

def createPassword(n):
    if n==0:   #in case people don't want to create the account 
        return(0)
    f2= open("pass.txt", "r")
        #we open it in read mode
    string2= f2.read()
        #we read it as a stirng
    list2=string2.split()
        #we make it into a list
    #print(list2)
        #checks entries
    f2.close()
        #look into changing this line
    
    while True:
        password=input("What do you want your password to be? ")
        passwordCheck=input("Confirm your password: ")
        if passwordCheck!=password:
            print("Passwords don't match.")
            continue
        if " " in password or password=="":
            print("Passwords can't be blank or contain spaces.")
            continue
        f2=open("pass.txt","w")
           #open in write mode, deletes file first
        list2.append(password)
        string2=" ".join(list2)
           #turns list into a string, to add to the file
        f2.write(string2)
        f2.close()
        break
        
def login(username,password):
    f1= open("user.txt", "r")
    string1= f1.read()
    list1=string1.split()
    f1.close() 
   
    f2= open("pass.txt", "r")
    string2= f2.read()
    list2=string2.split()
    f2.close()
    
    if not(username in list1):
        while True:
            w=input("This username isn't linked to any account. \nWould you like to create one?\n1-Yes\n0-No\n")
            if w=="0" or w=="1":
                w=int(w)
                break
            else:
                print("Only 1 or 0 please.")
        if w==1:
            return(0)
        elif w==0:
            return(1)
      
    i=-1
    for name in list1:
        i+=1
        if username==name:
            if list2[i]==password:
                return(7)   #avoids errors, 7=TRUE
            else:
                print("Credentials don't match our database.")
                return(4)   #4=FALSE
    
    
try:
    print("\n" + str(accountMain()) +"\n")
except KeyboardInterrupt:
    print("\nShuting down.")