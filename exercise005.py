#######################################################
# This is exercise 005 for week 2                     #
#                                                     #
# In this exercise you need to write a short program  #
#                                                     #
#######################################################





# Write a program to display a menu like the following

#   1. Play a game
#   2. Add some numbers
#   3. Solve a problem
#   4. Rename a file
#   Q. Quit

# Write some code to ask the user to choose an option (1, 2, 3, 4 or Q)
# HINT: x = input("User Message")

# Now write some code to check that the user input is one of the options

# Hint: Create a list of the options

# Hint: use an if statement to check if the input is in the list you created.

# If the user did not select a valid option print out a message to tell them

opts =["1. Play a game", "2. Add some numbers", "3. Solve a problem", "4. Rename a file", "Q. Quit"]



opt1="1. Play a game"
opt2="2. Add some numbers"
opt3="3. Solve a problem"
opt4="4. Rename a file"
quitt="Q. Quit"


for i in opts:
    print(i)
choise = str(input("you selected: "))

# if choise.lower() != "q":
choise=choise.upper()
try:
    # choise = int(choise)
    # check(choise)
    if choise in opt1:
        print(opt1)
    elif choise in opt2:
        print(opt2)
    elif choise in opt3:
        print(opt3)
    elif choise in opt4:
        print(opt4)
    elif choise in quitt:
        print(quitt)
    else:
        print("check input please")
except:
    print ("input malformed please check your entry")


