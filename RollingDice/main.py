# Dice game by display a random number


import random

print("Welcome to the dice game! ")

while True:
    number = random.randrange(1, 7)
    value = input("\npress enter to roll the dice or type stop:")
    if value == 'stop':
        print("Game is over! Byeeee")

    else:
        print("you rolled number: ", number)
