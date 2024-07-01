#Python is a dynamically typed language which means the type of a variable is determined at the runtime

#assignment of a value
n=0
print(type(n))
n="abc" #reassignment
print(n)
print(type(n))


#multiple assignment 
n,m=5,"abc"
print(n,m)


n+=1  #n=n+1 increment
n-=1  #n=n-1 decrement
n*=2  #n=n*2 


# None means absence of a value
n=4
n+=1
print(n)

n=0
n+=1
print(n)

n=None
n+=1
print(n)



