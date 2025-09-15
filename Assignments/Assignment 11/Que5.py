#Python Program to Sort a List According to the Length of the Elements within list.
words = ["apple", "fig", "banana", "kiwi"]
sorted_words = sorted(words, key=len)
print("Sorted by Length:", sorted_words)
