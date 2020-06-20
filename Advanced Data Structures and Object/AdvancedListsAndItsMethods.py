# extend() method is like append method but this help you for add whole list into another list;
print("extend method; \n")
list1 = [1,2,3,4]
list2 = [45,6893,245,667,"asd"]
list1.extend(list2)
print(list1)
print("---------")
# insert(index,element) method inserts an element into specified index
print("insert method; \n")
list3 = [1,3,6,"sdf",425,35]
print(list3)
list3.insert(0,"Zeroth index")
list3.insert(3,"3rd index")
print(list3)
print("------------")
# pop() method does two work
# 1. subtract index
#   1.1 if not specified it subtracts last index
#   1.2 if specified, it subtracts specified index
# 2. returns substracted index
list4 = [1,2,3,4,5,6,"asd",7,8]
print("pop method; \n")
list4.pop() # last index 8 is gone
print(list4.pop(4)) # 4. index 5 is gone and printed
list4.pop(2) # 2nd index 3 is gone
print(list4)
print("------------")
# remove method removes specified element of list with it string
# remove method required just element, not index
print("remove method;\n")
list5 = [1,2,4,"final",5]
print(list5)
list5.remove(2) # it removes element 2 , not 2nd index. As you can see 2nd index 4 is still in list
list5.remove("final")
print(list5)
print("---------")
print("index method;\n")
#index method search for whatever you want to find and returns its index.
#If you specified the method starts from an index to search
list6 = [23,56,23,100,78,225,8,100,235,9,34,3675,1,45,36,100,575,233]
print(list6.index(100)) # Start search from beginning for 100 and stop when first encounter.
print(list6.index(100,5)) # Start search from 5. index for 100 and stop when first encounter.
# in list6 100 element first comes up 3rd index and second time comes up on 7th index
print("----------")
#count method counts an element for how mant times exist in list // Bu ne biçim ingiliççe
print("count method; \n")
list7 = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
print("list7 has {} times 1".format(list7.count(1)))
print("------------")
# sort() metodu
# sort() metodu bir listenin elemanlarını sayıysa küçükten büyüğe , string ise alfabetik olarak sıralar.
# Eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.
print("sort method; \n")
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)
list8 = ["Aston Martin","BWM","Mercedes","Lamborghini",]
list8.sort()
print(list8)
list8.sort(reverse=True)
print(list8)
# --- The End ---