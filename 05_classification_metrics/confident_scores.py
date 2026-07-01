def confident_scores(scores,threshold):
	count =0
	for s in scores:
		if s>=threshold:
			count +=1
	return count

scores = [0.2, 0.95, 0.7, 0.99, 0.1]
print(confident_scores(scores, 0.8))
