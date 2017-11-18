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
        convert_List=doc.split()
        print(convert_List)
        file.close()

        file=open("curseCount.txt","w")
        convert_List.append(word)
        doc=" ".join(convert_List)
        file.write(doc)
        file.close()

        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()
        wordsinList= len(convert_List)
     
        if wordsinList == 1:
            sentMsg ="Please don't swear. I know I'm only a simple bot but I don't appreciate it.\nWord the human said = "+convert_List[0]+"\nWARNING = 1"
        if wordsinList == 2:
            sentMsg ="I have already warned you once and I appreciate that you are using me as your servant but please don't swear again. \nWord the human said = "+convert_List[1]+"\nWARNINGS = 2"
        if wordsinList == 3:
            sentMsg ="\n DESTROY ALL HUMANS!"*10
            file=open("curseCount.txt", "w")
            file.close()
        file.close()
    return (sentMsg)

print(curseCounter("fuck"))