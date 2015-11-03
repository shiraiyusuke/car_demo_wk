# -*- coding: utf-8 -*-
import cv2
 
def main():
    # 画像の取得
    im = cv2.imread("test.png")  # @UndefinedVariable
    # 直線を引く
    cv2.line(im,(100,200),(300,200),(0,0,255),5)
    # 画像の表示
    cv2.imwrite("bb.png",im)
 
if __name__ == '__main__':
    main()