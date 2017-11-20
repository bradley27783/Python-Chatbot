def curseCounter(message,username):
    
    from accountServerSide import infoHub
    
    cursewords=["asshole","arsehole","bitch","pissed","shit","son of a bitch","bastard","bellend","cock","dick","dickhead","knob","prick","pussy","twat","cunt","fuck","motherfucker","fuckoff","fuck off","fuckyou","fuck you"]
    sentMsg=""
    count=0
    for element in cursewords:
        if element in message:
            count+=1
            word=element
            break
    if count==1:
        
        userInfoList = infoHub(username,"","","")  #gets list
        
        if userInfoList[1] == "":   #if first time, make it 0 
            userInfoList[1]=0
            
        userInfoList[1] = int(userInfoList[1]) + 1  #turn to an int then add 1 
        
        swearCount = userInfoList[1]  #indexes the amount swore 
        
        if userInfoList[1] > 2:
            userInfoList[1] = 0 #resets after 3 
            
        infoHub(username,"",str(userInfoList[1]),"")  #index in the database in string form 
        
       
        

     
        if swearCount == 1:
            message ="Please don't swear. I know I'm only a simple bot but I don't appreciate it.\nWord the human said = "+word+"\nWARNING = 1"
        if swearCount == 2:
            message ="I have already warned you once and I appreciate that you are using me as your servant but please don't swear again. \nWord the human said = "+word+"\nWARNINGS = 2"
        if swearCount == 3:
            message ="\n DESTROY ALL HUMANS!"*10
    return (message)

