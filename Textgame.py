import time 
import math

character_Hitpoints = 0
character_Defense = 0
character_Attack = 0

print ("You are a player in a RPG game.")

def pick_Character():
    print ("Pick a Character:")
    Characters = {
        "Tank": {}
    }



print ("You wake up and look around. It is a typical day.")
time.sleep(1)
print ("What do you want to do?")
time.sleep(1)
print ("Press \"S\" to go to shop, or \"F\" to go Fight")
def Decision_1():
    while True:
        Decision1 = input("")    
        if Decision1 == "F" or Decision1 == "f":
            print ("You cannot fight yet. You do not have a weapon.")
            continue
        elif Decision1 == "S" or Decision1 == "s":
            print ("The shop includes some dank weapons. Pick one.")
            break
        else:
            print ("You didn't enter a valid option. Try again.")
            continue
Decision_1()

def Shop:
    print("Hello mate, and welcome to the shop. What can I help you with today?")
    print ("Press S to buy a sword, a to buy a bow & arrow, or b to exit the store")
    if Shop == "S" or Shop == "s":
            print ("You have bought the sword")
            continue
        elif Shop == "A" or Shop == "a":
            print ("You have bought the Bow & Arrow")
            break
        elif Shop == "B" or Shop == "b":
            print ("You have exited the store")
            break
        else:
            print ("You didn't enter a valid option. Try again.")
            continue
Shop()
