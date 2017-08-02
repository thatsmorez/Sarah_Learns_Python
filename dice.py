# This program simulates the rolling of a dice
# Each time that it is ran, a random number will be generated
# Users will have the option to roll again or to exit after each roll
from random import randint

min = 1
max = int(raw_input("How many sides are on your dice? "))

roll_again = 'y'

while roll_again == 'y':
	print randint(min, max)
	roll_again = raw_input("Roll again? y/n ")
