import cv2
def template_matching(img_path, tm_path):

	# 导入图片，灰度化
    img_rgb = cv2.imread(img_path)
    template_rgb = cv2.imread(tm_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    tm_gray = cv2.cvtColor(template_rgb, cv2.COLOR_BGR2GRAY)
    # 缺口图去除背景
    h, w = tm_gray.shape
    w_start_index, h_start_index = 0, 0
    w_end_index, h_end_index = w, h
    # 缺口图去除背景
    # 算出高起始位置
    for i in range(h):
        if not any(tm_gray[i, :]):
            h_start_index = i
        else:
            break
	# 算出高的结束位置
    for i in range(h - 1, 0, -1):
        if not any(tm_gray[i, :]):
            h_end_index = i
        else:
            break
	# 算出宽的起始位置
    for i in range(w):
        if not any(tm_gray[:, i]):
            w_start_index = i
        else:
            break
	# 算出宽的起始位置
    for i in range(w - 1, 0, -1):
        if not any(tm_gray[:, i]):
            w_end_index = i
        else:
            break
    # 取出完整的缺口图
    tm_gray= tm_gray[h_start_index:h_end_index + 1, w_start_index:w_end_index + 1]
    # 自适应阈值话
    img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
    tm_thresh = cv2.adaptiveThreshold(tm_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)

    # 边缘检测
    img_canny = cv2.Canny(img_thresh, 0, 500)
    tm_canny = cv2.Canny(tm_thresh, 0, 500)
    cv2.imshow("img_canny", img_canny)
    cv2.imshow("tm_canny", tm_canny)
    h, w = tm_gray.shape[:2]
    # 模板匹配
    res = cv2.matchTemplate(img_canny, tm_canny, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    right_bottom = (max_loc[0] + w, max_loc[1] + h)   # 右下角
	# 圈出矩形坐标
    cv2.rectangle(img_rgb, max_loc, right_bottom, (0, 0, 255), 2)

    # 保存处理后的图片
    cv2.imwrite('res.png', img_rgb)

    # 显示图片 参数：（窗口标识字符串，imread读入的图像）
    # cv2.imshow("test_image", img_rgb)
    return img_rgb

if __name__=='__main__':
    template_matching('captcha.png','tm.png')