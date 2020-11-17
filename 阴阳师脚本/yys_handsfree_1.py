import math

import cv2
import pyautogui as pag
from PIL import ImageGrab
import os
import time


def test_mouse_pos():
    """
    鼠标位置
    """
    while True:
        x, y = pag.position()
        print(x, y)

        pass


def test_shot_screen():
    """
    截屏
    """
    # bbox = (左偏移量，上偏移量，x轴长度，y轴长度)
    img = ImageGrab.grab(bbox=(0, 100, 1280, 900))
    print(img)
    img_name = "D:/My_IDE/MyNote/1.jpg"
    img.save(img_name, 'JPEG')


def test_shot_screen2():
    """
    截屏2
    使用cv2match 然后定位坐标
    """
    time.sleep(2)
    imag1 = ImageGrab.grab(bbox=(250, 140, 1670, 940))
    imag1.save("img/1.png", "PNG")
    imag1 = cv2.imread("img/1.png", 0)
    imag2 = cv2.imread("img/28zhang.png", 0)

    h, w = imag2.shape[:2]
    print(h, w)

    res = cv2.matchTemplate(imag1, imag2, cv2.TM_CCOEFF_NORMED)
    print(res.max())
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)

    top_left = min_loc
    btn_right = (top_left[0] + w, top_left[1] + h)
    print(btn_right)

    # 计算坐标
    a1, a2 = top_left
    b1, b2 = btn_right
    c1 = (a1 + w / 2) * 0.8
    c2 = (a2 + h) * 0.8
    e1 = math.ceil(c1)
    e2 = math.ceil(c2)
    d1 = (e1, e2)
    print("中心点", d1)

    # 弹出图像显示匹配位置
    # cv2.circle(res, top_left, 10, 0.2)
    # cv2.imshow("res", res)
    # cv2.waitKey(-1)

    # 画矩阵

    cv2.rectangle(imag1, top_left, btn_right, (0, 255, 0), 2)
    cv2.imshow("imag1", imag1)
    cv2.waitKey(-1)


if __name__ == '__main__':
    test_shot_screen2()
