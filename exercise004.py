#######################################################
# This is exercise 004 for week 2                     #
#                                                     #
# This exercise is about if statements and for loops  #                                                     #
#                                                     #
# if statements allow our code to make decisions      #                                                    #
#                                                     #
# for loops let us loop through ranges & collections  #
#                                                     #
#######################################################

###### Examples ######

a = 3
b = 10

if a < b: # This is the condition - the condition can only ever be true or false
    # if the condition is true this code runs
    print (a , "is less than", b)

# we can test multiple conditions

c = 5
d = 4

if c < d:
    print (c, "is less than", d)
elif c == d:
    print (c, "is equal to", d)
else:
    print (c, "is greater than", d)

# Try changing the value of c to 4 and then 3 and
# running the code each time. What happens?
           

# We can compare agains the result of a calculation

e = 4

if (e % 2) == 0:
    print (e, "is an even number")
else:
    print (e, "is an odd number")

# This is a list in python
myList = ["train", "car", "bike"]

# We can loop through the list
for x in myList:
    print (x)

# We can also loop through a range
for x in range (1, 6):
    print (x)



###### Exercise ######

print ("\nYour exercises are below\n")

# Exercise 004a
print ("\nExercise 0004a\n")

# Print 0 to 9 using a for loop
for x in range(10):
    print(x)


# Exercise 004b
print ("\nExercise 0004b\n")

# Print out a 12 times table using a for loop
# For example
# 0 x 12 = 0
# 1 x 12 = 12
# ...
# 12 x 12 = 144

for x in range(12):
    print(x*12)


# Exercise 004c
print ("\nExercise 0004c\n")

# Using a for loop print out the numbers 1 to 100
# Use an if statement to replace any number divisible by 3 with the string "flip"
# HINT (x % 3) == 0

for x in range(101):
    if (x % 3) == 0:
        print("flip")
    else:
        print(x)

# Exercise 004d
print ("\nExercise 0004d\n")

# Using your code from 004c above
# replace any number divisible by 5 with the string "flop"

for x in range(101):
    if (x % 5) == 0:
        print("flop")
    else:
        print(x)

# Exercise 004e
print ("\nExercise 0004e\n")

# Using your code from 004d above
# replace any number divisible by 5 and 3 with the string "flipflop"


for x in range(101):
    if (x % 3) == 0:
        print("flipflop")
    elif (x % 5) == 0:
        print("flipflop")
    else:
        print(x)





