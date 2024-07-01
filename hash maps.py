#Hash Maps = dictionary in python
#it has keys and values assigned to those keys
#we can't have duplicate keys inside hash maps

myMap={}
myMap["alice"]=88
myMap["bob"]=22
print(myMap)
print(len(myMap))

#we can modify the values mapped to a key
myMap["alice"]=80
print(myMap)

#search for a key in hash map - in constant time
print("alice" in myMap)

myMap.pop("alice")
print("alice" in myMap)



#initialising a hashmap
myMap={"alice":10,"bob":100}
print(myMap)


#dict comprehension
myMap={i:2*i for i in range(5)}
print(myMap)


#looping through maps
myMap={"alice":10,"bob":100}  #to get keys and values
for key in myMap:
    print(key, myMap[key])
    
for key,val in myMap.items():  #to get keys and values
    print(key,val)

for value in myMap.values():  #to get just the values
    print(value)


    
  