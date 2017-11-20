from collections import Counter
import csv

file = open("ArtList", 'r')
lines = file.readlines()


ArtistList = open(ArtList.txt, 'r')
reader = csv.reader(ArtistList)
allRows = [row for row in reader]


#ArtistList=["Rihanna","Drake","Drake","DJ,Blue"]
Artist=input("User searches and we get artist")
ArtistList.append(Artist)

sorted(ArtistList,reverse=True)

print(Counter(ArtistList))
