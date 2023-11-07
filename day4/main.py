import random
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

user_choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, 2 for scissors."))
computer_choice= random.randint(0,2)
print(f"Computer chose: {computer_choice}")

if computer_choice == 0 and user_choice == 1:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
else : 
    print("Tie")