#Created by Kamil Krawczyk
#02/23/2020
#Problem number 6
#This program displays 2 different ways to calculate the factorial of a user input value

import math   #import math library

num = int(input("input a number: "))    #user inputs the number
fac = 1
 
for i in range(1, num + 1):   #for loop to calculate the factorial
  fac = fac * i

print(fac)

print(math.factorial(num))    #math library function to calculate factorial

