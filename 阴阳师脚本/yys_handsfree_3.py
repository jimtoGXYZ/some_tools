import random
import cv2
import time
import pyautogui as pag
from PIL import ImageGrab


def screen_shot(temp_path, x=250, y=140, x_width=1670, y_width=940):
    full_screen_img = ImageGrab.grab(bbox=(x, y, x_width, y_width))
    # 必须全英文路径
    full_screen_img.save("D:/My_IDE/MyNote/1.png", 'PNG')
    full_screen_img = cv2.imread("D:/My_IDE/MyNote/1.png", 0)
    temp_img = cv2.imread(temp_path, 0)
    res = cv2.matchTemplate(temp_img, full_screen_img, cv2.TM_CCOEFF_NORMED)
    print(res.max())
    return res


def validate_num(fun):
    """
    装饰器 验证输入数字
    """

    def inner():
        print("into inner")
        fuck_time = input("请输入重复次数:")
        try:
            fuck_time = int(fuck_time)
            fun(fuck_time)
        except Exception as e:
            print(e)
            print("请输入数字!")

    return inner


@validate_num
def yuhun(fuck_time):
    """
    刷御魂
    """
    print("*" * 10 + "开始刷御魂" + "*" * 10)
    time.sleep(2)
    res = screen_shot("img/baqidashe.png", 250, 140, 1600, 950)
    if res.max() > 0.7:
        pag.click(x=400 + random.choice([5, 7, 2, 6, 3]), y=560 + random.choice([5, 7, 2, 6, 3]), clicks=1,
                  interval=0, button='LEFT')
        time.sleep(random.choice([1.5, 1.52, 1.55, 1.49, 1.59]))
        for i in range(fuck_time):
            print("第%s次御魂" % str(i + 1))
            res = screen_shot("img/beiming.png")
            if res.max() > 0.7:
                pag.click(x=1530 + random.choice([5, 7, 2, 6, 3]), y=830 + random.choice([5, 7, 2, 6, 3]),
                          clicks=1, interval=0, button='LEFT')
            time.sleep(random.choice([50, 50.2, 50.4, 50.3, 49.8, 50.5, 51]))
            pag.click(x=950 + random.choice([5, 7, 2, 6, 3]), y=730 + random.choice([5, 7, 2, 6, 3]),
                      interval=1.5, clicks=2, button='LEFT')


@validate_num
def kun28(fuck_time):
    """
    刷狗粮 困28前两个
    """
    print("*" * 10 + "开始刷狗粮" + "*" * 10)
    time.sleep(2)
    res = screen_shot("img/28zhang.png")
    if res.max() > 0.7:
        pag.click(x=1520 + random.choice([5, 7, 2, 6, 3]), y=800 + random.choice([5, 7, 2, 6, 3]))
        time.sleep(2)
        for i in range(fuck_time):
            print("第%s次刷困28" % str(i + 1))
            res = screen_shot("img/28mianlingqi.png")
            if res.max() > 0.7:
                pag.click(x=1300 + random.choice([5, 7, 2, 6, 3]), y=735 + random.choice([5, 7, 2, 6, 3]))
                time.sleep(random.choice([2, 2.1, 2.01, 2.12, 2.08]))
                res = screen_shot("img/28goutou.png")
                if res.max() > 0.7:
                    for i in [1280, 1570]:
                        pag.click(x=i + random.choice([5, 7, 2, 6, 3]), y=470 + random.choice([5, 7, 2, 6, 3]))
                        time.sleep(random.choice([18, 19, 18.6, 18.4, 19.1]))
                        pag.click(x=928 + random.choice([5, 7, 2, 6, 3]), y=780 + random.choice([5, 7, 2, 6, 3]))
                        time.sleep(random.choice([2.0, 2.1, 2.2, 2.13, 2.22]))
                    pag.click(x=302 + random.choice([5, 7, 2, 6, 3]), y=220 + random.choice([5, 7, 2, 6, 3]))
                    time.sleep(random.choice([0.99, 1.08, 1.12, 1.1]))
                    pag.click(x=1100 + random.choice([5, 7, 2, 6, 3]), y=600 + random.choice([5, 7, 2, 6, 3]))
                    time.sleep(random.choice([2, 2.1, 2.01, 2.12, 2.08]))
        pag.click(x=1416 + random.choice([5, 7, 2, 6, 3]), y=310 + random.choice([5, 7, 2, 6, 3]))


def menu():
    print("*" * 10 + "阴阳师Hands Free" + "*" * 10)
    print("*" * 10 + "1. 御魂" + "*" * 10)
    print("*" * 10 + "2. 困28" + "*" * 10)
    print("*" * 10 + "0. 退出" + "*" * 10)


if __name__ == '__main__':
    while True:
        menu()
        choice = input("请选择:")
        choice = int(choice)
        if choice == 1:
            yuhun()
        if choice == 2:
            kun28()
        if choice == 0:
            break
