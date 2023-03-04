course = 'Python for beginners'
print(len(course)) # gonna print the length of the string
print(course.upper()) #PYTHON FOR BEGINNERS
print(course.lower()) #python for beginners
print(course.find('P')) #0 (casesensative)
print(course.replace("beginners","absolute beginners.")) #Python for absolute beginners.(casesensative)
print('Python' in course) #True(casesensative) in return boolean value like do we have the element or not.
print('python' in course) #False(casesensative)
print(course.title()) #Python For Beginners [returns a string where the first character in every word is upper-case.]






#N.B.:This function upper is using for converting the string into upper case, now more accurately because this function is specific to string, we reger to this as a method. In contrast len and print are general purpose functions, they don't belong to strings or numbers or other kinds of objects. This is the difference between methods and functions.