def create_vocabulary(text):
    text = text.lower()
    cleaned_text = ""
    vocabulary = []
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text = cleaned_text + char
    tokens = cleaned_text.split()
    for token in tokens:
        if token not in vocabulary:
            vocabulary.append(token)
    return vocabulary


def create_word_index(vocabulary):
    word_index ={}
    for index in range (len(vocabulary)):
        word = vocabulary[index]
        word_index[word] = index
    return word_index


review = "Ohh now I remember!!?"
print(create_vocabulary(review))

vocabulary = ["ai", "learns", "from", "data"]
print(create_word_index(vocabulary))
