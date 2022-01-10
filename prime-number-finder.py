# Finds prime numbers in a given range. Inspired by SoloLearn's "Intermediate Python" course.

print("Let's find all of the prime numbers in a range. \n")
min_value = int(input("Please provide minimum value: \n"))
max_value = int(input("Please provide maximum value: \n"))

def isPrime(x):
	if x < 2:
		return False
	else:
		for number in range(2, x):
			if x % number == 0:
				return False
		return True

def primeGenerator(x, y):
	for number in range(x, y):
		if isPrime(number):
			yield number

print(list(primeGenerator(min_value, max_value)))
