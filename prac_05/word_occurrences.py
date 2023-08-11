word_dic = {}

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

for word in word_dic:
    print('{word} : {count}'.format(word=word, count=word_dic[word]))
