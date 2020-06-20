print("""
Hi there! 
You seem to forget the pronunciation of some numbers. Don't be afraid I'll tell 'em
Let's give me number and I tell you its way of read.
As lon as you give me numbers, I'll continue to tell you their pronunciation
If you want to quit just press the "q" then I'll be lost!
""")
def Pronunciation0_9(number) :
    units_digit = {"0": "Zero", "1" : "One" , "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    print(units_digit[number[0]])
    # a = units_digit[number[0]]  If I use return of this in another place these 2 line is enough
    #     #return a

def Pronunciation_of_Teens(number):
    teens = {"10" : "Ten" , "11" : "Eleven" , "12" : "Twelve" , "13" : "Thirteen" , "14" : "Fourteen" , "15" : "Fifteen" , "16" : "Sixteen" , "17" : "Seventeen" , "18" : "Eighteen" , "19" : "Nineteen"}
    print(teens[number])
    return teens[number]

def Pronunciation20_99(number):
    tens_digit = { "0" :"" , "2" : "Twenty" , "3" : "Thirty" , "4" : "Fourty" , "5" : "Fifty" , "6" : "Sixty" , "7" : "Seventy" , "8" : "Eighty" , "9" : "Ninety"}
    units_digit = {"0" : "" , "1" : "One" , "2" : "Two" , "3" : "Three" , "4" : "Four" , "5" : "Five" , "6" : "Six" , "7" : "Seven" , "8" : "Eight" , "9" : "Nine"}
    print(tens_digit[number[0]] , units_digit[number[1]] )
    return tens_digit[number[0]] + " " + units_digit[number[1]]

def Pronunciation100_999(number):
    hundreds_digit = {"0": "", "1" : "One" , "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    units_digit = {"0": "", "1" : "One" , "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    if (number[1] == "0") :
        print(hundreds_digit[number[0]],"hundred",units_digit[number[2]])
    elif (int(number[1:]) >= 10 and int(number[1:]) < 20) :
        print(hundreds_digit[number[0]],"hundred",Pronunciation_of_Teens(number[1:]))
    elif (int(number[1:]) >= 20 and int(number) <= 999) :
        print(hundreds_digit[number[0]],"hundred",Pronunciation20_99(number[1:]))

while True :
    number = input("Yes.. What do I look for ? \n:")
    if (number == "q") :
        break
    elif (len(number) == 0 or number == " ") :
        print("Oh Come On!! You didn't give me any number. Please try it again.")
    elif (int(number) >= 10 and int(number) < 20) :
        Pronunciation_of_Teens(number)
    elif ( len(number) == 1) :
        Pronunciation0_9(number)
    elif (len(number) == 2) :
        Pronunciation20_99(number)
    elif (len(number) == 3) :
        Pronunciation100_999(number)
