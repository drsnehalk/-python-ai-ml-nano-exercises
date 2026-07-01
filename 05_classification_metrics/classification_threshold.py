def classification_threshold(scores,threshold):
	prediction = []
	for score in scores:
		if score>=threshold:
			prediction.append(1)
		else:
			prediction.append(0)
	return prediction

scores = [0.2, 0.6, 0.8, 0.4]
threshold = 0.5

print(classification_threshold(scores, threshold))
