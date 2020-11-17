import random

import cv2
import time
from PIL import ImageGrab
import pyautogui as pag


def screen_shot(x, y, x_width, y_width, temp_path):
    full_screen_img = ImageGrab.grab(bbox=(x, y, x_width, y_width))
    # 必须全英文路径
    full_screen_img.save("D:/My_IDE/MyNote/1.png", 'PNG')
    full_screen_img = cv2.imread("D:/My_IDE/MyNote/1.png", 0)
    temp_img = cv2.imread(temp_path, 0)
    res = cv2.matchTemplate(temp_img, full_screen_img, cv2.TM_CCOEFF_NORMED)
    print(res.max())
    return res


# 安装cv2 https://blog.csdn.net/qq_38327353/article/details/88847694
# 使用管理员权限打开pycharm 否则无法使用pyautogui
def yuhun(fuck_time):
    """
    刷御魂
    在开始界面选择探索
    在探索中选择御魂
    在御魂中选择八岐大蛇
    在八岐大蛇中选择层数
    在八岐大蛇中点击挑战（循环，每一轮挑战需要sleep）
    """
    time.sleep(2)
    # 1.屏幕截图查看是否存在探索按钮
    res = screen_shot(250, 140, 1400, 760, "img/2.png")
    # 若可信度大于70
    if res.max() > 0.7:
        pag.click(x=960 + random.choice([5, 7, 2, 6, 3]), y=270 + random.choice([5, 7, 2, 6, 3]), clicks=1, interval=0,
                  button='LEFT')
        time.sleep(1.5)
        res = screen_shot(250, 140, 1670, 940, "img/yuhun_small.png")
        if res.max() > 0.55:
            pag.click(x=440 + random.choice([5, 7, 2, 6, 3]), y=860 + random.choice([5, 7, 2, 6, 3]), clicks=1,
                      interval=0, button='LEFT')
            time.sleep(1)
            res = screen_shot(250, 140, 1600, 950, "img/baqidashe.png")
            if res.max() > 0.7:
                pag.click(x=400 + random.choice([5, 7, 2, 6, 3]), y=560 + random.choice([5, 7, 2, 6, 3]), clicks=1,
                          interval=0, button='LEFT')
                time.sleep(1.5)
                for i in range(fuck_time):
                    print("第%d次御魂" % i)
                    res = screen_shot(250, 140, 1670, 940, "img/beiming.png")
                    if res.max() > 0.7:
                        pag.click(x=1530 + random.choice([5, 7, 2, 6, 3]), y=830 + random.choice([5, 7, 2, 6, 3]),
                                  clicks=1, interval=0, button='LEFT')
                    time.sleep(50)
                    pag.click(x=950 + random.choice([5, 7, 2, 6, 3]), y=730 + random.choice([5, 7, 2, 6, 3]),
                              interval=1.5, clicks=2, button='LEFT')
            else:
                pass
        else:
            pass
    else:
        pass


if __name__ == '__main__':
    yuhun(20)
