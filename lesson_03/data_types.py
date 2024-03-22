#String Data  Types 

#Literal Assignment 

name = "Craig"
surname = "Dipuka"

# print (type(name))
# print(type(surname)==str)
# print (isinstance(name,str))
# print (isinstance(surname,str))

# #constructor function

# pizza = str("pepperoni")
# print (type(pizza))
# print(type(pizza)==str)
# print (isinstance(pizza,str))

# as shown above we have two ways of assigning data , literal assignment and using constructor functions


#Concatination

# fullname = name+ " "+surname
# print(fullname)

# # we can also concatinate an extra value to what already exists
 
# fullname+= "!"
# print(fullname ,end = "\n")


# Type Casting 
#casting is assinging one data type to another type 

# decade = 1980
# print(type(decade))

# new_type = str(decade)

#String Methods 
#String methods are functions that can be applied to strings to perform various operations or manipulations on them

# checking length of a string
length = len(name)
print(length)

#changin  fg to uppercase or lowercase 

uppercase  = name.upper()
print(uppercase)

lowercase  = name.lower()
print(lowercase)