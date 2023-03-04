course= 'Python for "Beginners"'
print (course)

#multiline String

multiline = '''
Hi there,

Here we are sending you the first email.
Thank you for your support.
The Supporting Team.
'''
print(multiline)

#printing charachters
course = 'Python for beginners'
print(course[-2])# gonna print r from the end
print(course[-1])# gonna print s from the end

print(course[0:3])# gonna print charachters starting from 0 index all the way to 3 but it's gonna exclude index 3.
print(course[:])# gonna print everything

another = course[:]#just copying the whole thing to another

#assignment

name = 'Jennifer'
print(name[1:-1]) # gonna print (e to r). Nope! I was wrong. It printed e to e as -1 will be excluded. Be Carefull!