import random
import time



print("""
Welcome to Jumanji 
""")

random_number = random.randint(1,40)
life = 8
while True :
    estimation = int(input("Your Estimation : ?"))

    if ( estimation < random_number) :
        print("Checking..")
        time.sleep(1)

        print(" Go Up")
        life -= 1
    elif (estimation > random_number) :
        print("Checking..")
        time.sleep(1)

        print(" Go Down")
        life -= 1
    else :
        print("Checking..")
        time.sleep(1)
        print("Congratulations!","You found the number :",random_number)
        break
    if (life == 0 ):
        print("Game Over :( ","The number was :",random)
        break
