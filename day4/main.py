import random

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices for easy access
choices = [rock, paper, scissors]

# Get user choice
user_choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n2"))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You lose!")
else:
    # Get computer choice
    computer_choice = random.randint(0, 2)

    # Display the choices
    print("\nYou chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[computer_choice])

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
