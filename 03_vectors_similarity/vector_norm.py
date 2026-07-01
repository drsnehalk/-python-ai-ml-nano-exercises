import math

def vector_norm(vector):
	total = 0
	for i in vector:
		squared= i**2
		total +=squared
	norm = math.sqrt(total)
	return norm

print(vector_norm([6,8]))

def vector_normalized(vector):
	normalized=[]
	norm = vector_norm(vector)
	for value in vector:
		new_value = value/norm
		normalized.append(new_value)
	return normalized

print(vector_normalized([3,4]))
