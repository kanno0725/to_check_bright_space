# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:14:31 2020

@author: kanno
"""

import cv2
#from tqdm import tqdm
#import numpy as np

video_path = "crop4_1.avi"
cap = cv2.VideoCapture(video_path)

filename = 'crop4_1_weld'
f = open(filename+'.csv', 'w')
f.close()

num = 0
while(cap.isOpened()):
    ret1, frame = cap.read()
    if ret1 == True:
        # 画像読み込み
        #img = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
        gray_img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # 2値化
        ret, binary = cv2.threshold(gray_img, 245, 255, cv2.THRESH_BINARY)

        # 輪郭抽出
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        areas = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if 500 < area :
                areas.append(cnt)
                
        f = open(filename+'.csv', 'a')
        for i in range(len(areas)):
            f.write('frame'+str(num)+','+'area'+str(i))
            for j in range(len(areas[i])):
                f.write(','+str(areas[i][j][0][0]))
                f.write(','+str(areas[i][j][0][1]))
            f.write('\n')
        f.close()
        
        #   im = cv2.drawContours(img, areas, -1, (0,255,0), 3)
        num += 1
        print('end / '+str(num))
    else:
        break

cap.release()

"""
cv2.imshow("img", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 余計な次元削除 (NumContours, 1, NumPoints) -> (NumContours, NumPoints)
contours = [np.squeeze(cnt, axis=1) for cnt in contours]

# 座標表示
print('coordinates of lines 0: {}', contours[0])
print('coordinates of lines 1: {}', contours[1])

print(area)
        epsilon = 0.1*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
"""