def getMusic():

        print("Loading...")
        n=1
        import time
        import urllib
        import urllib.request
        import urllib.parse
        import re
        import pafy   #For the code to run you must install the latest pafy and youtube-dl
        import webbrowser

        print("Done.")
        user_search = urllib.parse.urlencode({"search_query" : input("Type a song... ")})       #Retrieves users search input
        print("Searching...")
        youtube_content = urllib.request.urlopen("http://www.youtube.com/results?" + user_search)     #Searches youtube using user input
        youtube_results = re.findall(r'href=\"\/watch\?v=(.{11})', youtube_content.read().decode())     #Retrieves the search results from youtube and decodes them
        url1 = "http://www.youtube.com/watch?v=" + youtube_results[0]      #Saves the url of the first search result
        url2 = "http://www.youtube.com/watch?v=" + youtube_results[2]
        url3 = "http://www.youtube.com/watch?v=" + youtube_results[4]
        url4 = "http://www.youtube.com/watch?v=" + youtube_results[6]
        url5 = "http://www.youtube.com/watch?v=" + youtube_results[8]
        video1 = pafy.new(url1)         #Assigns the url to pafy and names it video
        video2 = pafy.new(url2)
        video3 = pafy.new(url3)
        video4 = pafy.new(url4)
        video5 = pafy.new(url5)
        print("Here's what I found:")
        print("1." + video1.title)         #Prints the exact title from youtube of the video
        print("2." + video2.title)
        print("3." + video3.title)
        print("4." + video4.title)
        print("5." + video5.title)
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
                else:
                    print("Sorry that was not an option, try again")

