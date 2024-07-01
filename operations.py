#decimal division (by default)
print(7/2) #output=3.5
print(int(-7/2)) #output=-3

#integer/floor division = round down
print(7//2)  #output=3
print(-7//2) #output=-4

#math helpers
#ceil method = round up
import math  
a=7/2
print(math.ceil(a)) #output=4
b=-7/2
print(math.ceil(b)) #output=-3

#floor method = round down
a=7/2
print(math.floor(a)) #output=3
b=-7/2
print(math.floor(b)) #output=-4



#modulo operator (can be used for integer or floating point numbers)
print(5%2) #output=1

print(-10%7) #output=4
#print(-10/7)
print(-10//7) #output=-2    # 7*(-2)+4=-10    4=remainder

print(-10%-7) #output=3

#to deal with negative numbers and to deal with floating point numbers
import math
print(math.fmod(-10,3))


#math helpers
print(math.sqrt(6))  #square root 
print(math.pow(4,5))  # 4 to the power of 5

#python numbers are infinite so they never overflow
# maximum integer
float("inf")
print(float("inf")) #output= inf
# minimum integer
float("-inf")
print(float("-inf"))  #output= -inf