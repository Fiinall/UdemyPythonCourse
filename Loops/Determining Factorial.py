print("""       Hello       
      
        I Can Help You to Determine Your Numbers Factorial
        
        To Exit Press the "q"
      
      """)

while True:
    Number = (input("Please Enter Your Number"))
    if (Number == "q"):
        print("Exiting...")
        break
    else :
        i = 1
        Factorial = 1
        Number = int(Number)
        while (i < Number or i == Number) :
            Factorial = i*Factorial
            i += 1
        print(" {} Factorial = ".format(Number), Factorial)




