import os
import datetime
os.chdir("C:/Users/Fatih")
a = os.getcwd()
print(a)
for i in os.walk(a):
    for j in i:
        if (type(j) == list) :
            if (len(j) == 0):
                continue
            else:
                for k in j:
                    if (k.endswith("pdf")):
                        print(k)
                        