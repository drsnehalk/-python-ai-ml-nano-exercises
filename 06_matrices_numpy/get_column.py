def get_column(matrix, column_index):
    column_values = []
    for row in matrix:
      column_values.append(row[column_index])
    return column_values

features = [
      [25, 50000, 0.8],
      [30, 60000, 0.6],
      [35, 80000, 0.9]
  ]

print(get_column(features, 0))
print(get_column(features, 1))

print(get_column(features, 2))
