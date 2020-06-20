a = {1, 2, 3}
b = set()
print(type(a))
print(type(b))
# a list can be set
c = [1, 3, 5, 6, "ABC", "XYZ"]
print(set(c))
"""
!!! Sets are a data type that holds only one from each element, as in mathematics.
"""
print({1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4})
d = ["Mercedes Benz is a good manufacturer"]
print(set(d[0])) # If we do like this there is only one from each letter
e = ["Mercedes Benz is a good manufacturer", "asd", "Mercedes Benz is a good manufacturer"]
print(set(e)) # If we do like this, there is a 3 term inside the list e and 2 of them is similar so in set one of them is exist.
# sets dont have queue. That means when you set some data, you sets may not be ordered as your data
print("--------")
# We can use sets in for loops
for i in set(d[0]) :
    print(i)
print("As you can see, letters  each letters are here but dont come in to queue111 ")
print("---------")
# We cant go to indexes of sets but if we need to go indexes of a set, we can convert it to list with list command.
# Let's look at the methods of sets
# add method adds element in set. If same element id added in a sets there will be no change.
set1 = {1,2,3,4,5,"a","b","c"}
print(set1)
set1.add(10)
set1.add("f")
set1.add(4) # because of 4 has already exist in set1 there will be no change.
print(set1)
# add method takes 1 parameter. In same time you can add only one elemnet to set. It means that set1.add(12,"ada",78) will not run.
print("----------------------")
# Now we look difference method. It gives as in the math, difference of sets according to usage. Examples explain more.
# difference method does not change the sets. It only returns differences.
# If you want to uptade your sets with differences you can use next method down below.
set2 = {1,2,3,4,5,6,7,8,9}
set3 = {-3,-12,0,1,4,7,46,9}
print(set2.difference(set3)) # it gives elements of set2 which are not exist in set3
print(set3.difference(set2)) # it gives elements of set3 which are not exist in set2
print("----------------")
# Now we look at difference_uptade() method.
# As we said above, this methods returns differences of set4 from set5 and updates the set4 with this output
# Let^s look at the examples
set4 = {1,2,3,4,5,6,7,8,9}
set5 = {-3,-12,0,1,4,7,46,9}
print("This is set4:",set4)
print("This is difference of set4 from set5",set4.difference(set5))
set4.difference_update(set5)
print("This is new set4:",set4)
# Abonove example explains this method.
print("----------------")
# Now lets look at the discard method. It helps you for subtract an element from a set.
# If given element does not exist in selected set, nothing will be cahnged. Program does not gives error
# discard method can take o parameter. If you try to discard more than one element in same time you'll get error
# that is; discard() takes exactly one argument (2 given)
print("discard method;")
set6 = {1,2,3,4,5,"asd"}
set6.discard(3) # 3 will be discarded
set6.discard(120) # 120 does not exist in set so nothing will change
print("New set6 is:",set6)
print("----------------------")
# Now lets look at the intersection method
# This method gives intersection of  two sets
set7 = {1,2,3,45,"a","final"}
set8 = {94,392,"Python","b",1,4,6,45}
print(set7.intersection(set8))
print(set8.intersection(set7))
# The point is intersection so 2 code above will return same output.
print("-----------")
# Just as difference_uptade method there is intersection_uptade method.
set9 = {1,2,3,4,5,6,7,8,9}
set10 = {-3,-12,0,1,4,7,46,9}
print("This is set9:",set9)
print("This is intercestion with set9 and set10",set9.intersection(set10))
set9.intersection_update(set10)
print("This is new set9:",set9)
# Abonove example explains this method.
print("-------------------------")
## Now it time to isdisjoint method. it look are sets disjoint or not. According to result it returns True or False.
print("isdisjoing method;\n")
set11 = {2,4,6,8,10}
set12 = {1,3,5,7,9,11}
set13 = {1,2,3,4,5,6}
print(set11.isdisjoint(set12))
print(set12.isdisjoint(set11))
print(set12.isdisjoint(set13))
print(set11.isdisjoint(set13))
print("---------------")
# issubset method give true of false according to is one of set subset of other set
print("issubset method \n")
set14 = {1,2,3,4,5,6,7,8,9,10}
set15 = {3,5,7,9}
print(set14.issubset(set15)) # False
print(set15.issubset(set14)) # True
# As you see in the output, set 15 is subset of set14 but vice versa situtation is False
print("----------")
# union method gives union of 2 sets
print("union method; \n")
set16 = {1,2,3,4}
set17 = {1,2,-1,-3,-4,132}
print(set16.union(set17))
print(set17.union(set16))
# these two line gives same output.
print("---------")
#uptade method returns union of two sets as first set
print("update method; \n")
set18 = {1,3,6,9,35}
set19 = {"af","klmghş",36,7435,1}
print(set18.update(set19)) # ! This returns "None". There is no need to print update method. uptade method do works and convert sets.
# then you can directly print sets
set18.update(set19)
set19.update(set18)
print(set18)
print(set19) # it is like a+b=b+a

# --- The End --- #




