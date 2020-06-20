print("Give me 5 numbers")
n1 = int(input("What is your 1. number"))
n2 = int(input("What is your 2. number"))
n3 = int(input("What is your 3. number"))
n4 = int(input("What is your 4. number"))
n5 = int(input("What is your 5. number"))
print("Your numbers {}, {}, {}, {} and {}".format(n1,n2,n3,n4,n5))
print("Now I'm gonna give you the greatest one")
if (n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5):
    print("the greatest one is 1. number")
elif (n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5):
    print("the greatest one is 2. number")
elif (n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5):
    print("the greatest one is 3. number")
elif (n4 > n1 and n4 > n3 and n4 > n2 and n4 > n5):
    print("the greatest one is 4. number")
elif (n5 > n1 and n5 > n3 and n5 > n4 and n5 > n2):
    print("the greatest one is 5. number")





