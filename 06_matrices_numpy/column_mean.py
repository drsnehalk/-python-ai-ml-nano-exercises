def calculate_mean(values):
    total = 0
    for value in values:
        total += value
    return(total/len(values))


def get_column(matrix,column_index):
    column_values = []
    for row in matrix:
        column_values.append(row[column_index])
    return column_values

def column_mean(matrix):
    means = []
    no_of_columns = len(matrix[0])
    for column_index in range (no_of_columns):
        column = get_column(matrix, column_index)
        mean = calculate_mean(column)
        means.append(mean)
    return means

features = [
      [25, 50000, 0.8],
      [30, 60000, 0.6],
      [35, 80000, 0.9]
  ]
print(column_mean(features))
