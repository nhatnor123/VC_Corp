file_result = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/result.txt', 'r')
file_label = open('/home/nhatnor123/Desktop/BaiTapVCCorp/classify_data/test/label.txt', 'r')

count_true_result = 0

for line in file_label:
    temp = file_result.readline().split('\n')[0]
    if line.split('\n')[0] == temp:
        count_true_result+=1
        
print(count_true_result)

file_result.close()
file_label.close()

