"""
Word Occurrences
Estimate: 15 minutes
Actual:   28 minutes
"""
word_dic = {}
max_word_length = 0

text_list = input("Text :").split(" ")
text_list.sort()

for word in text_list:
    try:
        count = word_dic[word]
        count += 1
        word_dic[word] = count

    except KeyError:
        """ if its the first entry of word"""
        word_dic[word] = 1

    """ length of longest"""
    word_length = len(word)
    if word_length > max_word_length:
        max_word_length = int(word_length)

for word in word_dic:
    count = word_dic[word]
    length = max_word_length
    print(f"{word:<{length}} : {count}")
