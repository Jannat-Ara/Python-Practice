#python_modify_Strings
#Strip(): THe strip() method removes any whitespace from the beginning or the end.

a =" Hello, World! "
print(a.strip())

#String Format
age = 36
'''text = " My name is John, I am "+age
print(txt)
Its giving me error.
'''

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
txt = "My name is John, and I am {}."
print(txt.format(age))


# The format() method can take unlimited number of arguments
quantity = 3
item_no = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollar."
print(myorder.format(quantity, item_no, price)) #I want 3 pieces of item 567 for 49.95 dollar.
# We can use index numbers {0} to be sure the arguments are placed in the correct placeholders.
myorder1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder1.format(quantity, item_no, price)) #I want to pay 49.95 dollars for 3 pieces of item 567.
myorder1 = "I want to pay {:.2f} dollars for {} pieces of item {}."
print(myorder1.format(quantity, item_no, price)) #I want to pay 3.00 dollars for 567 pieces of item 49.95.
myorder = "I want {0} pieces of item number {1} for {2:.1f} dollars."
print(myorder.format(quantity, item_no, price))#I want 3 pieces of item number 567 for 50.0 dollars.


mycar = "I have a {carname}, it is a {model}."
print(mycar.format(carname="Ford", model="Mustang"))#I have a Ford, it is a Mustang.
