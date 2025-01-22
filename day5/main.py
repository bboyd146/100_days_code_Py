import random
print('Welcome to the PyPassword Generator:\n\n')
letters_choice = int(input("How many letters would you like in your password?\n"))
symbols_choice = int(input("How many symbols would you like?\n"))
nums_choice = int(input("How many numbers would you like?\n"))

user_choices = [letters_choice, symbols_choice, nums_choice]
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters= [letter.upper() for letter in letters]
numbers= [0,1,2,3,4,5,6,7,8,9]
print(upper_letters)