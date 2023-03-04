# by defining a function
def f(x):# we know y and f(x) are same
    y = 4*x + 3
    return y #returning the value of y

print(5, " \t", f(5))# here i am putting f(5) because I have not define any x yet

# Next, a loop
for x in range(11):
    print(x, " \t",f(x)) #in default manner x starts from 0