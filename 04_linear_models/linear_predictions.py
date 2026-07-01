def linear_predictions(features, weights,bias):
	total =0
	for feature, weight in zip(features, weights):
		product = feature * weight
		total += product
	return total+bias

features = [2, 3, 4]
weights = [0.5, 1.0, -1.0]
bias = 1.5

result = linear_predictions(features,weights,bias)
print(result)
