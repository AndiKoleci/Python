from time import sleep
from random import randint

inventory = ["Sword", "Health Potion", "Gold", "Secret Symbol"]
gold = 50
health = 35
zone = "here"
complet = []
iteme = 0
spider_bool = False


def combat2():
    fighters = ["Goblin", "Orc", "FocaVIP"]
    inamic = fighters[randint(0, 2)]
    print("A wild {} appeared!".format(inamic))
    print(inamic)


def move2():
    global gold
    global health
    global zone
    global complet
    global iteme
    global spider_bool
    x = input("Where? 'g' for garden, 'd' for door, 's' for spiderwebs or 'n' to go back.")
    if x == "d":
        for items in inventory:
            if items == "Strange Key":
                sleep(1)
                print("The door opens.")
                inventory.remove("Strange Key")
                print("You are in a dark room. Everything seems vanished.")
                zone = "inRoom"
                action2()
        if zone != "inRoom":
            sleep(1)
            print("The door is locked.")
            action2()

    elif x == "s":
        if spider_bool == False:
            print("You remove some spiderwebs from the door and enter the room")
            print("You see a hole in the wall. Its shape resembles the one of a bird.")
            spider_bool = True
            action2()
        else:
            print("You are in the 'spiders' room")
            print("You are very focused on that missing piece on the wall...")
            action2()
        for items in inventory:
            if items == "Red Ruby":
                print(" . . . . . . . . . . .")
                sleep(1)
                print(" . . . . . . . . . . .")
                sleep(1)
                print("It's like the time stopped. You can't feel anything for a second")
                print("Suddenly, a trap door opens right under your feet!")
                sleep(2)
                print("You fall unconscious...")
                sleep(1)
                print("W H A T  I S  H A P P E N I N G ? ? ? ? ? ? ? ?")
                return
        action(2)

    elif x == "g":
        print("You are in a small garden. You see a person sleeping on a chair")
        print("Suddenly, he wakes up and attacks!")
        combat2()
        action2()

    else:
        print("Invalid command. Try again.")
        action2()


def action2():
    global gold
    global health
    global zone
    global complet
    global iteme
    x = input("Move? or open Inventory? 'm', or 'i'.")
    if x == "m":
        sleep(1)
        move2()
    elif x == "i":
        for items in inventory:
            print(items)
        y = input("What do you want to use? Enter the first letter of the word(s), or 'n' to go back")
        if y == "n":
            sleep(1)
            action2()
        elif y == "g":
            sleep(1)
            print("You have {} gold.".format(gold))
            action(2)
        elif y == "hp" and len(inventory) == 2:
            sleep(1)
            health += 15
            print("Now you have {} HP!".format(health))
            sleep(1)
            inventory.remove("Health Potion")
            action(2)
        else:
            print("Invalid command. Try again.")
            action2()
    else:
        print("Invalid command. Try again.")
        action2()


def move1():
    global gold
    global health
    global zone
    global complet
    if len(complet) == 0:
        y = input("Where? 'c' for chest, 's' for shiny objects, 'd' for dagger or 'n' to go back.")
    elif len(complet) == 1:
        for zones in complet:
            if zones == "dagger":
                y = input("Where? 'c' for chest, 's' for shiny objects or 'n' to go back.")
            elif zones == "shiny":
                y = input("Where? 'c' for chest, 'd' for dagger or 'n' to go back.")
    elif len(complet) == 2:
        y = input("Where? 'c' for chest or 'n' to go back.")
    if y == "c":
        sleep(1)
        print("You are in front of the chest.")
        sleep(1)
        zone = "chest"
        action1()
    elif y == "s":
        sleep(1)
        z = input("Take the shiny objects? 'y' or 'n'.")
        zone = "shiny"
        if z == "y":
            sleep(1)
            gold += 50
            print("You received 50 gold coins. Now you have {} gold coins!".format(gold))
            complet.append("shiny")
            sleep(1)
            action1()
        elif z == "n":
            sleep(1)
            action1()
        else:
            print("Invalid command. Try again.")
            action1()
    elif y == "d":
        sleep(1)
        z = input("Take the dagger? 'y' or 'n'.")
        zone = "dagger"
        if z == "y":
            sleep(1)
            print("You received a golden dagger.")
            sleep(1)
            inventory.append("Dagger")
            complet.append("dagger")
            action1()
        elif z == "n":
            sleep(1)
            action1()
        else:
            print("Invalid command. Try again.")
            action1()
    else:
        print("Invalid command. Try again.")
        action1()


def action1():
    global zone
    global health
    global gold
    global iteme
    if iteme == 3:
        sleep(1)
        print("Now you are ready to fight! Good luck, champion... You will need it.")
        return
    x = input("What do you want to do? Press 'm' to move, or 'i' for inventory.")
    if x == "m":
        sleep(1)
        move1()
    elif x == "i":
        sleep(1)
        for items in inventory:
            print(items)
        sleep(1)
        a = input("What do you want to use? Type the first letter of the word(s), or 'n' to go back.")
        if a == "s":
            sleep(1)
            print("You equip the sword.")
            iteme += 1
            sleep(1)
            inventory.remove("Sword")
            action1()
        elif a == "hp":
            sleep(1)
            health += 15
            print("Now you have {} HP!".format(health))
            sleep(1)
            inventory.remove("Health Potion")
            action1()
        elif a == "g":
            sleep(1)
            print("You have {} gold.".format(gold))
            sleep(1)
            action1()
        elif a == "ss":
            sleep(1)
            if zone == "chest":
                sleep(1)
                print("The secret symbol opens the chest. You recieve a Chainmail!")
                sleep(1)
                inventory.remove("Secret Symbol")
                inventory.append("Chainmail")
                action1()
            else:
                sleep(1)
                print("Nothing happens.")
                sleep(1)
                action1()

        elif a == "d":
            sleep(1)
            print("You equip the dagger.")
            iteme += 1
            sleep(1)
            inventory.remove("Dagger")
            action1()
        elif a == "c":
            sleep(1)
            print("You equip the chainmail.")
            iteme += 1
            sleep(1)
            inventory.remove("Chainmail")
            action1()
        elif a == "n":
            sleep(1)
            action1()
        else:
            print("Invalid command. Try again.")
            action1()
    else:
        print("Invalid command. Try again.")
        action1()


print("Welcome to DUNGEON SIMULATOR")
sleep(1)
print("Around you, all you see is a chest, some shiny, round objects on the floor and a dagger.")
sleep(1)
action1()
print("You suddenly get teleported to a very small, dim-lit room.")
print("In front of you there is a door")
print("To your left, there is an opened door, leading outside")
print("To your right, you see a door covered in spider webs")
action2()