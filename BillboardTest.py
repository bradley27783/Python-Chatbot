#This fuction will retrieve the top 100 chart from billboard.com using an unnoficial api
#Then print either the number 1 or the top 10 list

def topCharts():

    print("Loading...")
    import billboard #Imports the api library Billboard.py must be installed to use
    while True:
        userCommand = input("What would you like to know? : ")
        if 'number 1' in userCommand:
            chartList = billboard.ChartData('hot-100') #Retrieves the top 100 chart as a list
            topsong = chart[0] #Chooses the first song in the list
            print("The number 1 song is: ")
            print(topsong)
            return()
        if 'top 10' in userCommand:
            chart = billboard.ChartData('hot-100')
            song1 = chart[0]
            song2 = chart[1]
            song3 = chart[2]
            song4 = chart[3]
            song5 = chart[4]
            song6 = chart[5]
            song7 = chart[6]
            song8 = chart[7]
            song9 = chart[8]
            song10 = chart[9]
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
        if userCommand == 'help' or userCommand == 'Help' or userCommand == 'HELP':
            print("You can ask:")
            print("What is the number 1 song")
            print("What are the top 10 songs")
        else:
            print("Sorry I don't understand what you are asking...\nType Help to see what you can say: ")

topCharts()
