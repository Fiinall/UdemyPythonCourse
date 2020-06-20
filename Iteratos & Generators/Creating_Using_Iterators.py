# Iterators are literally objects that provide us to ...... like for loops
# To being iterable object, the object has to define __iter()__ & __next()__ methods.

# When we talk about ordinary function, function
# when it is called, scope of function is entirely executed and then
# If it called again, scope of function is entirely executed again !

# When we look at the generators. We'll see that functions execute the scope TILL yield.
# and then it will start to execute scope from yield.

def foo():
    print("This is the firs time generator runs")
    yield 1

    print("Now it's second")
    yield 2

    print("There is third one")
    yield 3

f = iter(foo())
print(next(f))
print(next(f))
print(next(f))


print("-------------------------")
# To show how it works let's do an example;
list = [1,5,12,"Final",200,"Python"]
# Normally you can get all index one by one with for loop.
for i in list:
    print(i)
print("--------1--------")

# let do same thing with iterators;
ite = iter(list)
for i in range(len(list)):
    print(next(ite))
# You can see the same output.

# The other important point --> 'for loop' can stop when it  reach its last index.
# Whereas while doing same thing with iterators, If you try to go more forward than it have; You get 'StopIteratoin' Error
# Example;
#   Traceback (most recent call last):
#       File "C:/Users/Fatih/Desktop/Final/My improvements/Coding Exercise/Iteratos & Generators/Creating_Using_Iterators.py", line 14, in <module>
#         print(next(ite))
#   StopIteration
print("--------2-----------")
# We can avoid the problem with try except methods
ite = iter(list) # Neden bunu buraya tekrar yazmam gerekti || Yazmayınca try: alındaki print herhangi bişey bastırmadı.
while True:
    try:
        print(next(ite))
    except StopIteration:
        break
print("-------------3----------")
# Now let's create our own iterable objects
class student():
    def __init__(self,name,faculty,department,grade):
        self.name = name
        self.faculty = faculty
        self.department = department
        self.grade = grade
        self.index = -1
    info = [self.name,self.faculty,self.department,self.grade]
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if (self.index < len(self.info)):
            return self.info[self.index]
        else:
            self.index = -1
            raise StopIteration


me = student("Fatih","Eng","Mech",3)

print(me) # Neden bu satır çalışmıyor. Hata vermiyor ancak hiç bir şey de bastırmıyor.
print(me.grade) # Neden bu satır çalışmıyor. Hata vermiyor ancak hiç bir şey de bastırmıyor.
ite = iter(me)
print(next(ite)) # Neden bu satır çalışmıyor. Hata vermiyor ancak hiç bir şey de bastırmıyor.
print(next(ite)) # Neden bu satır çalışmıyor. Hata vermiyor ancak hiç bir şey de bastırmıyor.





