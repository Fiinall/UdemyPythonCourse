x = 0
a = int(input("What is the coefficient of second order variable, a = "))
b = int(input("What is the coefficient of first order variable, b = "))
c = int(input("What is the coefficient of constant number, c = "))

print("Your Equation is : \n")
print("{}*x^2 + {}*x + {}".format(a , b , c))
print("Roots are calculating")

Delta = b**2 - 4*a*c

Root_1 = (-b + Delta**0.5)/(2*a)
Root_2 = (-b - Delta**0.5)/(2*a)

print("Your Quadratic Equations Roots are {} and {}".format(Root_1,Root_2))






