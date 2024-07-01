#HashSets are useful because we can search them in constant time and we can insert values in constant time
#There can't be any duplicates in a hash set


mySet=set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
print(1 in mySet) #search for values 
print(3 in mySet)
mySet.remove(2) #in constant time
print(mySet)



#list to set
print(set([1,3,5,7,9]))




#set comprehension
my_Set={i for i in range(5)}
print(my_Set)