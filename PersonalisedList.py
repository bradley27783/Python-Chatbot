import os
from os.path import join
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
for f_name in os.listdir(path):
    if f_name.startswith('artistlist.txt'):
        filename = join(path, f_name)
        print(filename)
        
top10List=filename
artistList = open(filename, "r")
artistList = artistList.read()
artistList = artistList.split(',')

print("Your Top 10 Artists are:")

for count, elem in sorted(((artistList.count(e), e) for e in set(artistList)), reverse=True):
    listmode = '%s (%d)' % (elem, count) #Sorts a the list Descending
    print(elem)
