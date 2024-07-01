class myClass:
    def __init__(self,nums): #__init__ is the Constructor  # self is passed into every method of the class
        self.nums=nums #creating member variables #self keyword is use to create member variables
        self.size=len(nums)
    
    def getLength(self): #creating method for a class #self keyword is always required as parameter
        return self.size
    
    def getDoubleLength(self): #calling another member function from a member function
        return 2*self.getLength()
