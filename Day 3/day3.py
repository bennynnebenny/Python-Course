# print("Welcome to the Roller Coaster!")
# height = int(input("What is your height in cm?\n"))

# bill = 0

# if height < 120:
#     print("You can't enter!")
# else:
#     age = int(input("Sure, you can play. But how old are you?\n"))

#     if age < 12:
#         bill += 5
#         print("Your ticket price will be $5")
#     elif age >= 12 and age <= 18:
#         bill += 7
#         print("Your ticket price will be $7")
#     else:
#         bill += 12
#         print("Your ticket price will be $12")

#     wants_photo = input("Do you want to have a photo? Type \"y\" for Yes and \"n\" for No")

#     if wants_photo == "y":
#         bill += 3
#         print(f"The total bill will be at ${bill}")
#     else:
#         print(f"The total bill will be at ${bill}")

# print("Welcome to Python Pizza Deliveries!")

# bill = 0
# pizza_size = input("Which size of pizza do you want? Choose between Small (S), Medium (M), Large (L)\n")
# add_peperoni = input("Would you like to add peperoni on your pizza? Choose \"y\" for Yes and \"n\" for No\n")
# add_cheese = input("Would you like to add extra cheese on your pizza? Choose \"y\" for Yes and \"n\" for No\n")

# if pizza_size == "S" or pizza_size == "s":
#     bill += 15
#     if add_peperoni == "y":
#         bill += 2
#     if add_cheese == "y":
#         bill += 1
# elif pizza_size == "M" or pizza_size == "m":
#     bill += 20
#     if add_peperoni == "y":
#         bill += 3
#     if add_cheese == "y":
#         bill += 1
# elif pizza_size == "L" or pizza_size == "l":
#     bill += 25
#     if add_peperoni == "y":
#         bill += 3
#     if add_cheese == "y":
#         bill += 1
# else:
#     print("Please input the correct size of Pizza!")

# print(f"Your total bill will be ${bill}")

# print("Welcome to Treasure Island. Your mission is to find the treasure.")
# print("Your mission is to find the treasure")
# directions = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

# if directions == "right":
#     print("You fell in to a hole. Game Over!")
# elif directions == "left":
#     swim = input("You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for boat. Type \"swim\" to swim across.\n").lower()

#     if swim == "swim":
#         print("You got attacked by an angry trout!. Game Over!")
#     elif swim == "wait":
#         choose_door = input("You arrived at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

#         if choose_door == "red":
#             print("It's a room full of fire. Game Over!")
#         elif choose_door == "blue":
#             print("You enter room full of beasts. Game Over!")
#         elif choose_door == "yellow":
#             print("You found the treasure. You win!")
#         else:
#             print("You choose a door that doesn't exist. Game Over!")
#     else:
#         print("Please choose the available choice given")
# else:
#     print("Please choose the available choice given")