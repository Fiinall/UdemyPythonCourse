print("""Welcome to Calculator

        Here are the operations that you can do

        1. Summation

        2. Extraction

        3. Multiplication

        4. Division

        Please Selecet the Operatiıon with + , - , * or /

 """)

First_Number = float(input("What is your first number"))
Operation = input("What is your Operator")
Second_Number = float(input("What is the second number"))

if (Operation == "+"):
    Conclusion = First_Number + Second_Number
    print(
        Conclusion
    )
elif (Operation == "-"):
    Conclusion = First_Number - Second_Number
    print("{} ile {}'nın farkı {}'dır".format(
        First_Number, Second_Number, Conclusion
    )
    )
elif (Operation == "*"):
    Conclusion = First_Number * Second_Number
    print(
        Conclusion
    )
elif (Operation == "/"):
    Conclusion = First_Number / Second_Number
    print(
        Conclusion
    )

else:
    print("Düzdün gir lan işlemi")

print("For Now: You can calculate for once. For better apps please wait :) ")