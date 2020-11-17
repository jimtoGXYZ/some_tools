import os

import cv2
import time
import pyautogui as pag
import random

from PIL import ImageGrab


def screen_shot(temp_path, x=250, y=140, x_width=1670, y_width=940):
    """
    对屏幕位置截图 并进行目标比对
    :param temp_path: 需要比对的图片路径
    :param x: 屏幕截图的x偏移量 默认250
    :param y: 屏幕截图的y偏移量 默认140
    :param x_width: 屏幕截图x宽度 默认1670
    :param y_width: 屏幕截图y高度 默认940
    :return: res：cv2.matchTemplate返回值
    """
    full_screen_img = ImageGrab.grab(bbox=(x, y, x_width, y_width))
    # 必须全英文路径
    full_screen_img.save("../img/screen_shot/1.png", 'PNG')
    full_screen_img = cv2.imread("../img/screen_shot/1.png", 0)
    temp_img = cv2.imread(temp_path, 0)
    res = cv2.matchTemplate(temp_img, full_screen_img, cv2.TM_CCOEFF_NORMED)
    # print(res.max())
    return res


def get_click_pos(file_path):
    """
    获取点击位置
    若可信度达到0.7则根据图片宽高计算点击位置
    否则返回 None
    :param file_path: 需要比对的图片路径
    :return: click_pos：元组 ==> （x,y）
    """
    res = screen_shot(file_path)
    if res.max() > 0.7:
        image = cv2.imread(file_path)
        h, w = image.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        click_pos = (250 + top_left[0] + w / 2 + random.choice([1, 2, 3, 4, 5, 6]),
                     140 + top_left[1] + h / 2 + random.choice([1, 2, 3, 4, 5, 6]))
        return click_pos
    else:
        return None


def click_action(file_path, sleep_time=0, x_offset=0, y_offset=0):
    """
    点击操作
    :param file_path: 需要点击的图片路径
    :param sleep_time: 睡眠时间
    :param x_offset: x轴偏移量
    :param y_offset: y轴偏移量
    :return: None
    """
    click_pos = get_click_pos(file_path)
    if click_pos is not None:
        pag.click(x=click_pos[0] + x_offset, y=click_pos[1] + y_offset)
        time.sleep(sleep_time + random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))
    else:
        time.sleep(1)


def exp_buff():
    """
    打开阴阳师经验buff
    :return: None
    """
    # 打开buff菜单
    click_action("../img/gouliang/jiacheng.png", 0.1)
    # 打开100%buff
    click_action("../img/gouliang/jingyan100.png", 0, 130)
    # 打开50%buff
    click_action("../img/gouliang/jingyan50.png", 0, 130)
    # 关闭buff菜单
    pag.click(x=1350, y=530)


def slide_screen():
    """
    滑动怪物界面屏幕
    :return: None
    """
    # 匹配图片定位坐标
    click_pos = get_click_pos("../img/gouliang/qiangjiao.png")
    # 点击墙角改变鼠标坐标
    pag.click(x=click_pos[0], y=click_pos[1])
    # 鼠标移动
    # pag.moveTo(x=click_pos[0], y=click_pos[1], duration=1, tween=pag.easeInOutQuad)
    # 拖拽鼠标
    pag.dragTo(x=300, y=click_pos[1], duration=random.choice([0.7, 0.6, 0.78]), button='LEFT')


def analyse_exp_monster():
    """
    识别经验怪位置 并点击经验怪战斗
    :return: None
    """
    base_path = "../img/gouliang/exp_pic"
    file_name_list = os.listdir(base_path)
    file_list = []
    for name in file_name_list:
        file_list.append(os.path.join(base_path, name).replace('\\', '/'))
    print(file_list)
    get_click_pos("../img/gouliang/exp_pic/")

def analyse_exp_monster():
    """
    识别经验怪位置 并点击经验怪战斗
    :return: None
    """
    base_path = "../img/gouliang/exp_pic"
    file_name_list = os.listdir(base_path)
    file_list = []
    for name in file_name_list:
        file_list.append(os.path.join(base_path, name).replace('\\', '/'))
    print(file_list)
    get_click_pos("../img/gouliang/exp_pic/")