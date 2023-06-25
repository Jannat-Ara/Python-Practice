#Python numeric types & type conversion 

num = 5j
print(num) #output: 5j
print (complex(num)) #output:5j

num1 = 25.0 
print (num1) #output: 25.0
print(complex(num1)) #output:(25+0j)


#Random number

# Python does not have a random() function to make a random number, but python has a built-in module called random that can be  used to make random numbers:

import random 
print( random.randrange( 5, 10)) # output: randomly picked 7


#type casting

a ="1"
b ="2"

print(int(a)+int(b))