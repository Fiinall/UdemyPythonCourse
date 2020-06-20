"""



"""

def a(*args):
    for i in args:
        print(i)

a(1,2,3)
print("----")
def b(*xyz):
    for i in xyz:
        print(i)
b(4,5,6)
# As you can see, "agrs" is not necesserily.
print("------------------")
def c(string,*numbers):
    for i in numbers:
        print(string,i)
c("Any String",4,7,3,12)

print("-------------------")
# not lets look at **kwagrs
# It is a dictionary
def d(**kwargs):
    print(kwargs)
d(name = "Fatih",surname = "Inal", age = 21)
print("-----------")

def e(**asd):
    print(asd)
e(a = 1,b = 2,c = 3)
# Again the point is ** (Probably)
print("--------------")

def dict(**kwargs):
    for i,j in kwargs.items():
        print("Word =",i,"\nDefinition =",j)
dict(abhor = "tiksinmek")
print("------------------")

def f(*args,**kwargs):
    for i,j in kwargs.items():
        for a in  range(len(args)):
            print("{}. thing --> ".format(args[a]),"\nWord :",i,"\nDefinition :",j)
            continue

f(4,5,9,23,98,loop = "döngü",function = "fonksiyon",data = "veri",module = "modül",object = "obje")
print("---------------------")

# Now let's look at interbedded functions

def primary(a,b):
    print("first parameter :",a,"\nsecond parameter :",b)
primary("Home",23)
print("---")
variable = primary
# Now "variable" is a same function with primary
variable("Python",3.8)
print("---")
del primary # Now I deleted primary function
# Though variable function is still being existed
variable("one",2)
print("--------------------")

# We can write interbedded functions
def bigone(*args):
    print("Numbers: ", args)
    sums = 0  # local variable
    for i in args:
        sums += i
    def littleone(sums):  # local funcion ||| sum is built-in function so I can not use that word here.
        print(
            "Remainder of summaiton of numbers of division by 5 is {}".format(sums % 5))  # there is to many of "of" :P
    littleone(sums)
bigone(1,6,3,8,4,8,3,2,76,5)
print("----------------")

# We can use fonctions as parameter or output;

def fonksiyon(işlem_adı):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        print(toplam) # bu satırı yazmayınca konsolda herhangi bir şey çıkmıyor.
        return toplam # return toplam demek onu bastırmak için yeterli değil mi ?

    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım

    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma

func = fonksiyon("toplama") # now func is toplama function
print(type(func))
func(4,7,889,3,5)
print("------------------------")

def one(a):
    return a%4
def two(a):
    return a%3
def up(a,b,c):
    if (c == "one") :
        print(a(345))
    elif (c == "two"):
        print(b(539))
    else:
        print("wrong entry")
up(one,two,"one")
up(one,two,"two")






