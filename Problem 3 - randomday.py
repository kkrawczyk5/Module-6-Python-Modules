#Created by Kamil Krawczyk
#02/23/2020
#Problem number 3
#This program picks a random day of the week for a list

import random   #imports random library

weekday = ["Monday","Tuesday","Wednesday","Thursday",
"Friday", "Saturday", "Sunday"]   #list of days of the week
print(random.choice(weekday))   #function to select a random day of the week