import NavieBayes.Vocabulary
import NavieBayes.Train
import NavieBayes.NavieBayesCore

def main():
    file_stopword = open("/home/nhatnor123/Desktop/BaiTapVCCorp/Tuan 1/stopwords.txt", 'r', encoding='utf-8')
    list_stopword = []
    for line in file_stopword:
        list_stopword.append(line.split('\n')[0])
    del list_stopword[0]
    print(list_stopword)
    file_stopword.close()

    NavieBayes.Vocabulary(list_stopword)
    NavieBayes.Train(list_stopword)
    NavieBayes.Train(list_stopword)

    #tính kết quả sau khi phân loại :
    file_result = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/result.txt', 'r')
    file_label = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/label.txt', 'r')
    count_true_result = 0
    for line in file_label:
        temp = file_result.readline().split('\n')[0]
        if line.split('\n')[0] == temp:
            count_true_result += 1

    print(count_true_result)

    file_result.close()
    file_label.close()

