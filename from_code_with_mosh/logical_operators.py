'''If applicant has high income 
            AND 
    good credit Eligible for loan
'''
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan") #gonna print only if both are true


has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan") #gonna print any way only one need to be true

#Exercise
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g:')  

if unit.upper()=='L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight/0.45
    print(f"You are {converted} pound")