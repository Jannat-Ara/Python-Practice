'''
Total task which I am gonna execute:
    IF it's hot 
        It's a hot day
        Drink plenty of water
    otherwise if it's cold
        It's a cold day
        Wear warm clothes
    otherwise 
        It's a lovely day.

'''
is_hot = False
is_cold =True
if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day.")


'''Exercise:

Price of a house is $1M
IF byer has good credit
    they need to put down 10%
Otherwise 
    they need to put down 20%

print the down payment
'''

price_of_house = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price_of_house*0.1
else:
    down_payment = price_of_house*0.2

print(f'Down Payment: ${down_payment}')