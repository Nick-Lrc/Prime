from prime import is_prime
from prime import get_next_prime_after

def printGreeting():
	print(":: Prime Interaction Program ::")

def printOptions():
	print("Options")
	print("  1. Find a prime after a number")
	print("  2. Verify if a number is a prime")
	print()

def printGoodbye():
	print(":: Goodbye ::")

printGreeting()
printOptions()

while True:
	try:
		user_input = input("Option: ")
		option = int(user_input)
		if option == 1:
			user_input = input("After: ")
			num = int(user_input)
			prime = get_next_prime_after(num)
			
			if prime == -1:
				print("Cannot find a prime after '%d'" % num)
			else:
				print("Next prime after '%d' is '%d'" % (num, prime))
			
		elif option == 2:
			user_input = input("Target: ")
			num = int(user_input)
			if is_prime(num):
				print("'%d' is a prime" % (num))
			else:
				print("'%d' is not a prime" % (num))
		else:
			print("Error: invalid option '%s'" % (user_input))
		
		user_input = input("Continue(y/n): ")
		if user_input == "n":
			break
			
	except ValueError:
		print("Error: invalid input '%s'" % (user_input))
	finally:
		print()

printGoodbye()