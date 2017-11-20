def facts():
    """A function that displays appropriate facts for the selected artist"""
    while True:
        import itertools 
        with open('facts.txt', "r") as file: #opens the fact.txt document and defines it as 'file'
    
            artist = input("Please enter a artist: ") #asks the user to imput an artist name
    
            if artist in ('kanye west', 'Kanye West', 'kanye'): #if input defines the artist this block of code is executed                       
                for fact in itertools.islice(file, 1, 4,): #finds the lines in the facts file that contain the appropriate facts, which in thsi case is lines 1 - 4
                    print(fact) #prints facts 
                        
                #code repeats below but with different artists defined
                
            elif artist in ("the beetles", 'The Beetles'):       
                for fact in itertools.islice(file, 5, 10,):
                    print(fact)
                        
            elif artist in ("rick astley", 'Rick Astley'):        
                for fact in itertools.islice(file, 11, 14,):
                    print(fact)
                        
            elif artist in ("ed sheeran", 'Ed Sheeran'):   
                for fact in itertools.islice(file, 15, 18):
                    print(fact)
            
            elif artist in ("taylor swift", 'Taylor Swift'):   
                for fact in itertools.islice(file, 19, 22):
                    print(fact)
                
            elif artist in ("eminem", 'Eminem', 'slim shady', 'Slim Shady'):   
                for fact in itertools.islice(file, 23, 26):
                    print(fact)
                
            elif artist in ("michael jackson", 'Michael Jackson'):   
                for fact in itertools.islice(file, 27, 30):
                    print(fact) 
                
            elif artist in ("ellie goulding", 'Ellie Goulding'):   
                for fact in itertools.islice(file, 31, 35):
                    print(fact)
                
            elif artist in ('cancel', 'stop', 'break', 'exit', 'quit'): #if statement is broken if one of teh variables is inputted 
                exit()
                
            else:
                print("Error!!!Please try again, make sure you have spelt the artist names correctly!!!") #prints error message and calls the function again
                break
facts()        
  
