import os
import random
import threading
import cv2
import time
from PIL import ImageGrab
import pyautogui as pag


def shot_loc():
    """
    通过图片匹配位置可以确定坐标
    """

    time.sleep(2)

    full_image = ImageGrab.grab(bbox=(250, 140, 1670, 940))
    full_image.save("img/1.png", "PNG")
    full_image = cv2.imread("img/1.png", 0)
    btn_image = cv2.imread("img/28zhang.png", 0)

    res = cv2.matchTemplate(btn_image, full_image, cv2.TM_CCOEFF_NORMED)
    print("可信度:", res.max())

    h, w = btn_image.shape[:2]
    print("小图高:", h, "小图宽:", w)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)

    top_left = max_loc
    btn_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(full_image, top_left, btn_right, (255, 0, 0), 2)
    cv2.imshow("full_image", full_image)
    cv2.waitKey(-1)


def screen_shot(temp_path, x=250, y=140, x_width=1670, y_width=940):
    full_screen_img = ImageGrab.grab(bbox=(x, y, x_width, y_width))
    # 必须全英文路径
    full_screen_img.save("D:/My_IDE/MyNote/1.png", 'PNG')
    full_screen_img = cv2.imread("D:/My_IDE/MyNote/1.png", 0)
    temp_img = cv2.imread(temp_path, 0)
    res = cv2.matchTemplate(temp_img, full_screen_img, cv2.TM_CCOEFF_NORMED)
    print(res.max())
    return res


def get_click_pos(file_path):
    """
    返回点击位置 类型元组
    """
    res = screen_shot(file_path)
    if res.max() > 0.7:
        image = cv2.imread(file_path)
        h, w = image.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        click_pos = (250 + top_left[0] + w / 2, 140 + top_left[1] + h / 2)
        return click_pos
    else:
        return None


def click_action(file_path, sleep_time=0, x_offset=0, y_offset=0):
    """
    砸票重复点击
    """
    click_pos = get_click_pos(file_path)
    if click_pos is not None:
        pag.click(x=click_pos[0] + x_offset, y=click_pos[1] + y_offset)
        time.sleep(sleep_time + random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))


def watching_ssr():
    """
    监听ssr
    """
    base_path = "img/zapiao/test"
    tmp_list = os.listdir(base_path)
    file_list = []
    for i in tmp_list:
        file_list.append(os.path.join(base_path, i).replace("\\", "/"))
    print(file_list)

    while True:
        for file in file_list:
            print(file)
            click_action(file)


def slide_screen():
    # 匹配图片定位坐标
    click_pos = get_click_pos("img/gouliang/qiangjiao.png")
    # 鼠标移动
    pag.moveTo(x=click_pos[0], y=click_pos[1], duration=1, tween=pag.easeInOutQuad)
    # 拖拽鼠标
    pag.dragTo(x=300, y=click_pos[1], duration=1, button='LEFT')


def exp_buff():
    # 打开buff菜单
    click_action("img/gouliang/jiacheng.png", 0.1)
    # 打开100%buff
    click_action("img/gouliang/jingyan100.png", 0, 130)
    # 打开50%buff
    click_action("img/gouliang/jingyan50.png", 0, 130)
    # 关闭buff菜单
    pag.click(x=1350, y=530)


def kun28(fuck_time):
    time.sleep(2)
    print("*" * 10 + "开始刷狗粮" + "*" * 10)
    # 点击探索
    click_action("img/gouliang/tansuo.png", 1.5)
    # 打开经验buff
    exp_buff()
    for i in range(fuck_time):
        # 点击28章
        click_action("img/gouliang/28zhang.png", 2)
        flag = True
        # 点探索
        click_action("img/gouliang/tansuo2.png", 1)
        # 移动鼠标
        slide_screen()
        # 检测可进攻的怪物
        while True:
            # 找普通怪
            click_pos = get_click_pos("img/gouliang/jingong_pic/zhandou.png")
            if click_pos is None:
                # 没有普通怪找boss
                click_pos = get_click_pos("img/gouliang/jingong_pic/shoulingjingong.png")
                if click_pos is not None:
                    flag = False
            # 都没有则退出循环
            if click_pos is None:
                break
            # 有怪 打怪
            pag.click(x=click_pos[0], y=click_pos[1])
            time.sleep(random.choice([10, 10.4, 10.2, 10.6, 11]))
            click_action("img/gouliang/jingong_pic/shengli.png", 3.3)
            click_action("img/gouliang/jingong_pic/jubaopen.png", 1.5)

        if flag == False:
            # 检测不到怪物 退出
            click_action("img/gouliang/tuichu.png", 0.5)
            # 点击确认
            click_action("img/gouliang/queren.png", 1.5)
        else:
            time.sleep(0.5)

    # 关闭经验buff
    exp_buff()


if __name__ == '__main__':
    # shot_loc()
    time.sleep(2)
    # t1 = threading.Thread(target=watching_ssr, name="watching_ssr1")
    # t1.run()
    # watching_ssr()
    kun28(2)
