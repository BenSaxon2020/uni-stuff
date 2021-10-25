#######################################################
# This is exercise 003 for week 1                     #
#                                                     #
# This exercise is about while loops and operators    #                                                     #
#                                                     #
# Loops let us repeat code                            #
#                                                     #
#######################################################

###### Examples ######

i = 0           # This is the starting condition
while i < 3:    # This is the end condition
    print (i)
    i += 1      # This is the itterator

print ("The loop has ended.") # This is not in the loop

# We do not have to go up

c = 4
while c > 0:
    print (c)
    c -= 1

print ("The loop has ended.")

# We can iterate through the loop in different steps

iterator = 0
while iterator < 100:
    print (iterator)
    iterator += 31

print ("The loop has ended.")


###### Exercise ######

print ("\nYour exercises are below\n")

# Exercise 003a
print ("\nExercise 0003a\n")

# Write a loop to print out the numbers from 3 to 7
for i in range(3, 8):
    print(i)

# Exercise 003b
print ("\nExercise 0003b\n")

# Write a loop to print out all the even numbers between 0 and 10 inclusive
for i in range(11):
    if i % 2 == 0:
        print(i)
# Exercise 003c
print ("\nExercise 0003c\n")

# Write a loop to print out all the numbers that are divisible by three
# between 17 and 29 inclusive.
for i in range(17, 30):
    if i % 3 == 0:
        print(i)

# Exercise 003d
print ("\nExercise 0003d\n")

# Write a loop to print all the numbers from 1 to 10 in descending order
# on the same line "10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# HINT - Look back at the first exercise

for i in reversed(range(11)):
    print(i)    


# Exercise 003e
print ("\nExercise 0003e\n")

# Write a loop to calculates the sum of the numbers 1 to 100 and
# prints out the result.
count = 0
tot = 0
while (count<100):
    count+=1
    tot=tot+count
print(tot)




