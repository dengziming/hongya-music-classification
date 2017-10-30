# coding=utf-8
import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import fft
from scipy.io import wavfile

transetfile = 'D:/hongya/data/music/transet/'

genre_list = ["classical", "jazz", "country", "pop", "rock", "metal"]
X=[]
Y=[]
for g in genre_list:
    for n in range(100):
        rad=transetfile+g+"."+str(n).zfill(5)+ ".fft"+".npy"
        fft_features = np.load(rad)
        X.append(fft_features)
        Y.append(genre_list.index(g))

X=np.array(X)
Y=np.array(Y)

# 首先我们要将原始数据分为训练集和测试集，这里是随机抽样80%做测试集，剩下20%做训练集
import random
randomIndex=random.sample(range(len(Y)),int(len(Y)*8/10))
trainX=[];trainY=[];testX=[];testY=[]
for i in range(len(Y)):
    if i in randomIndex:
        trainX.append(X[i])
        trainY.append(Y[i])
    else:
        testX.append(X[i])
        testY.append(Y[i])


# 生成模型
from sklearn.linear_model import LogisticRegression
logclf = LogisticRegression()
logclf.fit(X, Y)

# 使用模型对测试数据进行预测
predictYlogistic=map(lambda x:logclf.predict(x)[0],testX)



# 将predictYlogistic与testY对比，我们就可以知道判定正确率
a = np.array(predictYlogistic)-np.array(testY)
print a, np.count_nonzero(a), len(a)
accuracyLogistic = 1-np.count_nonzero(a)/(len(a)*1.0)
print "%f" % (accuracyLogistic)


# 对黑豹乐队的无地自容进行类别判断
sample_rate, test = wavfile.read("D:/hongya/data/music/sample/heibao-wudizirong-remix.wav")
# sample_rate, test = wavfile.read("d:/genres/metal/converted/metal.00080.au.wav")
testdata_fft_features = abs(fft(test))[:1000]
print sample_rate, testdata_fft_features, len(testdata_fft_features)
print logclf.predict(testdata_fft_features)[0]
print genre_list[logclf.predict(testdata_fft_features)[0]]