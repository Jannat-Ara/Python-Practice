#Global Variables 
x = " a good PL."
y =" in ML."

def myfunc():
    y= " in AI."
    global z #To create a global variable inside a function, global keyword can be used.
    z = " in DL."
    print("Python is"+x)
    print("We can use it"+y)

myfunc()
print("We can use it"+y)
print("We can use it"+z)
'''
output: 
    Python is a good PL. (used as global)
    We can use it in AI. (used as local)
    We can use it in ML. (used as global)
    We can use it in DL. (by using global keyword)
'''