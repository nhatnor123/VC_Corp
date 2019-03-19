import re
import unicodedata
import math
import os

file_stopword = open("/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/stopwords.txt", 'r', encoding='utf-8')
list_stopword = []
for line in file_stopword:
    list_stopword.append(line.split('\n')[0])
del list_stopword[0]
file_stopword.close()

file_vocab = open('/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/vocabulary.txt', 'r', encoding='utf-8')
vocabulary = file_vocab.read().split('\n')
file_vocab.close()
vocabulary.pop()
vocabulary.pop()
print(vocabulary)
print(len(vocabulary))

classification_dict = {}
count_total = {}
for i in range(1, 14, 1):
    count_total[i] = 0
    classification_dict[i] = {}
    file = open('/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/' + str(i) + ".txt", 'r', encoding='utf-8')
    for line in file:
        classification_dict[i][line.split('\n')[0].split(' : ')[0]] = int(line.split('\n')[0].split(' : ')[1])
        count_total[i] +=int(line.split('\n')[0].split(' : ')[1])
print(classification_dict)
print(count_total)




file_test = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/data.txt', 'r', encoding='utf-8')
file_result = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/result.txt', 'a')
for i in file_test:
    #print(i.split('\n')[0])
    line = unicodedata.normalize("NFC", i.split("\n")[0])
    regex1 = "[\d]+"
    regex2 = "[^\w]+"
    listtemp = re.sub(regex1, "", line)
    listword = re.sub(regex2, ' ', listtemp).lower()
    print(listword)
    dict_word = {}

    for word in listword.split(" "):
        if word not in list_stopword and len(word) > 2:
            if word not in dict_word:
                dict_word[word] = 1
            else:
                dict_word[word] += 1
    p = float(0)
    min = -100000.0
    result = 0

    for label in classification_dict:
        for word in dict_word:
            if word not in classification_dict[label]:
                p += math.log10(1.0  / (len(vocabulary) + count_total[label]))*dict_word[word]
            else :
                p += math.log10(1.0+classification_dict[label][word])/ (len(vocabulary)+count_total[label])*dict_word[word]

        print(p)

        if p>min:
            min = p
            result = label

        p = float(0)

    print(result)
    file_result.write(str(result)+"\n")

file_result.close()
file_test.close()
