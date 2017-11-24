#This fuction will retrieve the top 100 chart from billboard.com using an unnoficial api
#Then print either the number 1 or the top 10 list

def topCharts():

    print("Loading...")
    import billboard #Imports the api library Billboard.py must be installed to use
    while True:
        userCommand = input("What would you like to know? : ")
        if 'number 1' in userCommand:
            chartList = billboard.ChartData('hot-100') #Retrieves the top 100 chart as a list
            topsong = chartList[0] #Chooses the first song in the list
            print("The number 1 song is: ")
            print(topsong)
        elif 'top 10' in userCommand:
            chartList = billboard.ChartData('hot-100')
            song1 = chartList[0]
            song2 = chartList[1]
            song3 = chartList[2]
            song4 = chartList[3]
            song5 = chartList[4]
            song6 = chartList[5]
            song7 = chartList[6]
            song8 = chartList[7]
            song9 = chartList[8]
            song10 = chartList[9]
            print("The current top 10 is: ")
            print("1) " + str(song1))
            print("2) " + str(song2))
            print("3) " + str(song3))
            print("4) " + str(song4))
            print("5) " + str(song5))
            print("6) " + str(song6))
            print("7) " + str(song7))
            print("8) " + str(song8))
            print("9) " + str(song9))
            print("10) " + str(song10))
        elif userCommand == 'help' or userCommand == 'Help' or userCommand == 'HELP':
            print("You can ask:")
            print("What is the number 1 song")
            print("What are the top 10 songs")
        else:
            print("Sorry I don't understand what you are asking...\nType Help to see what you can say: ")

topCharts()
