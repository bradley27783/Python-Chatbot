def curseCounter(message):
    cursewords=["asshole","arsehole","bitch","pissed","shit","son of a bitch","bastard","bellend","cock","dick","dickhead","knob","prick","pussy","twat","cunt","fuck","motherfucker"]
    sentMsg=""
    if message in cursewords:

        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()
        print(convert_List)
        file.close()

        file=open("curseCount.txt","w")
        convert_List.append(message)
        doc=" ".join(convert_List)
        file.write(doc)
        file.close()

        file= open("curseCount.txt", "r")
        doc= file.read()
        convert_List=doc.split()
        wordsinList= len(convert_List)
     
        if wordsinList ==1:
            sentMsg ="Please don't swear. I know I'm only a simple bot but I don't appreciate it.\nWord the human said = "+convert_List[0]+"\nWARNING = 1"
        if wordsinList ==2:
            sentMsg ="I have already warned you once and I appreciate that you are using me as your servant but please don't swear again\nWARNINGS = 2"
        if wordsinList ==3:
            sentMsg ="DESTROY ALL HUMANS!\n"*50
        file.close()
    return (sentMsg)