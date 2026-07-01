def clean_text(text):
    cleaned_text = " "
    text = text.lower()
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text = cleaned_text + char
    return cleaned_text

def tokenize(text):
    text = clean_text(text)
    tokens = text.split()
    return tokens

def create_vocabulary(tokens):
    vocabulary = [ ]
    for token in tokens:
        if token not in vocabulary:
            vocabulary.append(token)
    return vocabulary

def create_word_index(vocabulary):
    word_index = {}
    for index in range(len(vocabulary)):
        word = vocabulary[index]
        word_index[word] = index
    return word_index

def encode_tokens(tokens, word_index):
    token_ids =[]
    for token in tokens:
        index = word_index[token]
        token_ids.append(index)
    return token_ids

def create_index_word(word_index):
    index_word = {}
    for word in word_index:
        index = word_index[word]
        index_word[index] = word
    return index_word

def decode_ids(token_ids,index_word):
    decoded_tokens =[]
    for token_id in token_ids:
        word = index_word[token_id]
        decoded_tokens.append(word)
    return decoded_tokens

text = "AI models learn from data."

tokens = tokenize(text)
vocabulary = create_vocabulary(tokens)
word_index = create_word_index(vocabulary)
token_ids = encode_tokens(tokens, word_index)
index_word = create_index_word(word_index)
decoded_tokens = decode_ids(token_ids, index_word)

print("Tokens:", tokens)
print("Vocabulary:", vocabulary)
print("Word index:", word_index)
print("Token IDs:", token_ids)
print("Index word:", index_word)
print("Decoded tokens:", decoded_tokens)

