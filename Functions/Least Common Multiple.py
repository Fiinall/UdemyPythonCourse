print("""
Please give me 2 number and I tell you their greatest common divisor
To Quit just press the q
""")

def LCM(number1,number2):
    multiples_list1 = []
    multiples_list2 = []
    for i in range(1,number2+1) :
        multiples_list1.append(number1*i)
    for i in range(1,number1+1):
        multiples_list2.append(number2*i)
    print("Firt number's multiples are: {}".format(multiples_list1) , "\nSecond number's multiples are : {}".format(multiples_list2))
    multiples_list1.sort()
    multiples_list2.sort()
    for i in multiples_list1 :
        if i in multiples_list2 :
            print("Your numbers Least Common Multiple is {}".format(i))
            return i
            break
        if ( i == number1*number2): 
            print("Your numbers least common multiple is their multiplication")
while True :
    number1 = input("What is your first number")
    number2 = input("What is your second number")
    """if (number1 or number2 == "q"):
        print("Shot Down...")
        break """
    number1 = int(number1)
    number2 = int(number2)
    LCM(number1,number2)










