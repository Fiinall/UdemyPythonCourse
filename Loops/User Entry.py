print("""

Welcome the ALFA SPACE And AUTO
    
    To enter the operational system please;
    Enter your ID then password
    Have a nice day 
    
""")

ID = "Mercedes"
Password = "GLA200 ///AMG"
a = 0
while ( a < 3 ):
    ID_s = input("Your ID please :  ")
    Password_s = input("Your Password please :  ")
    if  ID_s == ID and Password_s == Password :
        print("Welcome Home :) ")
        break
    elif (ID_s != ID):
        print("I Guess yout ID is not valid")
        a += 1
    elif ( ID_s == ID and Password_s != Password):
        print("Sorry Mercedes but Your Password is not Correct")
        a += 1
        print(a)
    if a == 3 :
        print("You did 3 mistakes. Entering Cancalled")
        break


