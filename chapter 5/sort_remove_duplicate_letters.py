import random

letters = []

for char in range(10):
    letters.append(random.choice(['a','b','c','d','e','f','g','h','i','j']))

print (letters)
print (sorted(letters))
print(sorted(letters, reverse=True))
print(sorted(set(letters)))