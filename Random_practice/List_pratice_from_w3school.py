#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#['apple', 'banana', 'watermelon', 'cherry']


# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)#['apple', 'watermelon']


# Append Items
# To add an item to the end of the list, use the append()method:
thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist) #['apple', 'banana', 'cherry', 'orange']


#Insert Items
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)#'apple', 'orange', 'banana', 'cherry']


#Extend List
#To append elements from another list to the current list, use the extend() method.
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)#['apple', 'banana', 'cherry', 'kiwi', 'orange'] 

