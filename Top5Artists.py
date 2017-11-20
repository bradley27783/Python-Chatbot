Top5List=["Rihanna","Drake","SelenaGomez","Khale","Drake","Drake","Rihanna"]   #Start with empty lis tand keep adding searches
artist=input("Artist?")     #Should be made to take the input(artist)everytime user searches somthing
Top10List.append(artist)#Adds to list

for count, elem in sorted(((Top5List.count(e), e) for e in set(Top5List)), reverse=True):
    print '%s (%d)' % (elem, count)   #Sorts a the list Descending and prints



