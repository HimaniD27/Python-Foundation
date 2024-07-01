#parentheses not required in conditionals, unless we are working with multi-line conditionals or multiple conditions (with logical operators)
#Indentation is needed to represent a block of code, not curly braces.
#logic and = and
#logic or = or

#range(start,end,step)
#end always excluded
#positive steps to step forward with start<end
#negative steps to step backward with start>end

for i in range(1,9):
    print(i)

for i in range(20,28,2):
    print(i)

for i in range(52,40,-2):
    print(i)

for i in range(52,40,2):  #won't work
    print(i)
    
for i in range(20,28,-2): #won't work
    print(i)



