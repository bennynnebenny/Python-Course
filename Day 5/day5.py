import random

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)

# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Easy version
# password = ""

# password_letters = int(input("How many letters world you like in your password?\n"))
# password_symbols = int(input("How many symbols would you like?\n"))
# password_numbers = int(input("How many numbers would you like?\n"))

# for i in range(0, password_letters):
#     password = password + random.choice(letters)

# for i in range(0, password_symbols):
#     password = password + random.choice(symbols)

# for i in range(0, password_numbers):
#     password = password + random.choice(numbers)

# print(password)

# Hard Version
# password = []
# final_password = ""

# password_letters = int(input("How many letters world you like in your password?\n"))
# password_symbols = int(input("How many symbols would you like?\n"))
# password_numbers = int(input("How many numbers would you like?\n"))

# for i in range(0, password_letters):
#     password.append(random.choice(letters))

# for i in range(0, password_symbols):
#     password.append(random.choice(symbols))

# for i in range(0, password_numbers):
#     password.append(random.choice(numbers))

# Caraku sendiri
# total_character = password_letters + password_numbers + password_symbols

# for i in range(0, total_character):
#     random_character =  random.choice(password)
#     final_password += random_character
#     password.remove(random_character)

# Dari Udemy
# random.shuffle(password)

# for character in password:
#     final_password += character

# print(final_password)