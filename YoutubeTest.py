import urllib
import urllib.request
import urllib.parse
import re
import pafy
import json
import http

query_string = urllib.parse.urlencode({"search_query" : input("Type a song... ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]
video = pafy.new(url)
print(video.title)
choice1 = input("Is this the correct song? (Y/n) ")
if choice1 == 'Y':
    urllib.request.urlopen(url)
