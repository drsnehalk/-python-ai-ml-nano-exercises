

def create_bow_vector (tokens,vocabulary):
    vector = []
    for word in vocabulary:
        count = 0
        for token in tokens:
            if token == word:
                count = count+1
        vector.append(count)
    return vector

tokens = ["ai", "models", "use", "ai"]

vocabulary = ["ai", "models", "use", "data"]

print(create_bow_vector(tokens,vocabulary))
