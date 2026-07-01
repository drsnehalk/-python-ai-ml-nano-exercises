def sum_positive(numbers):
	positive = 0
	for n in numbers:
		if n>=0:
			positive +=n
	return positive

print(sum_positive([-2, 5, -1, 3]))
