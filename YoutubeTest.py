
import urllib
import urllib.request
import urllib.parse
import re
import pafy   #For the code to run you must install the latest pafy and youtube-dl
import json
import webbrowser

user_search = urllib.parse.urlencode({"search_query" : input("Type a song... ")})       #Retrieves users search input
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + user_search)     #Searches youtube using user input
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())     #Retrieves the search results from youtube and decodes them
url1 = "http://www.youtube.com/watch?v=" + search_results[0]      #Saves the url of the first search result
url2 = "http://www.youtube.com/watch?v=" + search_results[1]
url3 = "http://www.youtube.com/watch?v=" + search_results[2]
url4 = "http://www.youtube.com/watch?v=" + search_results[3]
url5 = "http://www.youtube.com/watch?v=" + search_results[4]
video1 = pafy.new(url1)         #Assigns the url to pafy and names it video
video2 = pafy.new(url2)
video3 = pafy.new(url3)
video4 = pafy.new(url4)
video5 = pafy.new(url5)
print("1." + video1.title)         #Prints the exact title from youtube of the video
print("2." + video2.title)
print("3." + video3.title)
print("4." + video4.title)
print("5." + video5.title)
choice1 = input("Choose the correct song: ")
if choice1 == '1':
    webbrowser.open_new(url1)       #Opens the url in your default browser
if choice1 == '2':
    webbrowser.open_new(url2)
if choice1 == '3':
    webbrowser.open_new(url3)
if choice1 == '4':
    webbrowser.open_new(url4)
if choice1 == '5':
    webbrowser.open_new(url5)
