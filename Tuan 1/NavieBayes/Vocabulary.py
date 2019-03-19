import re
import unicodedata
import os

file_stopword = open("/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/stopwords.txt", 'r', encoding='utf-8')
list_stopword = []
for line in file_stopword:
    list_stopword.append(line.split('\n')[0])
del list_stopword[0]
print(list_stopword)
file_stopword.close()

vocabulary = []

for filedir in os.listdir("/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/train"):

    file = open("/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/train/" + filedir, 'r', encoding='utf-8')

    for line in file:
        line = unicodedata.normalize("NFC", line.split("\n")[0])
        regex1 = "[\d]+"
        regex2 = "[^\w]+"
        listtemp = re.sub(regex1, "", line)
        listword = re.sub(regex2, ' ', listtemp)
        # print(listword)
        for word in listword.lower().split(' '):
            if word not in list_stopword and word not in vocabulary and len(word) > 2:
                print(word)
                vocabulary.append(word)
    file.close()

file_vocab = open('/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/vocabulary.txt', 'a', encoding='utf-8')
for word in vocabulary:
    file_vocab.write(word)
    file_vocab.write("\n")
file_vocab.close()
