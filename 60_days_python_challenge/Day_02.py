#list are mutable and can be modified after creation

list = [8, 2.3 ,[-4,5], ["apple", "banana"]]
print(list) #output: [8, 2.3, [-4, 5], ['apple', 'banana']]

#tuples are immutable and can not be modified after creation.

tuple = (("parrot", "sparrow"),("Lion", "Tiger"))
print(tuple) #output:(('parrot', 'sparrow'), ('Lion', 'Tiger'))


#Range:
sequence = range(4, 14, 2)
for i in sequence:
    print(i)


#dictionary:

dict = {"name":"Raya", "age":24, "canVote":True}
print(dict) #output: {'name': 'Raya', 'age': 24, 'canVote': True}