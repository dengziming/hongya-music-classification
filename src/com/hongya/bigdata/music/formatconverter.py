
# coding=utf-8

import os


file = 'D:\\hongya\\data\\music\\genres\\'


def music_convert(fp):
    f = os.listdir(file + fp)  # 重新载入修改后的文件名
    os.mkdir(file + 'convert\\' + fp)
    for i in range(len(f)):
        print('sox %s %s' % (file + fp + f[i], file + 'convert\\' + fp + f[i] + '.wav'))  # python格式化输出的语法非常有用

        os.chdir('E:\\program\\sox')

        os.system('E:\\program\\sox\sox %s %s' % (file + fp + f[i], file + 'convert\\' + fp + f[i] + '.wav'))  # python格式化输出的语法


genre_list = ["classical\\", "jazz\\", "country\\", "pop\\", "rock\\", "metal\\"]

for g in genre_list:
    music_convert(g)

