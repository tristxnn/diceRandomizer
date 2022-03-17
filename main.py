import random
import time
print("\nRandom Dice Roll!")
print("")
cont = input("Would you like to roll the dice? Y/N: ").lower()

while cont == "y" or cont == "n":
    if cont == "y":
        print(int(random.randint(1, 6)), "is the number the dice has landed on! \n")
    elif cont == "n" or cont == "N":
        break
    time.sleep(0.55)
    repeat = input("Would you like to roll the dice? Y/N: ").lower()
else:
    raise Exception("Invalid entry!")