from Functions.Result import Result

print("""
             Hi! 
    You give me a number and I tell you 
    is that a prime number ?   

    If you want to quit just press the "q"

                    """)


def prime(a):
    if a == 1:
        return Result("1 is not prime either unprime", 0)
        # print("1 is not prime either unprime")
    elif a == 0:
        # buraya neden break yazamıyorumm. Outside loop hatası veriyor.
        return Result("0 girdin", -1)
        print("hass*ktir b*k")
    elif a == 2:
        return Result("prime", 1)
    for i in range(2, a):
        if a % i == 0:
            return Result("Your number {} is not a prime number".format(a), 1)
            # print("Your number {} is not a prime number".format(a))
            break
        elif i == a - 1:  # there is mistake here fix it
            return Result("prime", 1)
            # print(" Oh Baby you have a Prime number. Give me Five !!")


while True:
    number = input("What is your Number")
    if (number == "q"):
        print("Goodbye...")
        break
    else:
        number = int(number)
        result = prime(number)
        print(result.message)

