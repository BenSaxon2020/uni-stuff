#######################################################
# This is exercise 002 for week 1                     #
#                                                     #
# This exercise is about variables                    #                                                     #
#                                                     #
# Variables let us store values                       #
#                                                     #
#######################################################

# Examples

name = "Fred"
age = 42
print (name)
print (age)

# We can combine variables and literals in a print statement
print (name, "is", age, "years old")

# We can manipulate variables
fullName = name + " Smith"
futureAge = age + 5

print (fullName, "will be", futureAge, "in five years.")

# Variables have a type such

aString = "this is a string"
print (type (aString))


###### Exercise ######

print ("Your exercises are below\n")

# Exercise 002a
print ("\nExercise 0002a\n")
# Create two variables to hold your first name and second name.
# You should choose sensible names for the variables
# Print out your full name using one print statement
first = "ben"
last = "saxon"
print(f"{first} {last}")


# Exercise 002b
print ("\nExercise 0002b\n")
xCoordinate = 1.3
yCoordinate = 4.7

# Write code to print out "The location is (1.3, 4.7)
print(f"{xCoordinate}, {yCoordinate}",)

# Exercise 002c
print ("\nExercise 0002c\n")
aValue = 8
bValue = 7
# Write a line of code to print out the sum of the two variables above
print(aValue+bValue)

# Exercise 002d
print ("\nExercise 0002d\n")
newString = "Hello"
anInt = 7
aFloat = 1.234
aBool = True

# Use the type() function to print out the type of each variable above in
# a proper sentence such as
# "Hello is a <class 'str'>"
print(type(newString))
print(type(anInt))
print(type(aFloat))
print(type(aBool))


# Exercise 002e
print ("\nExercise 0002e\n")
anotherString = "2"
anotherInt = 2

# Print out the type of the two variables above
# What is the difference
# Write a comment in your code to explain the difference
#anotherString is a string meaning it is text and anotherInt is an int meaning is it a number


print(type(anotherString))
print(type(anotherInt))

# Exercise 002f
print ("\nExercise 0002f\n")

# Add the two variables from the previous exercise together
# and print out the result
# HINT - You will need to cast the string to an integer
print(anotherInt+int(anotherString))