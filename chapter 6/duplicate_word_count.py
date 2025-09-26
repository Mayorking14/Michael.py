def count_words(text):
    sentence = text.lower().split()

    count_word = {}

    for word in sentence:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    for key, value in count_word.items():
        if value > 1:
            print(f'{key}: appears {value} times')

word = ('this is me and this is you')
print(count_words(word))