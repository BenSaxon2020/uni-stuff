#######################################################
# This is exercise 001 for week 1                     #
#                                                     #
# This exercise is about the print statement          #                                                     #
#                                                     #
# Whatever we want to print goes between brackets ()  #
#                                                     #
# print (stuff to print goes here)                    #
#                                                     #
#######################################################



# This is a basic print statement <- And this is a comment
print ("Hello World!")

print ("This # is a hash symbol")

print ("Here is a longer line of text. What if we want it to display on two lines?")

print ("Here is a longer line of text. \nWhat if we want it to display on two lines?")

# What if we want to print out \n?
# We escape the escape character with \\n
print ("We use \\n to print this out")

# What if we do not want a new line after each print statement?
print ("This is the first print statement. ", end='')
print ("This is the second print statement. ", end='')
print ("This is the third print statement. ")
print ("\n\n\tHere is a line of text that has two blank lines and a tab.")

# We can print numbers too - NOTE there are no quotes ""
print (7)

# We can print out the results of calculations too
print (4 + 5)

###### Exercise ######

print ("Your exercises are below\n")

# Exercise 001a
print ("\nExercise 0001a\n")
# Print out the text 'Hello, My name is Philip'
# Change "Philip" to your name
print ("hell, my name is ben")
# Exercise 001b
print ("\nExercise 0001b\n")
# Print out the following on three lines using one print statement
# "This is line 1. This is line 2. This is line 3"
print("This is line 1.")
print("This is line 2.")
print("This is line 3")


# Exercise 001c
print ("\nExercise 0001c\n")
# Write code to print out the following
# He said "It's all about timing"
print(''' He said "It's all about timing" ''')

# Exercise 001d
print ("\nExercise 0001d\n")
# Uncomment the following two lines

print (4 + 7)
print ("four" + "seven")

# Write a comment here to explain what happens.
#adds the intigers 4+7 then prints the sum
# add the strings four and seven together with no space

# Exercise 001e
print ("\nExercise 0001e\n")

# Write code to print a menu that looks like the following

#       #####################
#       # 1 Play a game     #
#       # 2 Do some maths   #
#       # 3 Draw a picture  #
#       # Q Quit            #
#       #####################



opts =["1. Play a game", "2. Add some numbers", "3. Solve a problem", "4. Rename a file", "Q. Quit"]
for i in opts:
    print(i)