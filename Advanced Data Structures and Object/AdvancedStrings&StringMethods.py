"""
upper() and lower do their own name.
"""
print("This iS aN eXampLE".upper())
print("This iS aN eXampLE".lower())
print("----------1")

"""
replace(a,b) changes a with b in a string
"""
print("Bamboleyyo".replace("amb","441"))
print("A B C D".replace(" ","____"))
print("----------------2")

"""
startswith() & endswith() --> returns as True or False accoding their first and last index
"""
print("abcdef".startswith("a"))
print("12345".startswith("12"))
print("adasdsad".startswith("k"))
print("----")
print("abcdef".endswith("f"))
print("12345".endswith("45"))
print("adasdsad".endswith("k"))
print("-------------------3")
"""
split() splits from any index you want and gives list
"""
print("Mercedes Benz E 400 AMG Edition 1".split(" "))
print("-------------------4")

"""
strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.
"""
print("------------------------asdasdasd--------------".strip("-"))
print("------------------------asdasdasd--------------".lstrip("-"))
print("------------------------asdasdasd--------------".rstrip("-"))
print("                               a                       ".strip())
print("                               a                       ".strip(" ")) # same with above line
print("-------------------------5")

"""
join() combines each index of list that it takes as parameter
"""
print("/".join(["asd","40t","s2","204"]))
print("----------------------6")

"""
count() counts the index that it takes as parameter. It can also start to count from where you want
"""

print("Mercedes Benz E 400 AMG Edition 1".count("e"))
print("Mercedes Benz E 400 AMG Edition 1".count(" "))
print("Mercedes Benz E 400 AMG Edition 1".count("e",5))
print("----------------------------7")

"""
find() ve rfind()

find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
"""
print("Mercedes Benz E 400 AMG Edition 1".find("r"))
print("Mercedes Benz E 400 AMG Edition 1".find("k"))
print("Mercedes Benz E 400 AMG Edition 1".rfind("E"))
print("Mercedes Benz E 400 AMG Edition 1".rfind("k"))
print("-------------------------8")




