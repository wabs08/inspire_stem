#strings in python 
#name : wabs
#date : 22/02/2024
city = "nairobi"
#convert into upper case
print(city)
print("\n") # prints a new line
print(city.upper())

name = "WABS LUK"
print(name)
print(name.lower()) #convert string to lower case

town = "        Naivasha     "
print(town)
print("\t") # new tab
print(town.strip())


# add two strings


f_name = "wabs"
s_name = "luk"

full_name = f_name + s_name

print(full_name)


print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[5])
print(city[6]) 


print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[-1])

print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[-1])
print(city[-2])  #neg ....>reverse the string
 
 #palindrome

#ASSIGNMENT .....1) WRITE A PROGRAM THAT REVERSES A STRING


#Replacing a character

fruit = "orange"
print(fruit.replace("o","y"))
 
#splitting strings
subject = "indusrial:chemistry"
print(subject.split(":"))

#string format

age = 24

print("I am {} years old" .format(age))

#double format ...>KEY
age = 24
height = 1.2

print("I am {0} years old and {1} metres tall" .format(age, height))