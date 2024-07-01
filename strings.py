s="abc"
print(s[0:2]) #can be sliced like arrays

#strings are immutable
s[0]="A" #we cannot assign values in strings

#we can update the string but updating will create a new string
s+="def"
print(s)  #output=abcdef 
#Modifying a string is an end time operation




# strings can be converted into integers
print(int("124")+int("345")) #adds 2 integers together

# integers can be converted into strings
print(str(123)+str(345)) #appends or concatenates strings together



#to find the ASCII value of a character: ord()
print(ord("a"))



#Combine a list of strings using a delimitor
strings=["I","am","a","data","analyst"]
print("".join(strings))
print(" ".join(strings))