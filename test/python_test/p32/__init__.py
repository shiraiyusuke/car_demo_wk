# -*- coding: utf-8 -*-
import math
import numpy as np

#p26 ���3.1 4�̃x�N�g���𐳋K������

def main():
    #indata
    a = np.array([3,2])
    b = np.array([3,4])
    c = np.array([5,4])
    d = np.array([5,6])
    
    indata = [a,b,c,d]
    num = len(indata)
    # x��y�̕���
    sum_x = 0
    sum_y = 0
       
    #���ώZ�o     
    mean_x = 0
    mean_y = 0

    for i,val in enumerate(indata):
        sum_x += val[0]
        sum_y += val[1]

    mean_x = sum_x / num
    mean_y = sum_y / num
    mean = [mean_x,mean_y]
    
    #�W���΍��Z�o
    x = 0
    y = 0
    sd_x = 0
    sd_y = 0
    for j,val in enumerate(indata):
        x += (val[0] - mean[0]) * (val[0] - mean[0])
        y += (val[1] - mean[1]) * (val[1] - mean[1])
    sd_x = math.sqrt(x/num)
    sd_y = math.sqrt(y/num)
    
    #共分散行列を求めるための準備
    normarize_x = [1/sd_x,0]
    normarize_y = [0,1/sd_y]
    
    nomarize = np.array([normarize_x,
                         normarize_y])
    
    # 転置した標準化ベクトル
    a1 = a.dot(nomarize)
    b1 = b.dot(nomarize)
    c1 = c.dot(nomarize) 
    d1 = d.dot(nomarize)
    
    print a1
    
    print "-------------"
    
    #標準化ベクトルの平均取得
    mean_x1 =0
    mean_y1 = 0
    meansum_x1 =0
    meansum_y1 = 0
    
    mean_data1 = [a1,b1,c1,d1]
    num1 = len(mean_data1)
    
    for i,val in enumerate(mean_data1):
        meansum_x1 += val[0]
        meansum_y1 += val[1]
    mean_x1 = meansum_x1 / num
    mean_y1 = meansum_y1 / num
    mean_row = np.array([[mean_x1],[mean_y1]])
    
    # 共分散行列算出
    print a1
    print mean_row
    print a1 - mean_row
        
if __name__ == '__main__':
    main()