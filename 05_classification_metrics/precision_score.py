def precision_score (true_positives,false_positives):
	precision = true_positives/(true_positives + false_positives)
	return precision

true_positive = 8
false_positive = 2

print(precision_score(true_positive, false_positive))
