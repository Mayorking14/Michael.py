def remove_duplicates(words):
    sorted_word = sorted(set(words.split()))
    #removed = set(sorted_word)
    return sorted_word




word = ('this is me and this is you')
print(remove_duplicates(word))