import os
import random
import threading
import cv2
import time
import pyautogui as pag

from PIL import ImageGrab
import action_utils


class dog_food:

    def __init__(self, times):
        self.times = times

    def run(self):
        pass


if __name__ == '__main__':
    time.sleep(2)
    # 主界面点击探索
    action_utils.click_action("../img/gouliang/tansuo.png", 2)
    # 打开buff
    action_utils.exp_buff()
    for i in range(3):
        # 点击28章
        action_utils.click_action("../img/gouliang/28zhang.png", 2)
        # 点击探索
        action_utils.click_action("../img/gouliang/tansuo2.png", 1.5)
        # 滑动屏幕
        action_utils.slide_screen()
        # 识别经验怪 点击战斗
        action_utils.analyse_exp_monster()
    # 关闭buff
    action_utils.exp_buff()
