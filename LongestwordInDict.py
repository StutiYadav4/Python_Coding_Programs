dict_input = input("Enter the words in the dictionary: ")
dictionary = set(dict_input.split())
string = input("Enter the string: ")
largestWord = ""
for word in dictionary:
    word_len = len(word)
    string_len = len(string)
    i, j = 0, 0
    while i < word_len and j < string_len:
        if word[i] == string[j]:
            i += 1
        j += 1
    if i == word_len:
        if len(word) > len(largestWord):
            largestWord = word
        elif len(word) == len(largestWord) and word < largestWord:
            largestWord = word
print("The largest word is :", largestWord)


