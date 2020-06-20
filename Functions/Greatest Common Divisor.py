print("""
Please give me 2 number and I tell you their greatest common divisor
""")
def sub_multiple(number) :
    sub_multiples_list = []
    for i in range(1,number+1):
        if (number % i == 0):
            sub_multiples_list.append(i)
        else :
            continue
    return(sub_multiples_list)
while True :
    number1 = int(input("What is your 1st number"))
    number2 = int(input("What is your 2nd number"))
    list1 = sub_multiple(number1)
    print("Your first numbers sub multiples are", sub_multiple(number1))
    list2 = sub_multiple(number2)
    print("Your second numbers sub multiples are", sub_multiple(number2))
    list1.sort(reverse = True)
    list2.sort(reverse = True)
    for i in list2:
        if i in list1 :
            print("The Greatest Common Divisor of your numbers are: " , i)
            break











