#This fuction uses packages from outside the python standard library called 'pafy' and 'youtube-dl'
##links to these modules will be in the appendix

def getMusic(): #This fuction search in youtube using the user input and return the results.

        print("Loading...")
        import time
        import urllib
        import urllib.request
        import urllib.parse
        import re
        import pafy   #For the code to run you must install the latest pafy and youtube-dl
        import webbrowser

        print("Done.")
        userSearch = urllib.parse.urlencode({"search_query" : input("Enter your search here... ")})       #Retrieves users search input
        print("Searching...")
        youtubeSearch = urllib.request.urlopen("http://www.youtube.com/results?" + userSearch)     #Searches youtube using user input
        resultUrls = re.findall(r'href=\"\/watch\?v=(.{11})', youtubeSearch.read().decode())     #Retrieves the search results from youtube and decodes them
        url1 = "http://www.youtube.com/watch?v=" + resultUrls[0]      #Saves the url of the first search result
        url2 = "http://www.youtube.com/watch?v=" + resultUrls[2]
        url3 = "http://www.youtube.com/watch?v=" + resultUrls[4]
        url4 = "http://www.youtube.com/watch?v=" + resultUrls[6]
        url5 = "http://www.youtube.com/watch?v=" + resultUrls[8]
        url6 = "http://www.youtube.com/watch?v=" + resultUrls[10]      #Saves the url of the first search result
        url7 = "http://www.youtube.com/watch?v=" + resultUrls[12]
        url8 = "http://www.youtube.com/watch?v=" + resultUrls[14]
        url9 = "http://www.youtube.com/watch?v=" + resultUrls[16]
        url10 = "http://www.youtube.com/watch?v=" + resultUrls[18]
        song1 = pafy.new(url1)         #Assigns the url to pafy and names it song
        song2 = pafy.new(url2)
        song3 = pafy.new(url3)
        song4 = pafy.new(url4)
        song5 = pafy.new(url5)
        song6 = pafy.new(url6)         #Assigns the url to pafy and names it song
        song7 = pafy.new(url7)
        song8 = pafy.new(url8)
        song9 = pafy.new(url9)
        song10 = pafy.new(url10)
        print("Here's what I found:")
        print("1." + song1.title)         #Prints the exact title from youtube of the song
        print("2." + song2.title)
        print("3." + song3.title)
        print("4." + song4.title)
        print("5." + song5.title)
        while True:
                choice1 = input("Choose the correct song by typing the correct number:\nPress Enter to see the next 5 options...............:")
                if choice1 == '1':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url1) 
                        return()#Opens the url in your default browser
                elif choice1 == '2':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url2)
                        return()
                elif choice1 == '3':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url3)
                        return()
                elif choice1 == '4':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url4)
                        return()
                elif choice1 == '5':
                        print("Opening Browser...")
                        time.sleep(1)
                        print("Goodbye :)")
                        time.sleep(0.5)
                        webbrowser.open_new(url5)
                        return()
                elif choice1 == '':
                        print("6." + song6.title)         #Prints the exact title from youtube of the song
                        print("7." + song7.title)
                        print("8." + song8.title)
                        print("9." + song9.title)
                        print("10." + song10.title)
                        while True:
                                choice1 = input("Choose the correct song by typing the correct number: ")
                                if choice1 == '1':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url1) 
                                        return()#Opens the url in your default browser
                                elif choice1 == '2':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url2)
                                        return()
                                elif choice1 == '3':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url3)
                                        return()
                                elif choice1 == '4':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url4)
                                        return()
                                elif choice1 == '5':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url5)
                                        return()
                                if choice1 == '6':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url6) 
                                        return()#Opens the url in your default browser
                                elif choice1 == '7':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url7)
                                        return()
                                elif choice1 == '8':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url8)
                                        return()
                                elif choice1 == '9':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url9)
                                        return()
                                elif choice1 == '10':
                                        print("Opening Browser...")
                                        time.sleep(1)
                                        print("Goodbye :)")
                                        time.sleep(0.5)
                                        webbrowser.open_new(url10)
                                        return()
                                else:
                                        print("Sorry that was not an option, try again")
                        
                else:
                        print("Sorry that was not an option, try again")

getMusic()
