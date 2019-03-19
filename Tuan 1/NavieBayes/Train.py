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


for filedir in os.listdir("/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/train"):

    file = open("/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/train/" + filedir, 'r', encoding='utf-8')

    dict = {}

    for line in file:
        line = unicodedata.normalize("NFC", line.split("\n")[0])
        regex1 = "[\d]+"
        regex2 = "[^\w]+"
        listtemp = re.sub(regex1, "", line)
        listword = re.sub(regex2, ' ', listtemp)
        # print(listword)
        for word in listword.lower().split(' '):
            if word not in list_stopword and len(word) > 2:
                #print(word)
                if word not in dict:

                    dict[word] = 1
                else :
                    dict[word] +=1
    file.close()
    print(dict)
    print(len(dict))

    file.close()

    file_train = open('/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/'+ filedir, 'a', encoding='utf-8')
    for word in dict:
        file_train.write(word+" : "+ str(dict[word])+"\n")
    file_train.close()

