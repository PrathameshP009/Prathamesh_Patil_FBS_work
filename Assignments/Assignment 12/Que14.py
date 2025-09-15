#Python Program to count the occurrences of ach word in a string.
s = "apple banana apple orange banana apple"
words = s.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Counts:", word_count)
