print('Welcome to the Tip Calculator !\n\n\n')
total = float(input('What is the bill total? $'))
tip_per = int(
    input('How much would you like to tip? 10 15 20?\n (do not add % sign) '))
bill_w_tip = (tip_per / 100 * total) + total

other_diners = ['yes', 'no']


def question_for_people():
    for x in other_diners:
        print(x)


print(f'Your total bill including tip will be:\n ${bill_w_tip:.2f}')
# print(question_for_people())
