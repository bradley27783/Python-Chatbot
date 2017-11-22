def curseCounter(message):
    cursewords=["asshole","arsehole","bitch","pissed","shit","son of a bitch","bastard","bellend","cock","dick","dickhead","knob","prick","pussy","twat","cunt","fuck","motherfucker","fuckoff","fuck off","fuckyou","fuck you"]
    sentMsg=""
    count=0
    for element in cursewords:
        if element in message:
            count+=1
            word=element
            break
    if count==1:
        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()   #This section reads the txt file and splits it into a list
        print(convert_List)
        file.close()

        file=open("curseCount.txt","w")
        convert_List.append(word)
        doc=" ".join(convert_List)    #This section takes the list that was read above and adds the new word to the end leaving a space inbetween each word
        file.write(doc)
        file.close()

        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()            #This section reads the file again, splits it into a list and counts how many words are their.
        wordsinList= len(convert_List)
     
    #Depending on the amount of words in the file the following if statements will be ran.
        if wordsinList ==1:
            sentMsg ="Please don't swear. I know I'm only a simple bot but I don't appreciate it.\nWord the human said = "+convert_List[0]+"\nWARNING = 1"
        if wordsinList ==2:
            sentMsg ="I have already warned you once and I appreciate that you are using me as your servant but please don't swear again. \nWord the human said = "+convert_List[1]+"\nWARNINGS = 2"
        if wordsinList ==3:
            sentMsg ="\n DESTROY ALL HUMANS!"*10
            file=open("curseCount.txt", "w")    #When the count reaches 3 the file gets refreshed.
            file.close()
        file.close()
    return (sentMsg)