def unknown_word(tokens,word_index):
    token_ids = []
    for token in tokens:
        if token in word_index:
            index = word_index[token]
            token_ids.append(index)
        else:
            index = word_index["<UNK>"]
            token_ids.append(index)
    return token_ids



tokens = ["ai", "models", "generalize"]

word_index = {
      "<UNK>": 0,
      "ai": 1,
      "models": 2,
      "learn": 3
  }
print(unknown_word(tokens, word_index))
