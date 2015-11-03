# -*- coding: utf-8 -*-
import math
import numpy as np

#p26 例題3.1 4つのベクトルを正規化せよ

def main():
    #indata
    a = [3,2]
    b = [3,4]
    c = [5,4]
    d = [5,6]
    
    indata = [a,b,c,d]
    num = len(indata)
    # xとyの平均
    sum_x = 0
    sum_y = 0
       
    #平均算出     
    mean_x = 0
    mean_y = 0

    for i,val in enumerate(indata):
        sum_x += val[0]
        sum_y += val[1]

    mean_x = sum_x / num
    mean_y = sum_y / num
    mean = [mean_x,mean_y]
    
    #標準偏差算出
    x = 0
    y = 0
    sd_x = 0
    sd_y = 0
    for j,val in enumerate(indata):
        x += (val[0] - mean[0]) * (val[0] - mean[0])
        y += (val[1] - mean[1]) * (val[1] - mean[1])
    sd_x = math.sqrt(x/num)
    sd_y = math.sqrt(y/num)
    
    #正規化行列
    normarize_x = [1/sd_x,0]
    normarize_y = [0,1/sd_y]
    
    nomarize = np.array([[normarize_x],
                         [normarize_y]])
    
    print "(3,2)は"
    print a * nomarize
    
    print "(3,4)は"
    print b * nomarize
    
    print "(5,4)は"
    print c * nomarize    

    print "(5,6)は"
    print d * nomarize
    
if __name__ == '__main__':
    main()