while True:
    dice = int(input("Roll the dice! (type 0 to end the game)\n"))

    while dice == 6:
        print("You can walk 6 steps ahead!")
        dice = int(input("Roll the dice again!\n"))

    if dice > 6:
        print("The number must be between 1 and 6 !")

    if dice == 1 or dice == 2 or dice == 3 or dice == 4 or dice == 5 or dice == 6:
        print("You can walk", dice,"steps ahead!")

    if dice == 0:
        break