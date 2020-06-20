"""

Enumerate Function is like zip function but enumerate is always combining a list with [0,1,2,3,4...].
It is being used for associate each term of list with its own index

enumerate(list)

it is also required to convert list to print.

"""

# let's begin zip
list1 = list(range(0,10))
list2 = ["Muffin","Pufi","Safiş","Paşa"]
print(list(zip(list1,list2)))
print(list(enumerate(list2)))
# Outputs are same
# Let's look some more examples
print(list(enumerate([1,2,3,4,5])))
print(list(enumerate(["a","b","c","d","e","f"])))


