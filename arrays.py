arr=[1,2,3,4,5,6,7,8]
arr.append(9)
arr.pop()  #array.pop(index)
arr.insert(3,18)  #arr.insert(index,value_to_be_inserted)
print(arr)
#appending, inserting = big O of end time operation

arr[0]=555
print(arr)
#indexung array is not Big O of end time operation  #constant time operation

# End time operations:
# appending an element to the end of a list
# removing the last element from a list
# accessing the last element in a list

# Constant time operations:
# accessing an element in an array by index (array[i]).
# pushing or popping an element from the end of a stack.
# retrieving the length of an array or list.




#Slicing an array:
arr1=[1,2,3,4,5,6,7,8]
print(arr1[2:5])



#unpacking an array
x,y,z=[1,2,3]
print(x,y,z)



#looping through arrays
for i in range(len(arr1)): #using index
  print(arr1[i])

for n in arr1: #without index
  print(n)

for i,n in enumerate(arr1):  #index,value pair
  print(i,n)

nums1=[1,2,3]  #looping through multiple arrays simultaneously without unpacking
nums2=[4,5,6]
for n1,n2 in zip(nums1,nums2):
  print(n1,n2)




#reversing an array:
a=[1,2,3]
a.reverse()
print(a)




#sorting an array:
a=[1,3,8,7,6,4]
a.sort()     
#a.sort(reverse=True)   #for desecending order
print(a)
#we can sort a list of strings, by default they will be sorted based on alphabetical order
a=["alice","in","wonder","land"]
a.sort() 
print(a)

#custom sort- by passing a lambda function
a.sort(key=lambda x:len(x)) 
#lambda= a function without a name, an anonymous function 
#A lambda function in Python is a small anonymous function defined with the lambda keyword. Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions are syntactically restricted to a single line.
#x=every element of array
#x:len(x)= taking every element of the array and returning the length of x 
# key is lambda x:len(x) based on which the array will be sorted
#each string is gonna be mapped to its length and then we're going to sort those



