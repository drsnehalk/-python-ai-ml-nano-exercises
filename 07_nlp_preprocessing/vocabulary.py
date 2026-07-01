def create_vocabulary(text):
    vocabulary = []
    text = text.lower()
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text = cleaned_text + char
    tokens = cleaned_text.split()
    for token in tokens:
        if token not in vocabulary:
            vocabulary.append(token)
    return vocabulary


text = "AI learns, predicts, and improves! AI learns from data."
print(create_vocabulary(text))
