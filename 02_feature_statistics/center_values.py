def calculate_mean(values):
    total = 0
    for value in values:
        total += value
    return total/len(values)


def center_values(values):
    c_values = []
    mean = calculate_mean(values)
    for value in values:
        new = value - mean
        c_values.append(new)
    return c_values

feature_values = [10, 20, 30]

print(center_values(feature_values))
