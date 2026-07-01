def cleaned_text(text):
    cleaned= ""
    text = text.lower()
    for char in text:
        if char not in  ".,!?":
            cleaned = cleaned + char
    return cleaned


def tokenize(text):
    text = cleaned_text(text)
    token = text.split()
    return token

review = "This movie is so GOOD!!!"
print(tokenize(review))
