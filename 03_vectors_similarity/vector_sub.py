def vector_sub(a,b):
	results = []
	for i in range(len(a)):
		results.append(a[i]-b[i])
	return results

print(vector_sub([1, 2, 3], [4, 5, 6]))
