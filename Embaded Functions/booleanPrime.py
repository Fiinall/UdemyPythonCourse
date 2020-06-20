from math import floor
def prime(a):
    if (a == 0):
        raise ValueError("0 is neither prime, nor composite number")
    if ( a == 1 or a == 2 or a == 3):
        return True
    i = 2
    while (i<=a**0.5):
        if (a%i == 0):
            return False
        elif (i == floor(a**0.5)):
            return True
        i += 1
