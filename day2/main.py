total = float(input('What is the bill total? $'))
tip = int(input('How much would you like to tip? 10 15 20?\n (do not add % sign) '))
bill_w_tip = tip / 100 * total + total

print(f'Your total bill including tip will be:\n ${bill_w_tip:.2f}')