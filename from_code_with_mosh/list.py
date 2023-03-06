names =['John','Bob','Mosh','Sarah','Mary']
print(names[:4]) #['John', 'Bob', 'Mosh', 'Sarah']
print(names[:])#['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:])#['Mosh', 'Sarah', 'Mary']

#Exercise: Write a program to find the largest number in a list.
numbers = [30, 44, 1,25, 2, 72, 15, 7]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
        
print(max)

#2D list 
'''
    1 2 3
    4 5 6
    7 8 9


'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][1])# 2

print(matrix[1][2]) #6

#if you want to print all the item from a 2D matrix

for row in matrix:
    for item in row:
        print(item)