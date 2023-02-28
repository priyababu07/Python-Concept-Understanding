"""
@AUTHOR  : PRIYA BABU

@DATE    : 23/02/2023

@CONTENT : VARIABLES DATATYPES AND TYPECASTING
"""

#To understand variable consider an example in kitchen we keep containers to store everything differently so variable is also consider as a container that stores variable of same data type
#EX:
var1 = "priya"# here we stored a string in var1
var2 = 12 # stored a integer in variable var2
var3 = 12.5 #stored a float in variable in var3
print(var1)
print(type(var1))#To get the type of var1

print(var2 + var3) #This is a normal equation to run program to add two numbers

# if we consider a string
var4='priya '
var5='rahul'
print(var4+var5)

#Lets look for type casting
var6 = '12'
var7 = '9'
print(int(var6) + int(var7)) #here the string is converted to integer
"""
str()
int()
float()
"""
print(100*"HEllo World\n")

"""
QUIZE 
"""
#User input
num1=int(input("Enter the number"))
print(num1)

#QUIZE PROBLEM
"""
CALCULATOR THAT ADDS TWO NUMBER
"""

numa=int(input("Enter the first number"))
numb= int(input("Enter the second number"))

sum= numa+numb
print(sum)