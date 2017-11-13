
Top10List=["Rihanna","Drake","SelenaGomez","Khale","Drake","Drake","Rihanna"]
#artist=input("Artist?")#Should be made to take the input(artist)everytime user searches somthing
#Top10List.append(artist)#Adds to list

for count, elem in sorted(((Top10List.count(e), e) for e in set(Top10List)), reverse=True):
    print '%s (%d)' % (elem, count)   #Sorts a the list Descending


print("Your Top 10 Songs Are:")
for i in range(1,11):
        i=i+1
        print(Top10List[i])

