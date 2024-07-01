#helpful in recursive problems
#inner functions or nested functions have access to the outer variables or variables of the outer function

def outer(a,b):
    c="c"
    def inner(): #inner() will have access to both the outer variables
        return a+b+c
    return inner()
print(outer("a","b"))


#can modify objects but not reassign unless you are using non local keyword 
def double(arr,val):
    def helper(): #helper() will have access to both the outer variables
        for i,n in enumerate(arr):
            arr[i]*=2 #will only modify(double the) value in the scope of the helper function
        nonlocal val #this will modify val outside the scope of the helper function
        val*=2
    helper()
    print(arr,val)
    
nums=[1,2]
val=3
double(nums,val)
