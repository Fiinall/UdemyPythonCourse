# When dealing with big datas, generators are good choice.
# To illustrate you're gonna do same operation for 10000 values. Holding these values in a list will occupy so much place.
# For instance range() function is written by generators.

# First let's write a function without generator

def square(*args):
    conc = []
    for i in args:
        conc.append(i ** 2)
    return conc

print(square(1,2,3,4,5))
print("---------------------")
# Now it's time to write it with a generator

def square2(*args):
    for i in args:
        yield i ** 2

generator = square2(1,2,3,4,5,6) # name of variable does not have to be generator :)
print(generator) # Let's look how it looks. See it is a generator.
print("-----------------")

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) # See that just like iterators, you can iterate it with next()
# StopIteration error is also valid for generators.
# !!!! I DON'T KNOW WHY BUT IN THE UDEMY COURSE, INSTRUCTOR, USED 'iterator = iter(generator)' AND THEN
    # WROTE 'print(next(iterator)'. WHAT IS CHANGES ?
print("--------------")

# Recall the listh compherension. We can translate list compherensions to generators.
# by just changing [] with ()
# for example

list = [f * 3 for f in range(1,8)]
print(list)
print("-----------------")
generator = (f * 3 for f in range(1,8))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# !!! AGAIN INSTRUCTOR INSTRUCTOR, USED 'iterator = iter(generator)' AND THEN
#     # WROTE 'print(next(iterator)'. WHAT IS CHANGES ?
print("---------------")

# To understand the idea better think it;

def multi_table():
    for i in range(1,5):
        for j in range(1,5):
            yield "{} * {} = {}".format(i,j,i*j)
        print("---")
for i in multi_table():
    print(i)
# !!! THIS IS MY INFERRING -- I DO NOT SURE IF IT IS TRUE OR NOT!
# Pay attention to the for loop just above. Output of the multiple_table() is an iterable object. for loop iterate on it!
# In my opinion this means that each index is holding in memory.
# But in the udemy course instructor says that,
# the function with 'yield' is a generator and their outputs are not held in memory.

# We can say the generator for how many times it will work before raise StopIteration;

def n_times_func(n):
    i = 1
    while i < n :
        print("{}. Hey".format(i))
        yield "yieding thing"
        i += 1

five = n_times_func(5)
print(next(five))
print(next(five))
print(next(five))
print(next(five))





