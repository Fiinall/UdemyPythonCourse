"""
Let's briefly talk about what do all and any functions do ?
"""
def allofthem (liste) :
    for i in liste :
        if not i :
            return False
    return True

def noneofthem(liste):
    for i in liste :
        if i :
            return True
    return False


a = [True, True, True, True, True, True]
b = [True, True, True, True, True, True]
c = [True, True, True, True, True, False]
d = [True, True, True, True, False, False]
e = [False,False,False,False,False,False,]

print(allofthem(a))
print(allofthem(b))
print(allofthem(c))
print(allofthem(d))
print("-------------")
print(noneofthem(a))
print(noneofthem(b))
print(noneofthem(c))
print(noneofthem(d))
print(noneofthem(e))
print("--------------")
"""
It didn't brielfly :) We have functions of logical operation "and" & "or" 

!!! BTW important reminder: 0 is False and all other number are True; as seen below
"""
print(allofthem([1,1,1,1,1,0,234,45,67,5604]))
print(noneofthem([0,0,0,0,0,0,0,1,0,0,0,234,345,678,23]))
print("--------------")
#---------------------#

"""

all() function returns True if all entire list it take only contain True,  }
      at least one value is False --> it returns False.                     } it is like "OR" logical operation

any() function function returns False if all entire list it take only contain False,  }
      at least one value is True --> it returns True.                     } it is like "AND" logical operation
      
"""

print(all(a))
print(all(b))
print(all(c))
print(all(d))
print("--------------")
print(any(a))
print(any(b))
print(any(c))
print(any(d))
print(any(e))




