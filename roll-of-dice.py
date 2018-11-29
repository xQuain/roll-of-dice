#Roll of dice
#Generating random numbers

import random

#Generate randoms number between 1-6

roll = random.randint(1,6)
roll2 = random.randint(1,6)

total = roll + roll2

print("You rolled a", roll, "and a", roll2, "for a total of", total)
