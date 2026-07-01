def dot_product(a,b):
	total = 0
	for i in range(len(a)):
		product = a[i] * b[i]
		total +=product
	return total

a = [1, 2, 3]
b = [4, 5, 6]

print(dot_product(a,b))
