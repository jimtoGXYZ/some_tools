import os
import random
import threading

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
    # print(res.max())
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


# @validate_num
# def kun28(fuck_time):
#     """
#     刷狗粮
#     """
#     print("*" * 10 + "开始刷狗粮" + "*" * 10)
#     time.sleep(2)
#     res = screen_shot("img/28zhang.png")
#     if res.max() > 0.7:
#         pag.click(x=1520 + random.choice([5, 7, 2, 6, 3]), y=800 + random.choice([5, 7, 2, 6, 3]))
#         time.sleep(2)
#         for i in range(fuck_time):
#             print("第%s次刷困28" % str(i + 1))
#             res = screen_shot("img/28mianlingqi.png")
#             if res.max() > 0.7:
#                 pag.click(x=1300 + random.choice([5, 7, 2, 6, 3]), y=735 + random.choice([5, 7, 2, 6, 3]))
#                 time.sleep(random.choice([2, 2.1, 2.01, 2.12, 2.08]))
#                 res = screen_shot("img/28goutou.png")
#                 if res.max() > 0.7:
#                     pag.moveTo(x=1600, y=290, duration=1, tween=pag.easeInOutQuad)
#                     pag.dragTo(x=300, y=290, duration=1, button='LEFT')
#                     while True:
#                         res = screen_shot("img/zhandou.png")
#                         if res.max() < 0.7:
#                             break
#                         zhandou_image = cv2.imread("img/zhandou.png")
#
#                         h, w = zhandou_image.shape[:2]
#
#                         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#                         top_left = max_loc
#
#                         click_pos = (250 + top_left[0] + w / 2, 140 + top_left[1] + h / 2)
#                         print("计算出战斗位置:", click_pos)
#                         # 点击怪物战斗图标
#                         pag.click(x=click_pos[0], y=click_pos[1])
#                         time.sleep(random.choice([18, 19, 18.6, 18.4, 19.1]))
#                         pag.click(x=928 + random.choice([5, 7, 2, 6, 3]), y=780 + random.choice([5, 7, 2, 6, 3]))
#                         time.sleep(random.choice([2.0, 2.1, 2.2, 2.13, 2.22]))
#
#                     # 退出副本 左上角x
#                     pag.click(x=302 + random.choice([5, 7, 2, 6, 3]), y=220 + random.choice([5, 7, 2, 6, 3]))
#                     time.sleep(random.choice([0.99, 1.08, 1.12, 1.1]))
#                     # 点击确定
#                     pag.click(x=1100 + random.choice([5, 7, 2, 6, 3]), y=600 + random.choice([5, 7, 2, 6, 3]))
#                     time.sleep(random.choice([2, 2.1, 2.01, 2.12, 2.08]))
#
#         # 结束循环
#         pag.click(x=1416 + random.choice([5, 7, 2, 6, 3]), y=310 + random.choice([5, 7, 2, 6, 3]))


def exp_buff():
    # 打开buff菜单
    click_action("img/gouliang/jiacheng.png", 0.1)
    # 打开100%buff
    click_action("img/gouliang/jingyan100.png", 0, 130)
    # 打开50%buff
    click_action("img/gouliang/jingyan50.png", 0, 130)
    # 关闭buff菜单
    pag.click(x=1350, y=530)


def slide_screen():
    # 匹配图片定位坐标
    click_pos = get_click_pos("img/gouliang/qiangjiao.png")
    # 鼠标移动
    pag.moveTo(x=click_pos[0], y=click_pos[1], duration=1, tween=pag.easeInOutQuad)
    # 拖拽鼠标
    pag.dragTo(x=300, y=click_pos[1], duration=1, button='LEFT')


def slide_to_pic(file_name):
    """
    移动鼠标到图片位置
    """
    # 获得图片位置
    pos = get_click_pos(file_name)
    # 鼠标移动到图片位置
    pag.moveTo(x=pos[0], y=pos[1], duration=0.5, tween=pag.easeInOutQuad)
    return pos


def is_full_level():
    """
    检测是否满级
    """
    res = screen_shot("img/gouliang/man.png")
    print("满级可信度检测", res.max())
    if res.max() > 0.701:
        # 若满级点击满级图标
        time.sleep(1)
        pag.click(x=790, y=600)
        time.sleep(1)
        print("已点击满及图标")
        # 点击全部
        pag.click(x=325, y=875)
        time.sleep(1)
        print("已点击全部")
        # 点击N
        pag.click(x=435, y=525)
        time.sleep(1)
        print("已点击N")
        # 移动鼠标到滑块
        pag.click(x=460, y=910)
        print("已滑动到滑块")
        # 拖拽滑块右移650
        pag.dragTo(x=1110, y=910, duration=1, button='LEFT')
        # 定位涂壁
        pos = slide_to_pic("img/gouliang/tubi.png")
        # 拖拽到指定位置
        pag.dragTo(x=470, y=470, duration=0.5, button='LEFT')
        # 定位涂壁2
        pos = slide_to_pic("img/gouliang/tubi.png")
        # 拖拽到指定位置2
        pag.dragTo(x=950, y=500, duration=0.5, button='LEFT')


@validate_num
def kun28(fuck_time):
    time.sleep(2)
    print("*" * 10 + "开始刷狗粮" + "*" * 10)
    # 点击探索
    click_action("img/gouliang/tansuo.png", 1.5)
    # 打开经验buff
    exp_buff()
    for i in range(fuck_time):
        print("第%s次狗粮" % str(i + 1))
        # 点击28章
        click_action("img/gouliang/28zhang.png", 2)
        # 点探索
        click_action("img/gouliang/tansuo2.png", 1)
        # 移动鼠标
        slide_screen()
        # 检测可进攻的怪物
        while True:
            # 找boss
            click_pos = get_click_pos("img/gouliang/jingong_pic/shoulingjingong.png")
            if click_pos is None:
                # 没boss找普通怪
                click_pos = get_click_pos("img/gouliang/jingong_pic/zhandou.png")
            # 都没有则退出循环
            if click_pos is None:
                break
            # 有怪 打怪
            pag.click(x=click_pos[0], y=click_pos[1])
            time.sleep(random.choice([10, 10.4, 10.2, 10.6, 11]))
            click_action("img/gouliang/jingong_pic/shengli.png", 3.3)
            click_action("img/gouliang/jingong_pic/jubaopen.png", 1.5)

        # 检测不到怪物 退出
        click_action("img/gouliang/tuichu.png", 0.5)
        # 点击确认
        click_action("img/gouliang/queren.png", 1.5)

    # 关闭经验buff
    exp_buff()


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


def get_throw_pos(file_path):
    """
    返回丢豆子的位置
    """
    res = screen_shot(file_path)
    if res.max() > 0.7:
        image = cv2.imread(file_path)
        h, w = image.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        click_pos = (250 + top_left[0] + w / 2, 140 + top_left[1] + h / 2)
        print("识别位置", click_pos)

        # 画图
        # image = cv2.imread("D:/My_IDE/MyNote/1.png")
        # btn_right = (top_left[0] + w, top_left[1] + h)
        # cv2.rectangle(image, top_left, btn_right, (0, 255, 0), 2)
        # cv2.imwrite("D:/My_IDE/MyNote/2.png", image)
        # cv2.imshow("imag1", image)
        # cv2.waitKey(-1)

    else:
        click_pos = (
            1580 + random.choice([1, 2, 3, 4, 5, 6, 9, 8, 7, 11]), 550 + random.choice([1, 2, 3, 4, 5, 6, 9, 8, 7, 11]))

    return click_pos


def click_action(file_path, sleep_time=0, x_offset=0, y_offset=0):
    """
    点击
    """
    click_pos = get_click_pos(file_path)
    if click_pos is not None:
        pag.click(x=click_pos[0] + x_offset, y=click_pos[1] + y_offset)
        time.sleep(sleep_time + random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))
    else:
        time.sleep(1)


def click_action_2(file_path):
    """
    砸豆点击
    """
    click_pos = get_throw_pos(file_path)
    pag.click(x=click_pos[0], y=click_pos[1])
    time.sleep(random.choice([0.19, 0.2, 0.3, 0.4, 0.45]))


def choose_up_animal():
    """
    选up怪
    """
    pag.click(x=random.choice([580, 966, 1360]), y=670)
    time.sleep(0.2)


def watching_ssr():
    """
    监听ssr出现 控制点击事件砸豆
    """
    base_path = "img/zapiao/ssr"
    tmp_list = os.listdir(base_path)
    file_list = []
    for i in tmp_list:
        file_list.append(os.path.join(base_path, i).replace("\\", "/"))

    while True:
        for file in file_list:
            click_action_2(file)


def watching_baigui_over():
    """
    监听砸票是否结束
    """
    while True:
        click_action("img/zapiao/tips/baiguiqiyueshu.png", 1.8)


def watching_buff():
    """
    监听buff鸟
    """
    base_path = "img/zapiao/buff"
    tmp_list = os.listdir(base_path)
    buff_img_list = []
    for i in tmp_list:
        buff_img_list.append(os.path.join(base_path, i).replace("\\", "/"))
    while True:
        for file in buff_img_list:
            click_action_2(file)


@validate_num
def zapiao(fuck_time):
    """
    砸票
    """
    time.sleep(2)
    print("*" * 10 + "开始砸票" + "*" * 10)
    # 点击町中
    click_action("img/zapiao/tips/tingzhong.png", 2)
    # 点击百鬼夜行灯笼
    click_action("img/zapiao/tips/baiguiyexing.png", 1)
    for i in range(fuck_time):
        print("第%s次砸票" % str(i + 1))
        # 点好友+号
        click_action("img/zapiao/tips/yaoqinghaoyou.png", 0.5)
        # 选择好友
        click_action("img/zapiao/tips/xuanzehaoyou.png", 0.5)
        # 进入
        click_action("img/zapiao/tips/jinru.png", 1.5)
        # 选up怪
        # click_action("img/zapiao/tips/xuanren.png", 0)
        choose_up_animal()
        # 点击开始
        click_action("img/zapiao/tips/kaishi.png", 1.5)
        time.sleep(4)
        # 开线程 监听ssr 自动砸豆
        t1 = threading.Thread(target=watching_ssr, name="watching_ssr1")
        t1.run()
        # 监听游戏结束
        t2 = threading.Thread(target=watching_baigui_over, name="watching_baigui_over1")
        t2.run()
        # 监听buff鸟
        t3 = threading.Thread(target=watching_buff, name="watching_buff")
        t3.run()

        time.sleep(60)


def menu():
    print("*" * 10 + "阴阳师Hands Free" + "*" * 10)
    print("*" * 10 + "1. 御魂" + "*" * 10)
    print("*" * 10 + "2. 困28" + "*" * 10)
    print("*" * 10 + "3. 砸豆" + "*" * 10)
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
        if choice == 3:
            zapiao()
        if choice == 0:
            break
