import random 

# friends = ["Benny", "Riko", "Raken", "Geo"]


# # random_number = random.randint(0, 3)

# print(random.choice(friends))

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print("\n\nYour choice is")

if choice == 0:
    print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')
    print("\n\nComputer choice is")
    if computer_choice == 0:
        print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')
        print("Draw")
    elif computer_choice == 1:
        print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
''')
        print("You lose!")
    else:
        print('''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
        print("You win!")
elif choice == 1:
    print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
''')
    print("\n\nComputer choice is")
    if computer_choice == 0:
        print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')
        print("You win")
    elif computer_choice == 1:
        print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
''')
        print("Draw!")
    else:
        print('''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
        print("You lose!")
elif choice == 2:
    print('''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
    print("\n\nComputer choice is")
    if computer_choice == 0:
        print('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')
        print("You lose!")
    elif computer_choice == 1:
        print('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
''')
        print("You win!")
    else:
        print('''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
        print("Draw")
else:
    print("Please select the correct input that available!") 