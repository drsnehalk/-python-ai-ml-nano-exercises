def min_max(values):
    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return [0 for value in values]

    scaled_values = []

    for value in values:
        scaled_value = (value - min_value) / (max_value - min_value)
        scaled_values.append(scaled_value)

    return scaled_values


feature_values = [10, 20, 30]
print(min_max(feature_values))

feature_values = [5, 5, 5]
print(min_max(feature_values))
