import urllib.request
import urllib.parse
import re
import pafy

query_string = urllib.parse.urlencode({"search_query" : input("Type a song... ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]

video = pafy.new(url)
bestaudio = video.getbestaudio()
downloadChoice = input("Would you like to download" + video.title + "? (Y/n) ")
if downloadChoice == 'Y':
    bestaudio.download()
finalChoice = input("Is that all? (Y/n) ")
if finalChoice == 'Y':
    exit()
