#Created by Kamil Krawczyk
#02/23/2020
#Problem number 5
#This program displays 2 different ways to convert radians to degrees

import math #import math library

num = int(input("enter the number to convert: ")) #user input for the conversion

rad_to_degr = (num *180/3.14159265359)   #regular equation to convert radians to degrees
print(rad_to_degr)

print(math.degrees(num))  #math library function to conver radians to degrees






