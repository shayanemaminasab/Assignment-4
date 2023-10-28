import random

while True:
    dice = random.randint(1,6)

    while dice == 6:
        print("Your dice is 6")
        print("You can walk 6 steps ahead and roll the dice again!")
        dice = random.randint(1,6)

    if dice == 1 or dice == 2 or dice == 3 or dice == 4 or dice == 5:
        print("Your dice is", dice)
        print("You can walk", dice,"steps ahead!")
        break