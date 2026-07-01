def error_rate(a,b):
	count = 0
	for i,j in zip(a,b):
		if i !=j:
			count +=1
	return count/len(b)


prediction = [1,1,1,0,1]
label = [0,0,1,1,0]

result = error_rate(prediction, label)
print(result)
