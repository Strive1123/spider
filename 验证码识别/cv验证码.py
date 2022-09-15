import cv2
cap_ima = cv2.imread('captcha.png',0)
tem_ima = cv2.imread('tm.png',0)
#读取图片 灰度图片
#cap_img=cv2.cvtColor(cap_ima,cv2.)
#tem_img=cv2.cvtColor(tem_ima,cv2.COLOR_BGR2GRAY)
cv2.imshow('b',cap_ima)


#边缘检测
cap_canny = cv2.Canny(cap_ima,300,450)
tem_canny = cv2.Canny(tem_ima,300,450)
cv2.imshow('c',cap_canny)
#轮廓获取
cap_tre= cv2.adaptiveThreshold(cap_canny,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0)
tem_tre= cv2.adaptiveThreshold(tem_canny,244,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0)
cv2.imshow('d',cap_tre)

#模板匹配
#ret = cv2.matchTemplate(cap_tre,tem_tre,cv2.TM_CCOEFF_NORMED)
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(ret)
#计算矩形坐标
#h,w =tem_img.shape[:2]
#right_bottom = (max_loc[0]+w,max_loc[1]+h)
#cv2.rectangle(cap_ima,max_loc,right_bottom,(0,0,255),2)

cv2.imwrite('1.png',cap_ima)
cv2.waitKey(5000)

#https://blog.csdn.net/ysuprogrammer_li/article/details/124709997?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166265606516800182776257%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166265606516800182776257&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-124709997-null-null.142^v47^control,201^v3^add_ask&utm_term=%E7%88%AC%E8%99%AB%E6%BB%91%E5%9D%97%E9%AA%8C%E8%AF%81%E7%A0%81&spm=1018.2226.3001.4187