import random

pc_number = random.randint(0,20)
i = 1
while i<21:
    user_number = int(input("Enter a number:"))

    if user_number == pc_number:
        print("YEAH!")
        break

    if user_number < pc_number:
        print("Enter a bigger number")

    if user_number > pc_number:
        print("Enter a smaller number")

    i+=1

print("The number was", pc_number)
print("You have tried",i,"times")