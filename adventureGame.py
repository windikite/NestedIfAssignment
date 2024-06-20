import random

#Task 1

# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action == "climb a tree":
#         print("You found a bird's nest!")
#     elif action == "cross a river":
#         print("You found a boat!")
# elif place == "cave":
#     print("You find a hidden treasure!")

#Task 2 ----------------------------------------------------------------------------------------

# print("Choose a place: \n(1) Go foraging in the forest \n(2) Go spelunking in the cave ")
# place = int(input("Choice: "))
# if place == 1:
#     print("(1) Climb tree \n(2) Cross river")
#     choice = int(input("Choice: "))
#     if choice == 1:
#         print("You found a bird's nest!")
#     elif choice == 2:
#         print("You found a boat!")
# elif place == 2:
#     print("It's dark! \n(1) Light a torch \n(2) Proceed in the dark")
#     choice = int(input("Choice: "))
#     if choice == 1:
#         print("You see multiple crevices, which do you search? Crevice 1, 2 or 3?")
#         location = random.randrange(1, 3)
#         choice = int(input("Choice: "))
#         if choice == location:
#             print("You find a hidden treasure!")
#         else:
#             print("The crevice explodes! You died!")
#     elif choice == 2:
#         print("You see three shadowy crevices, but one has a slight glimmer! \n(1) Check glimmering crevice \n(2) Check dark crevice \n(3) Check darker crevice \n(4) Leave cave and go home")
#         choice = int(input("Choice: "))
#         if choice == 1:
#             print("You find a hidden treasure!")
#         elif choice == 4:
#             print("At least you lived!")
#         elif choice == 2 or choice == 3:
#             print("The crevice explodes! You died!")

#Task 3 ----------------------------------------------------------------------------------------

print("Choose a place: \n(1) Go foraging in the forest \n(2) Go spelunking in the cave ")
place = int(input("Choice: "))
if place == 1:
    print("(1) Climb tree \n(2) Cross river")
    choice = int(input("Choice: "))
    if choice == 1:
        print("You found a bird's nest!")
    elif choice == 2:
        print("You found a boat!")
    else:
        print("Improper choice!")
elif place == 2:
    print("It's dark! \n(1) Light a torch \n(2) Proceed in the dark")
    choice = int(input("Choice: "))
    if choice == 1:
        print("You see multiple crevices, which do you search? Crevice 1, 2 or 3?")
        location = random.randrange(1, 3)
        choice = int(input("Choice: "))
        if choice == location:
            print("You find a hidden treasure!")
        else:
            print("The crevice explodes! You died!")
    elif choice == 2:
        print("You see three shadowy crevices, but one has a slight glimmer! \n(1) Check glimmering crevice \n(2) Check dark crevice \n(3) Check darker crevice \n(4) Leave cave and go home")
        choice = int(input("Choice: "))
        if choice == 1:
            print("You find a hidden treasure!")
        elif choice == 4:
            print("At least you lived!")
        elif choice == 2 or choice == 3:
            print("The crevice explodes! You died!")
        else:
            print("Improper choice!")
    else:
        print("Improper choice!")
else:
    print("Improper choice!")