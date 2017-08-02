# This program is a simple number guessing game
# Each time that it is ran, a random number will be generated
# The user will have five chances to guess the number 

from random import randint

mystery_number = randint(1,100)

number_guessed = False
count = 1
print "You have five chances to guess the mystery number between 1 and 100..."

while count < 6:
	guess = int(raw_input("Guess Number %s: " %count))
	if (guess == mystery_number):
		print "Congratulations! You guessed the mystery number."
		break
	else:
		count = count + 1
		print "Try Again..."
else:
	print "Sorry, you lost."
