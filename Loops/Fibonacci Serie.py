print("Hello")
Step = int(input("How many step does your Fibonacci series have"))
a = 1
b = 1
Fibonacci = [a,b]
for i in range(2 , Step) :
    Fibonacci.append(a + b)
    a,b = a+b,a
print(Fibonacci)
#1 1 2 3 5 8 13

