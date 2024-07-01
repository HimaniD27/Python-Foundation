#list comprehension in 1-D list or array:
arr=[i for i in range(8)]
print(arr)

arr=[i+i for i in range(8)]
print(arr)

#list comprehension in 2-D list or array:
arr=[[0]*4 for i in range(4)] #4 unique rows are created using list comprehension
print(arr)
arr=[[0]*4]*4  #it modifies all the rows as all rows are the same

arr=[[i]*4 for i in range(4)]
print(arr)

