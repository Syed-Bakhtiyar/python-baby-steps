# Conditions

x = 2
print x == 2 # prints out True
print x == 3 # prints out False
print x < 3  # prints out True


# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print "Your name is John, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick."


# "in" Operator
if name in ["John", "Rick"]:
    print "Your name is either John or Rick."

# if elseif else

"""
if <statement is true>:
    <do something>
elif <another statement is true>: # else if
    <do something else>
else:
    <do another thing>
"""


# 'is' operator
x = [1,2,3]
y = [1,2,3]
print x == y # Prints out True
print x is y # Prints out False


# "not" operator
print not False # Prints out True
print (not False) == (False) # Prints out False
