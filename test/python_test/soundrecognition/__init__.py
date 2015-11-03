# -*- coding: utf-8 -*-
import math

# p10 例題1.1
def main():
    #正解ベクトル生成
    mozi_0 = [0,1,1,1,0, \
              1,0,0,0,1, \
              1,0,0,0,1, \
              1,0,0,0,1, \
              0,1,1,1,0]

    mozi_1 = [0,0,1,0,0, \
              0,0,1,0,0, \
              0,0,1,0,0, \
              0,0,1,0,0, \
              0,0,1,0,0]

    mozi_2 = [0,1,1,1,1, \
              1,0,0,1,0, \
              0,0,1,0,0, \
              0,1,0,0,0, \
              1,1,1,1,1]

    mozi_3 = [0,1,1,1,0, \
              1,0,0,0,1, \
              0,0,1,1,0, \
              1,0,0,0,1, \
              0,1,1,1,0]

    mozi_4 = [0,0,1,0,0, \
              0,1,0,0,0, \
              1,0,0,1,0, \
              1,1,1,1,1, \
              0,0,0,1,0]
    
    aa = [mozi_0,mozi_1,mozi_2,mozi_3,mozi_4]

    # 予測用文字列
    yosoku = [0,0,0,1,0, \
              0,0,0,1,0, \
              0,0,0,1,0, \
              0,0,0,1,0, \
              0,0,0,1,0]
    
    result = []
    num = 0
    result_num = 0
    min_x =0
    
    
    for i,mozi in enumerate(aa):
        gosa = 0
        for j in range(24):
            gosa += (mozi[j] - yosoku[j]) * (mozi[j] - yosoku[j])
            
        gosa = math.sqrt(gosa)
        print str(i) + ":" + str(gosa)
        result.append(gosa)
    
    for k,gosa in enumerate(result):
        if k == 0:
            min_x = gosa
            result_num = k
        else:
            if min_x > gosa:
                min_x = gosa
                result_num = k
    
    print "最も近いのは、" + str(result_num) + "で、誤差は" + str(min_x)
        
if __name__ == '__main__':
    main()
    
