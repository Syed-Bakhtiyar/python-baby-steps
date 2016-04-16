# Lists
# Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

# print by indexes
print 'list print by indexes'
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# print by for loop
print 'list print by for loop'
for x in mylist:
    print x




#Accessing an index which does not exist generates an exception (an error).

# mylist2 = [1,2,3]
# print(mylist2[10])
