import random as r
gues = -1
guesses = 0

def guess():
    try:
        g = int(input("take a guess between 0 and 100: "))
        return g
    except:
         print("guess not valid try again")
         guess()



num = r.randrange(101)
# print(num)

while  gues != num:   
    guesses = guesses+1
    print("guess number: ", guesses)
    if num >= gues:
        print("higher")
    elif num <= gues:
        print("lower")
    gues = guess()

print ("correct guess welldone!")
