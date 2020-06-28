import os
from datetime import datetime

print(os.getcwd())
os.chdir("C:/Users/Fatih/Desktop")
print(os.getcwd())
for i in os.listdir():
    print(i)

print("----------------")

# to create embaded directories os.mkddir("asdadasd/qweqweqwe") won't run unless asdasdasd is not exist ,so use ;
 # os.makedirs("Test1/test2") !!!!!!!!!!!! I take the line to comment beacuse it cant run more then 1 times.
print("--------")
# Remove Dir..
# os.rmdir("Test1/test2") !!!!!!!!!!!! I take the line to comment beacuse it cant run more then 1 times.
# os.removedirs("Test/asd/zxc") # removes all directory under this # it should be empty directory

# os.rename("değiştirilcek olan","yeni isim")

os.stat("6th Term.PNG") # dosya hakkında bilfiler veriyor. mesela st_mtime dosyanın değiştirilme zamanı saniye cinisnden
print(datetime.fromtimestamp(os.stat("6th Term.PNG").st_mtime))
print("----------")

print(os.walk("C:/Users/Fatih/Desktop")) # it is generator
for i,j,k in os.walk("C:/Users/Fatih/Desktop"):
    print(i)
