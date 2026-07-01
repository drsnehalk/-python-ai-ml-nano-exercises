def mat_vec_mul(matrix,vector):
	result = []
	for row in matrix:
		total = 0
		for i in range(len(vector)):
			total+= row[i]*vector[i]
		result.append(total)
	return result


A = [
      [1, 2],
      [3, 4]
  ]

x = [10, 20]

print(mat_vec_mul(A, x))

