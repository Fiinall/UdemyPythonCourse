# decorators are very useful while adding additional features to some functions.
# it is being often used in flask
from time import time
from math import factorial

def measure_time(func): # this is an additional feature
    def wrapper(argument):
        start = time()
        operation = func(argument)
        end = time()
        print(func.__name__+" "+"took "+str(end-start)+"seconds")
        return operation
    return wrapper

@measure_time
def any_function(arg):
    conc = []
    for i in arg:
        conc.append(factorial(i))
    return conc # bu satır ile conc u ileride kullanamayacak mıyım? Ne işe yarıyor bu return o zaman ?

@measure_time
def another_function(arg):
    conc2 = []
    for i in arg:
        conc2.append(i % 45)
    return conc2


conc = any_function(range(1,4000,4))
another_function(conc)



