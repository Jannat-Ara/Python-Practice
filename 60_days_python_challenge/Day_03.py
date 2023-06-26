# unpack a collection

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.This is called unpacking.(source: https://www.w3schools.com/python/python_tuples_unpack.asp)

#unpack a list 
fruits = ["apple", "banana", "cherry"]

x,y,z = fruits
print(x)
print(y)
print(z)

'''
output: 
   apple
   banana
   cherry
'''

#unpacking a tuple

fruits1= ("apple","banana","cherry")
(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)

'''
output: 
   apple
   banana
   cherry
'''


#using asterisk *
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list: (source: https://www.w3schools.com/python/python_tuples_unpack.asp)

f =('apple','banana','cherry','strawberry','rasberry')
(g, y, *r)= f

print(g)
print(y)
print(r)
'''
output:
    apple
    banana
    ['cherry', 'strawberry', 'rasberry']
'''
#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left. (source: https://www.w3schools.com/python/python_tuples_unpack.asp)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

'''
output:
    apple
    ['mango', 'papaya', 'pineapple']
    cherry
'''