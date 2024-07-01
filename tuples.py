# tuples are like arrays but immutable, we can index them but can't modify them
# to initialize them, we use parenthesis instead of brackets

tup=(1,2,3)
print(tup[2])
tup[0]=4 #can't modify the values
print(tup)


#mainly used as keys for a hashmap or hashset
myMap={(1,2):3}   #this tuple is our hashable key
print(myMap[(1,2)])

mySet=set()
mySet.add((1,2))
print((1,2) in mySet)

#because lists are not hashable and cannot be keys in hashmaps or hashsets
myMap[[3,4]]=5
