"""
Here we have some functions about numbers
"""
print(bin(4))
print(bin(12))
print(bin(40))
print(bin(452))
print("----------")
for i in range(1,35) :
    print(hex(i))
print("----------")
"""
hex() turns decimal to hexadecimal.
0 1 2 3 4 5 6 7 8 9 a b c d e f 10 11 12 13 14 15...

abs() gives absolute value

"""
abs(-3)
abs(32)
abs(-123)
abs(42.5)
abs(-92.53)

"""
round() / round( , ) functions round decimally numbers to integer. .5 and lower decimal go to lower integer and .6 and up go to higher integer. Let's see
round(12.22345,3) means round for 3 decimal after point.
"""

i = 0
t = 12
while i < 1:
    newt = t+i
    print("{} + {} = {} is rounded to {}".format(t,i,newt,round(newt)))
    i += 0.1
print("------------")
print((round(2.59409393202,4)))
print(round(435.129,2))
print(round(482.3275,3)) # Do NOT forger ! .5 is also round to lower integer.
print("-------------------")

"""
max() & min() functions gives max and min of a data.
"""
# They could be used directly without and list or tuple
# But They also could take lists and tuples as parameter.

print(max(243,456,34,67,79,23,12,57,344, -2341,6,22,7,22))
print(max([243,456,34,67,79,23,12,57,344,-2341,6,22,7,22]))
print(max((243,456,34,67,79,23,12,57,344,-2341,6,22,7,22)))
#  print(max(345,-538,[-243,456,-34,67,79,23,12,57,344,6,22,7,22],-23113,100000))
print("----------------")
print(min(243,456,34,67,79,23,12,57,344, -2341,6,22,7,22))
print(min([243,456,34,67,79,23,12,57,344,-2341,6,22,7,22]))
print(min((243,456,34,67,79,23,12,57,344,-2341,6,22,7,22)))
#  print(min(345,-538,[-243,456,-34,67,79,23,12,57,344,6,22,7,22],-23113,100000))
# !!! max() and min() can take single type parameters.
print("--------------")


"""
sum() function works with lists and tuples. DOES NOT WORK WİTH just variables like sum(2,3,5,6)
"""
print(sum([2,4,78,7,27,3]))
print(sum((2,4,78,7,27,3)))
print(sum([2.3,45,7.234,8.200]))     # Why .733999999 instead of .7340
print(sum((2.3,45,7.2341,8.200)))
print("----------------")

"""
number1 ** number2 ---> is number1 to the power of number2
and pow() function does same thing.
"""
print(pow(2,4))
print(pow(3,5))
print(pow(5,3))
print(pow(400,0.5))
print(pow(2,-2))
print(pow(16,-0.5))
pow("------------")

