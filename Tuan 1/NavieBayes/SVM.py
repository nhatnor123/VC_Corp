import numpy as np

from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

def get_train(stopword):
	datas_train = []
	targets_train = []
	for i in range(1, 14, 1):
		for line in open("/home/nhatnor123/Desktop/gitlabVC/classify_data/train/" + str(i) + ".txt", encoding="utf-8"):
			targets_train.append(i)
			doc = []
			for word in line.lower().split(" "):
				if (not word in stopword) and (not word.isdigit()):
					doc.append(word)
			datas_train.append(' '.join(doc))
	targets_train = np.asarray(targets_train)
	return datas_train, targets_train


def get_test(stopword):
	datas_test = []
	targets_test = []

	for line in open("/home/nhatnor123/Desktop/gitlabVC/classify_data/test/data.txt", encoding="utf-8"):
		doc = []
		for word in line.lower().split(" "):
			if (not word in stopword) and (not word.isdigit()):
				doc.append(word)
		datas_test.append(' '.join(doc))

	for line in open("/home/nhatnor123/Desktop/gitlabVC/classify_data/test/label.txt", encoding="utf-8"):
		targets_test.append(int(line))
	targets_test = np.asarray(targets_test)
	return datas_test, targets_test


def svm_core(datas_train, targets_train, datas_test, targets_test):
	vectorizer = TfidfVectorizer(min_df=0.005, max_df=0.8)
	vectors_train = vectorizer.fit_transform(datas_train)
	vectors_test = vectorizer.transform(datas_test)
	
	scoreLSVC = LinearSVC(C=2.2).fit(vectors_train, targets_train).score(vectors_test, targets_test)

	print("--------- classify_data ---------")
	print("Train : ", vectors_train.shape[0])
	print("Test  : ", vectors_test.shape[0])

	print("-----          SVM          -----")
	print("ScoreLSVC :", 100 * scoreLSVC, "%")


#main
stopword = open("/home/nhatnor123/Desktop/gitlabVC/Tuan 1/stopwords.txt", encoding="utf-8").read().split("\n")
data_train, target_train = get_train(stopword)
data_test, target_test = get_test(stopword)
svm_core(data_train, target_train, data_test, target_test)