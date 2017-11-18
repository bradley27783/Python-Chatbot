import pickle

def accountServerSide(dictionary):
    if __name__=="__main__":
        x=input("Do you want to delete the database?\n")
        if x == "Yes, I do, avocados are great.":
            f1=open("database.txt","w")
            print("You monster.")
            f1.close()
            return()
        else:
            print("Nah, fam.")
    username=dictionary["username"]
    password=dictionary["password"]
    login=str(dictionary["login"])
    
    f1= open("database.txt", "r")
        #we open it in read mode
    string1= f1.read()
        #we read it as a stirng
    list1=string1.split()
        #we make it into a list
    f1.close()
    
    x=len(list1)
    
    listUser=list1[0:int(x/2)]
    listPass=list1[int(x/2):x]
    
    if login == "False":
        if username in listUser:
            return(1)
        
        clientInfoRegister(username)
        
        listUser.append(username)
        listPass.append(password)
        
        f1=open("database.txt","w")        
        list1=listUser+listPass    
        string1=" ".join(list1)       
        f1.write(string1)
        f1.close()
        
        return(0)
    
    else:
        i=-1
        for element in listUser:
            i+=1
            if element == username:
                if listPass[i] == password:
                    return(7)
    return(2)


def clientInfoRegister(username):
    dictionaryInfo={}   
    
    try:
        f2=open("clientInfo.txt","rb")
        dictionaryInfo = pickle.load(f2)  
        f2.close()
    except EOFError:
        pass
    dictionaryInfo[username]=["","",""] 
    f3=open("clientInfo.txt","wb")
    pickle.dump(dictionaryInfo,f3)
    f3.close()
    
    return()

def infoHub(username,terminalName,curseCounter,placeholder):
    
    f2=open("clientInfo.txt","rb")
    dictionaryInfo = pickle.load(f2)
    f2.close()
    
    list1 = dictionaryInfo[username]
    
    if terminalName:
        list1[0] = terminalName
    elif curseCounter:
        list1[1] = curseCounter
    elif placeholder:
        list1[2] = placeholder
    else:
        print("User info:" + str(list1))
        return(list1)
    
    dictionaryInfo[username]=list1
    
    print(dictionaryInfo)
    
    f3=open("clientInfo.txt","wb")
    pickle.dump(dictionaryInfo,f3)
    f3.close()
    

if __name__=="__main__":
    try:
        dictionary={"username":"sergiu","password":"test1","login":"False"}
        print(accountServerSide(dictionary))
        print(infoHub("sergiu","","",""))
    except KeyboardInterrupt:
        print("Shutting down.")
