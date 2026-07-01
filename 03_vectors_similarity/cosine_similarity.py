def dot_product(vector_a, vector_b):
	total =0
	for a,b in zip(vector_a, vector_b):
		product = a*b
		total +=product
	return total

import math
def vector_norm(vector):
	total = 0
	for value in vector:
		squared_total = value**2 
		total += squared_total
	return math.sqrt(total)

def cosine_similarity(vector_a, vector_b):
	for a, b in zip(vector_a, vector_b):
		dot = dot_product(vector_a, vector_b)
		norm_a = vector_norm(vector_a)
		norm_b = vector_norm(vector_b)
		similarity = dot / (norm_a * norm_b)
	return similarity

print(cosine_similarity([1, 2, 3], [1, 2, 3]))
