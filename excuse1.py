# We want to make some random selections
# so we need to import the random module.
# More on Python modules next week.
import random

# These are the three lists

quantity = [
    'like, a million',
    'loads and loads of',
    'a bunch of',
    'four score and ten',
    'literally a ton of']

item = [
    'Time Lords',
    'aliens',
    'Wombles',
    'bananas',
    'emo kids']

location = [
    'in the house',
    'by my breakfast',
    'on the table',
    'by my car']

# We will make our random selections first

randomQuantity = random.choice (quantity)
randomItem = random.choice (item)
randomLocation = random.choice (location)

# Then we print it all out

print ("I'm sorry I'm late but there were", randomQuantity, randomItem, randomLocation)


