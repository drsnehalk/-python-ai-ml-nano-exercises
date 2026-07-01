def confusion_counts(predictions,labels):
	true_positive = 0
	true_negative = 0
	false_positive = 0
	false_negative = 0
	for p,l in zip(predictions,labels):
		if p==1 and l==1:
			true_positive+=1
		if p ==0 and l==0:
			true_negative+=1
		if p ==1 and l==0:
			false_positive +=1
		if p ==0 and l==1:
			false_negative +=1
	return(true_positive,true_negative,false_positive,false_negative)


predictions = [1, 0, 1, 1, 0]
labels =      [1, 0, 0, 1, 1]

print(confusion_counts(predictions, labels))
