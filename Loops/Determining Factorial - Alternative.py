print("""       Hello       

        I Can Help You to Determine Your Numbers Factorial

        To Exit Press the "q"

      """)

while True:
    Number = (input("Please Enter Your Number"))
    if (Number == "q"):
        print("Exiting...")
        break
    else:
        Factorial = 1
        Number = int(Number)
        for  i in range(1,Number+1) :
            Factorial = i*Factorial
            i += 1
    print(Factorial)



