def recall_score(true_positives,false_negatives):
	recall = true_positives/(true_positives+false_negatives)
	return recall


true_positive = 6
false_negative = 4

print(recall_score(true_positive, false_negative))
