#Based on a list of fruits, you want  a new list, containing  only the fruits with the letter "a" in the name
fruits=['apple','banana','cherry','Kiwi','mango']
newlist= []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)#['apple', 'banana', 'mango']

#find it different

newlist1=['hola!' for x in fruits]
print(newlist1)#['hola!', 'hola!', 'hola!', 'hola!', 'hola!']