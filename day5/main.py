import random
print('Welcome to the PyPassword Generator:\n\n')

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
upper_letters= [letter.upper() for letter in letters]
numbers= [0,1,2,3,4,5,6,7,8,9]

letters_choice = int(input("How many letters would you like in your password?\n"))
upper_choice = int(input("Would you like uppercase letters? Type 1 for Yes and 2 for No\n"))
if upper_choice == 1:
    num_upper = int(input("How many uppercase letters would you like?\n"))
symbols_choice = int(input("How many symbols would you like?\n"))
nums_choice = int(input("How many numbers would you like?\n"))


random_password = []

for char in range(0, letters_choice):
    random_password.append(random.choice(letters))

for char in range(0, symbols_choice):
    random_password.append(random.choice(symbols))

for char in range(0, nums_choice):
    random_password.append(random.choice(numbers))

if upper_choice == 1:
    for char in range(0, num_upper):
        random_password.append(random.choice(upper_letters))

random.shuffle(random_password)
result = "".join(map(str,random_password))
print(f"Your password is: {result}")