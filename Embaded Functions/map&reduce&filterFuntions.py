"""
 reduce(function, iterasyon yapılabilen veritipi(liste vb.))

reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve
daha sonra çıkan sonucu listenin 3. elemanına uygular ve
bu şekilde devam ederek liste bitince bir tane değer döner.



  map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır. (Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.





filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır
ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular.
filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner. Hemen örneklerimize bakalım.
"""

from booleanPrime import prime
from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.
print(list(filter(prime,range(1,200))))
print(list(map(prime,range(1,20))))
print(reduce(lambda x,y : x*y , range(1,6))) # 5 factorial
# max fonksiyonu()
print(max([1,2,3,4,5,6]))
# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

print(reduce(maksimum, [-2,1,100,35,32]))

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y : x * y , liste1,liste2)))
print(list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3)))
# if some lists are longer than the shortest one, extra terms of longer lists will be neglected!!

