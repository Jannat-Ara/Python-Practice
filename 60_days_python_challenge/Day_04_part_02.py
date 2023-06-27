#Python Strings

print(' He said, " I want to eat an apple.')
print( "He said, \"I want to eat an apple.")

#multiline

receipe ="""
1. Heat the pain and oil
2. Crack the egg
3. Add salt in egg and mix well
4. Pour the mixture in pain
5. Fry on medium heat
"""
print(receipe)

note="""
This is a multiline string.
It is used to display multiline message in the program.
"""
print(note)

# Strings in Python are arrays of bytes representing unicode characters.
#Python does not have a character data type, a single character is simply a string with a length of 1.
array = "Hello, World!"
print(array[0]) #output: H

#Looping through a string
for x in "Strawberry":
    print(x)

'''
output: 
S
t
r
a
w
b
e
r
r
y
'''
alphabets = "ABCDE"
for i in alphabets:
    print(i)
'''
output:
A
B
C
D
E
'''

#Length of a string:  We can find the length of a string using len() function.
fruit= "Mango"
len1 = len(fruit)
print("Mango is a", len1,"letter word.")#output: Mango is a 5 letter word.

#check String $ Check if NOT
# To check if a certain phrase or character is present in a string, we can use the keyword in.

text ="The best thing is life are free!"
print("free" in text) #Output come as bool data type.

if " free" in text:
    print("Yes, 'free' is present in the text.")

print("NOT" not in text)

if "Expensive" not in text:
    print("No, 'Expensive'is NOT present.")