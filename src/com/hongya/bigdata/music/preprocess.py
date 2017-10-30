# coding=utf-8

import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import fft
from scipy.io import wavfile

# g是类别，n是每个类别的音乐文件前面的数字

# file是转换格式后的文件地址
file = 'D:/hongya/data/music/genres/convert/'
transetfile = 'D:/hongya/data/music/transet/'

# g是类别，n是文件前面的数字
def create_fft(g,n):
    rad=file+g+"."+str(n).zfill(5)+".au.wav"
    sample_rate, X = wavfile.read(rad)
    fft_features = abs(fft(X)[:1000])
    sad=transetfile+g+"."+str(n).zfill(5)+ ".fft"
    np.save(sad, fft_features)

#-------creat fft--------------

genre_list = ["classical", "jazz", "country", "pop", "rock", "metal"]
for g in genre_list:
    for n in range(100):
        create_fft(g,n)