
def accountCheck():
    x=int(input("Do you already have an account?\n1-Yes\n0-No\n"))
    if x==0:
    createUsername()

def createUsername():

    f1= open("user.txt", "r")
        #we open it in read mode
    string1= f1.read()
        #we read it as a stirng
    list1=string1.split()
        #we make it into a list
    print(list1)
        #checks entries
    f1.close()
        #look into changing this line
    f1=open("user.txt","w")
        #open in write mode, deletes file first
    x=0



    while x==0:
        username=input("What do you want your username to be? ")
        if " " in username:   
            print("Usernames cannot contain spaces.")
            continue
                    #takes care of naughty users
        n=1
        for word in list1:
            if username==word:
                    print("Sorry, this username is taken.")
                    n+=1
                    break
        if n>1:
            continue
        y=input("Are you happy with the username " + username + "?\n1-Yes\n0-No\n")
        if y==0:
            continue 
        list1.append(username)
        string1=" ".join(list1)
        #turns list into a string, to add to the file
        f1.write(string1)
        f1.close()
        x=1
def createPassword:
        
accountCheck()



