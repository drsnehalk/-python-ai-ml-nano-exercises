def biggest(numbers):
	biggest =numbers[0]
	for n in numbers:
		if n> biggest:
			biggest = n
	return biggest

print(biggest([3, 9, 2, 10, 4]))
