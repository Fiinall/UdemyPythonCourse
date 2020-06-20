"""

Combining lists into one list.

"""
liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10, 11]
liste3 = ["Python","Php","Java"]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.
#-------without zip funciton-----
i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i], liste2[i]))

    i += 1
print(sonuç)
#-------------------------------
#---- with zip function---------
list3 = zip(liste1,liste2)
print(list(list3))
print(list(zip(liste1,liste2,liste3)))

#--------------------------------------------#

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)


# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

print(list(zip(sözlük1,sözlük2))) # Anahtarlar eşleşti
print(list(zip(sözlük1.values(),sözlük2.values()))) # Değerler eşleşti













