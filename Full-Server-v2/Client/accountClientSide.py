
def accountClientSide(userCount):
    x=0
    if userCount==0:
        while True:
            x=input("Do you have an account?\n1-Yes\n0-No\n")
            if x=="1" or x=="0":
                x=int(x)
                break
            else:
                print("Only 1 or 0 please.")
    while True:
        if userCount==1:
            x=int(input("We have detected that this username is linked to another account.\nIs this account yours?\n1-Yes\n0-No\n"))
        dictionary={}
        n=""
        if x==0:
            dictionary["username"]=createUsername(userCount)   
            dictionary["password"]=createPassword()
            dictionary["login"]="False"
            x=1
            return(dictionary)
        elif x==1:
            dictionary["username"]=input("Username: ")
            dictionary["password"]=input("Password: ")
            dictionary["login"]="True"
            return(dictionary)
            
def createUsername(userCount):
    while True:
        if userCount == 0:
            username=input("What do you want your username to be? ")      
        elif userCount > 0:
            username=input("Pick another username please: ")
        if " " in username or username=="":   
            print("Usernames can't be blank or contain spaces.")
            continue    
        return(username)
        

def createPassword(): 
    while True:
        password=input("What do you want your password to be? ")
        passwordCheck=input("Confirm your password: ")
        if passwordCheck!=password:
            print("Passwords don't match.")
            continue
        if " " in password or password=="":
            print("Passwords can't be blank or contain spaces.")
            continue
        return(password)
        

