def dot_product(vector_a, vector_b):
	total = 0
	for a,b in zip(vector_a,vector_b):
		product = a * b
		total += product
	return total


def batch_linear_predictions(feature_matrix, weights, bias):
	predictions = []
	for row in feature_matrix:
		dot = dot_product(row,weights)
		total = dot + bias
		predictions.append(total)
	return predictions




features = [
      [1, 2],
      [3, 4],
      [5, 6]
  ]

weights = [0.5, 1.0]
bias = 2

print(batch_linear_predictions(features, weights, bias))

