print("""
Welcome to Final World
I can tell you the sub multiples of a number you select
If you want to quit please just press the "q"
""")
def sub_multiple(number) :
    sub_multiples_list = []
    for i in range(1,number+1):
        if (number % i == 0):
            sub_multiples_list.append(i)
        else :
            continue
    print(sub_multiples_list)
    print(len(sub_multiples_list))
    print("The summation of sub multiples of {} is {}".format(number,sum(sub_multiples_list)))
    if (sub_multiples_list == [1,number]) :
        print("Your number {} is a prime number so it does not have any sub multiple except 1 and itself".format(number))
    if (sum(sub_multiples_list) - number == number) :
        print("Your number {} is a perfect number. The perfect number means that summation of sub multiples equals itself.".format(number))

    """
    for i in sub_multiples_list :
        carpım = lambda i = i*
"""
while True:
    number = input("\n Which number you want to know its sub multiples: \n")
    if (number == "q") :
        print("Okay! C'ya")
        break
    else :
        number = int(number)
        sub_multiple(number)
