number = [2, 2,3,3, 1, 5, 6, 8, 8]
unique = []

for num in number:
    if num not in unique:
        unique.append(num)

print(unique)#[2, 3, 1, 5, 6, 8]
unique.sort()
print(unique)#[1, 2, 3, 5, 6, 8]
unique.reverse()
print(unique)