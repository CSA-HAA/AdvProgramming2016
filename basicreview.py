#Hamzah Ahmed

import random

print("Program #1")
#Makes empty list
x = []

#Adds a random num as long as there arent 10 things in list
while len(x) != 10:
	randomnum = random.randrange(1, 50) #generates random number between 1 and 50
	if randomnum not in x: #Adds number if it hasnt already been generated
		x.append(randomnum)
	else:
		continue

#Prints each number one after another seperated by a space
x = [str(i) for i in x]
print (' '.join(x))

print()

print("Program #2")
#Makes car class
class Car:
	#Gives is color year and topspeed attributes
	def __init__(self, color, year, topspeed):
		self.color = color
		self.year = year
		self.topspeed = topspeed
	#returns a string with all variables in a sentence
	def __str__(self):
		return ("You have a " + self.color + " car from "+ self.year +" that can go " + self.topspeed + " miles per hour.")
		
#Asks for info on car
c = input("What color is the car? ")
y= input("What year is the car? ")
ts = input("What is the car's top speed? ")

#Adds values to a car and creates a car object
thecar = Car(c, y, ts)

#Calls on a car method to print the car attributes
print (thecar)
