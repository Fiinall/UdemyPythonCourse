from datetime import datetime

print(datetime.now())
print("------------")
current = datetime.now().hour,datetime.now().minute
print(current)
print(type(current)) # It is tuple, not list
print("---------------")
current_time = datetime.now()
print(datetime.ctime(current_time))
# ctime() functions requires a variable that defined before with datetime.now()
# It doesn't returns time. It just regulate the output
print("------------")

print(datetime.strftime(current_time,"%Y"))

print(datetime.strftime(current_time,"%B"))

print(datetime.strftime(current_time,"%A"))

print(datetime.strftime(current_time,"%X"))

print(datetime.strftime(current_time,"%D"))

print(datetime.strftime(current_time,"%Y %B %A"))

# for other many options check the website:
# https://docs.python.org/2/library/time.html
print("-------------------")

# to obtain returns in Turkish:
import locale
print(locale.setlocale(locale.LC_ALL,""))
print(datetime.strftime(current_time,"%Y %B %A")) # locale ile bulunduğumuz yerin diline çevirebiliyoruz.
print("------------------------")

"""
timestamp() ve fromtimestamp()
Şu anki zamanı saniye cinsinden bulmak için, 
datetime objemizi (şu_an objesi) timestamp() fonksiyonumuza gönderebiliriz. 
Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine çevirebiliriz.

Peki fromtimestamp() fonksiyonunun içine "0" verirsek ne olacak ? (0. saniye)

Jupyter böyle bir kullanıma hata veriyor. 
Ancak sonuç Python IDLE'da "1970-01-01 03:00:00" çıkacak. 
Buna epoch zamanı deniyor. 
Yani günümüzde kullandığımız bilgisayarlar o andan itibaren sürekli saniye sayıyor ve 
böylelikle şu anki zamanı hesaplayabiliyorlar. Yani bilgisayar aleminde zamanın başlaması 1 Ocak 1970 :) 
Epoch zamanını isterseniz araştırabilirsiniz.
"""

# Calculating gap btw 2 date

born = datetime(1998,5,8)
now = datetime.now()

my_age_in_sec = datetime.timestamp(now) - datetime.timestamp(born) # this is terms of seconds
print("my_age_in_sec:",my_age_in_sec)
my_age = datetime.fromtimestamp(my_age_in_sec) # this functions gives a stupid thing  :D not raleted with me :DD
print(my_age,":P","This is the date If I was worn at 01.01.1970 03.00 :DD")

my_age_in_year = my_age_in_sec / (60*60*24*7*52)
print("my_age_in_year:",my_age_in_year)
print("my age in days:",now - born) # this is the other way of obtaining day gap.
