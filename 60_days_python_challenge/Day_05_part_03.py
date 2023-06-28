num = input("Enter a number to identify it's range: ")
num = int(num)
if (num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10.")
    elif (num> 10 and num<20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else: 
    print("Number is zero.")

#Short Hand If
a = 18
b = 10
if a>b: print("a is greater than b.")

#Short Hand If... Else

a = 2
b = 220

print("A") if a > b else print("B")