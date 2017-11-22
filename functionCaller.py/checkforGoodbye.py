def check_for_goodbye(sentence): 
    import random
    end_keyword = ["i have to go", "close","i am out", "farewell","see you later","peace", "see ya later", "c u later", "bye","later"]
    goodbye_keyword = ["Goodbye!", "See you later!", "Come back soon!","Have a good day!", "Take Care", "Bye!","OK, have a good day!"]
    i = "!" or "'" or "." or ","
    for i in sentence.lower():
        for word in end_keyword:
            if word in sentence.lower():
                return random.choice(goodbye_keyword)
 
    return ("I didn't understand what you said")