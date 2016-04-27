# Basic String Operations

# Strings are bits of text. They can be defined as anything between quotes:

astring = "Hello world!"
astring2 = 'Hello world!'


# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
print len(astring)	# get string length


# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase - this method only recognizes the first.
print astring.index("o")


# For those of you using silly fonts, that is a lowercase L, not a number one. This counts the number of l's in the string. Therefore, it should print 3.
print astring.count("l")


# This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.
print astring[3:7]

# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
print astring[3:7:3]

# Upper and Lower Case
print astring.upper()
print astring.lower()

# This is used to determine whether the string starts with something or ends with something, respectively. The first one will print True, as the string starts with "Hello". The second one will print False, as the string certainly does not end with "asdfasdfasdf".

print astring.startswith("Hello")
print astring.endswith("asdfasdfasdf")


# split
print astring.split(" ")
