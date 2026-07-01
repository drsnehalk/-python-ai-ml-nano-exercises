def clean_text(text):
    text = text.lower()
    cleaned = " "
    for char in text:
        if char not in ".,!?":
            cleaned = cleaned + char
    return cleaned

review = "This Movie was GOOD!!!"
print(clean_text(review))
