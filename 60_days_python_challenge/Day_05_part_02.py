#Python Boolean 
# There are not many values that evaluate to False, except empty values, such as (),[],{}, the number 0, and the value None. 
print(bool(False))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))


#Example: 01
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))#False

#Example: 02
def myFunction():
    return True

if myFunction():
    print("YES!")
else: 
    print("NO!")

#Example: 03
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x =200
print(isinstance(x,int)) #True