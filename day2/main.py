total = float(input('What is the bill total? $'))
tip = int(input('How much would you like to tip? 10 15 20? '))
bill_w_tip = tip / 100 * total + total

print(bill_w_tip)