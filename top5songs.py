def TopPersonalSongs(S):
    from collections import Counter    #imports collections.Counter
    if S==True:
        TopPersonalArt("Rihanna")     #runs TopPersonalArt function and gets the sorted element of top 5 artists
        #code for top song based on artists
        #      
        #
              
def accessToTop5(word):            
    searchedWord=["top10","favorite","top","top5","best"] #list for searched words
    if str(word) in searchedWord :    #ask the user if he wants a top 5 
        ask=input("Would you like a personalised top 5?(Y/n)")
        if ask=="n" :
            quit()
        else: 
            return TopPersonalSongs("word")     #if yes gows to function topPersonalSongs
