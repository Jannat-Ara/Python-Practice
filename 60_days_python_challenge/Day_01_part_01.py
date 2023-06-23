#comments, Escape Secquences and print Statement
#Escape Sequence Characters:
# An escape sequence character is a backslash \ followed by the charachter you want to internet.
# \n used to create new line.

print("Hey I am a good girl \nand this viewer is a good boy/girl")
'''output: Hey I am a good girl 
        and this viewer is a good boy/girl'''
print("Hey I am a \"good girl\" \nand this viewer is a good boy/girl")
'''output: Hey I am a "good girl" 
        and this viewer is a good boy/girl'''

# In the print Statement we can give multiple values
print("hey", 6, 7) #output: hey 6 7
print("hey", 6, 7, sep="~") #output: hey~6~7
print("hey", 6, 7, sep="~", end ="009\n") #end = Specify what to print at the end. Default is '\n'. Output:hey~6~7009