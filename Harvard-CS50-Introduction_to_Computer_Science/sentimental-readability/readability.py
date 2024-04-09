# TODO
from cs50 import get_string

# strings for sourcetext
text = get_string("Text: ")

# create variables
letters, words, sentences = 0, 1, 0  # words to 1 because there is no space at the end of the sentence

# count values (letters, words, sentences)
for value in text:
    if value.isalpha():
        letters = letters + 1
    if value.isspace():
        words = words + 1
    if value in ".!?":  # Edge case: (!? and ?!) >> single iteration in Python via strings not really possible ?
        sentences = sentences + 1


# Compute level of difficulty with cleman-liau formula
L = letters / words * 100
S = sentences / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# Output Grade: ... specific level of difficulty / below1:  1 > Before Grade 1 / over 16:  16  > Grade 16+
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
