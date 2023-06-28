# Some String method (resource: https://www.codewithharry.com/tutorial/python-string-methods/)

#1. strip(): The strip() method removes any white spaces before and after the string.

string1 =" Silver Spoon"
print(string1.strip())

#2. rstrip(): The rstrip() removes any trailling characters.
string2 = "Hello !!!"
print(string2.rstrip("!")) #output: Hello

#3. split(): The split() method splits the give string at the specified intance and returns the spearated strings as list items.
string3 = "Silver Spoon"
print(string3.split(" ")) #output: ['Silver', 'Spoon']

#4.center(): The center() method aligns the string to the center as per the parameters give by the user.
string4 = "Welcome to the console!!!"
print(string4.center(50))
print(string4.center(50,"."))

#5. swapcase(): The swapcase() method changes the character casing of the string.Upper case are converted to lower case and vice versa.
string5 = "Python is a Interpreted Language."
print(string5.swapcase())# output: pYTHON IS A iNTERPRETED lANGUAGE.