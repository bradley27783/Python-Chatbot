def accountCheck():
  x=int(input("Do you already have an account?\n1-Yes\n0-No"))
  if x==0:
    f1= open("user.txt", "r+")
    f2= open("pass.txt", "r+")
    list1= f1.readlines() 
    list2= f2.readlines()			
    f1.truncate
    f2.truncate
    username=input("What do you want your username to be? ")
    password=input("What would you want your password to be? ")
    list1.append(username)
    list2.append(password)
    f1.write(str(list1))
    f2.write(str(list2))
    f1.close()
    f2.close()
accountCheck()




  