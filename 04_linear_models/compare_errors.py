def mean_squared_error(predictions, targets):
	mse=0
	for prediction,target in zip(predictions,targets):
		error= target-prediction
		squared_error = error **2
		mse +=squared_error
	return mse/len(targets)
def mean_absolute_error(predictions, targets):
	mae=0
	for prediction, target in zip(predictions,targets):
		error = target-prediction
		abs_error= abs(error)
		mae += abs_error
	return mae/len(targets)

def compare_errors(predictions, targets):
     mse = mean_squared_error(predictions, targets)
     mae = mean_absolute_error(predictions, targets)

     return [mse, mae]

predictions = [2.5, 3.0, 4.8]
targets = [3.0, 2.5, 5.0]
results = compare_errors(predictions,targets)
print(results)
