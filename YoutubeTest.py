def searchYoutube()

import urllib
import urllib.request
import urllib.parse
import re
import pafy   #For the code to run you must install the latest pafy and youtube-dl
import json
import webbrowser

user_search = urllib.parse.urlencode({"search_query" : input("Type a song... ")}) #Retrieves users search input
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + user_search) #Searches youtube using user input
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) #Retrieves the search results from youtube and decodes them
url = "http://www.youtube.com/watch?v=" + search_results[0] #Saves the url of the first search result
video = pafy.new(url) #Assigns the url to pafy and names it video
print(video.title) #Prints the exact title from youtube of the video
choice1 = input("Is this the correct song? (Y/n) ")
if choice1 == 'Y':
    webbrowser.open_new(url) #Opens the url in your default browser
