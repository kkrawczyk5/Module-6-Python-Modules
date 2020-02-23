#Created by Kamil Krawczyk
#02/23/2020
#Problem number 4
#This program shows a long and a quick way to calculate pi

import math   #imports math library

pi = 0.0
for i in range(1, 10000000, 4):
    pi += 4/i
    pi -= 4/(i+2)
print(pi) #equation to calculate pi

print(math.pi) #using the math library to calculate pi


