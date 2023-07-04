row = 4
for num in range(row):
    for col in range(num+1):
        print("* ",end=" ")
    print(" ")

for num in range(row):
    for col in range(num,row):
        print("* ",end=" ")
    print(" ")


for num in range(row):
    for col in range(num, row):
        print(" ", end=" ")
    for col in range(num+1):
        print("*", end=" ")
    print()