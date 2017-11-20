from collections import Counter

file = open("ArtList.txt", 'r')
lines = file.readlines()

ArtistList = [line.split(' , ')for line in open ("ArtList.txt")]

#ArtistList=["Rihanna","Drake","Drake","DJ,Blue"]
Artist=input("User searches and we get artist")
ArtistList.append(Artist)

sorted(ArtistList,reverse=True)

print(Counter(ArtistList))



