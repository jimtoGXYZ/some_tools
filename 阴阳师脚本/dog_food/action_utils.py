import os
import threading

import cv2
import time
import pyautogui as pag
import random

from PIL import ImageGrab

change_flag = False


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
    full_screen_img.save("img/screen_shot/1.png", "PNG")
    full_screen_img = cv2.imread("img/screen_shot/1.png", 0)
    temp_img = cv2.imread(temp_path, 0)
    res = cv2.matchTemplate(temp_img, full_screen_img, cv2.TM_CCOEFF_NORMED)
    # print(res.max())
    return res


def get_click_pos(file_path, threshold=0.7):
    """
    获取点击位置
    若可信度达到threshold则根据图片宽高计算点击位置
    否则返回 None
    :param file_path: 需要比对的图片路径
    :return: click_pos：元组 ==> （x,y）
    """
    res = screen_shot(file_path)
    print(res.max())
    if res.max() > threshold:
        image = cv2.imread(file_path)
        h, w = image.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        click_pos = (250 + top_left[0] + w / 2 + random.choice([1, 2, 3, 4, 5, 6]),
                     140 + top_left[1] + h / 2 + random.choice([1, 2, 3, 4, 5, 6]))
        return click_pos
    else:
        return None


def click_action(file_path, sleep_time=0.0, x_offset=0, y_offset=0, click_times=1):
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
        print("准备点击", file_path)
        pag.click(x=click_pos[0] + x_offset, y=click_pos[1] + y_offset, clicks=click_times)
        time.sleep(sleep_time + random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))
    else:
        time.sleep(1)


def exp_buff():
    """
    打开阴阳师经验buff
    :return: None
    """
    # 打开buff菜单
    click_action("img/gouliang/jiacheng.png", 0.1)
    # 打开100%buff
    click_action("img/gouliang/jingyan100.png", 0, 130)
    # 打开50%buff
    click_action("img/gouliang/jingyan50.png", 0, 130)
    # 关闭buff菜单
    pag.click(x=1350, y=530)


def slide_screen():
    """
    滑动怪物界面屏幕
    :return: None
    """
    # 匹配图片定位坐标
    click_pos = get_click_pos("img/gouliang/qiangjiao.png")
    # 点击墙角改变鼠标坐标
    pag.click(x=click_pos[0], y=click_pos[1])
    # 鼠标移动
    # pag.moveTo(x=click_pos[0], y=click_pos[1], duration=1, tween=pag.easeInOutQuad)
    # 拖拽鼠标
    pag.dragTo(x=300, y=click_pos[1], duration=random.choice([0.7, 0.6, 0.78]), button='LEFT')


def watching_given_pic(file_path):
    """
    由子线程负责监听指定图片 当监听到指定图片后点击然后结束线程
    :param file_path: 图片路径
    :return: None
    """
    while True:
        res = screen_shot(file_path)
        if res.max() > 0.7:
            # 不知为何多个线程可能有冲突 所以需要睡眠并且重复点击一次才能保证流程不中断
            click_action(file_path, click_times=2)
            time.sleep(0.1)
            click_action(file_path, click_times=1)
            return


def wait_4_battle_N_click():
    """
    原来需要计算时间去点击 但是yys存在两次完全相同动画时间不同的情况 所以改用watching_given_pic
    本方法作废
    等待战斗结束 并点击屏幕
    :return: None
    """
    print("等待战斗时间")
    time.sleep(random.choice([9, 9.4, 9.2, 9.6, 10]))
    click_action("../img/gouliang/jingong_pic/shengli.png", 3.3)
    click_action("../img/gouliang/jingong_pic/jubaopen.png", 1.5)


def quit_battle_field():
    """
    退出战场
    :return: None
    """
    # 检测不到怪物 退出
    click_action("img/gouliang/tuichu.png", 0.5)
    # 点击确认
    click_action("img/gouliang/queren.png", 1.5)


def cal_battle_pos(pos):
    """
    根据pos计算最近的战斗图标坐标
    :param pos: 特定战斗目标类型位置
    :return: click_pos/None
    """
    # -----------------以下为识别普通指定怪逻辑---------------------
    # 以EXP图为中心 左右130 高250截图
    res = screen_shot("img/gouliang/jingong_pic/zhandou.png", x=pos[0] - 200, y=pos[1] - 300, x_width=pos[0] + 200,
                      y_width=pos[1])
    if res.max() > 0.7:
        image = cv2.imread("img/gouliang/jingong_pic/zhandou.png")
        h, w = image.shape[:2]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 战斗图标在小图中坐标的左上角
        top_left = max_loc
        # 计算出战斗图标在小图中的坐标
        click_pos = (pos[0] - 200 + top_left[0] + w / 2,
                     pos[1] - 300 + top_left[1] + h / 2)
        print("计算出战斗图标位置：", click_pos)
        return click_pos

    # -----------------以下为识别boss逻辑-------------------------
    else:
        # 若找不到普通特定类型怪 则全屏找boss
        res = screen_shot("img/gouliang/jingong_pic/shoulingjingong.png")
        if res.max() > 0.7:
            return get_click_pos("img/gouliang/jingong_pic/shoulingjingong.png")
        # 既无指定怪也无boss 返回None
        else:
            return None


class multi_cv2(threading.Thread):
    """
    该类负责使用cv2扫描指定路径下所有图片并返回坐标
    继承threading.Thread 可以通过多线程调用减少主线程时间损耗
    为防止主线程比子线程跑得快，需要将子线程设置为守护线程


        t = multi_cv2(base_path)
        t.start()
        t.join()
        pos = t.get_pos()
    """

    def __init__(self, base_path):
        super(multi_cv2, self).__init__()
        self.base_path = base_path
        self.pos = None

    def run(self):
        print("子线程负责扫描文件夹中的图片")
        file_name_list = os.listdir(self.base_path)
        file_list = []
        for name in file_name_list:
            file_list.append(os.path.join(self.base_path, name).replace('\\', '/'))
        print(file_list)

        # 打乱顺序
        random.shuffle(file_list)
        # 匹配四张经验图片 获取exp的位置
        for file in file_list:
            tmp = get_click_pos(file, 0.48)
            if self.pos is not None:
                break
            if tmp is not None:
                self.pos = tmp

    def get_pos(self):
        try:
            return self.pos
        except Exception as e:
            print(e)
            return None


def change_mon():
    """
    未完成
    换人动作
    :return: None
    """
    time.sleep(1.6)
    # 转场
    pag.click(x=818 + random.choice([3, 4, 5, 8, 9, 7]), y=634 + random.choice([3, 4, 5, 8, 9, 7]), clicks=2)
    # 点击换卡
    t = threading.Thread(target=watching_given_pic, args=("img/gouliang/quanbu.png",))
    t.run()
    time.sleep(0.5)
    # 点击n卡
    t = threading.Thread(target=watching_given_pic, args=("img/gouliang/n.png",))
    t.run()
    time.sleep(0.5)
    # 计算滑块坐标
    click_pos = get_click_pos("img/gouliang/huakuai.png")
    pag.click(x=click_pos[0], y=click_pos[1])
    # 每100像素滑动一次 直到找到1级涂壁
    for i in range(20):
        res = screen_shot("img/gouliang/tubi.png")
        print("涂壁识别度：", res.max())
        if res.max() > 0.88:
            tubi_pos = get_click_pos("img/gouliang/tubi.png")
            pag.moveTo(x=tubi_pos[0], y=tubi_pos[1], duration=0.5)
            pag.dragTo(x=474, y=510, duration=0.5, button='LEFT')
            tubi_pos = get_click_pos("img/gouliang/tubi.png")
            pag.moveTo(x=tubi_pos[0], y=tubi_pos[1], duration=0.5)
            pag.dragTo(x=958, y=535, duration=0.5, button='LEFT')
            global change_flag
            change_flag = False
            print("change_flag置False")
            return
        else:
            click_action("img/gouliang/huakuai.png")
            pag.dragTo(x=click_pos[0] + 50 * (i + 1), y=click_pos[1], duration=0.3, button='LEFT')


def watching_4_full_exp():
    """
    监听满级信号
    :return: res
    """
    for i in range(8):
        res = screen_shot("img/gouliang/fullexp.png")
        if res.max() > 0.7:
            global change_flag
            change_flag = True
            print("change_flag置True")
            break


def analyse_exp_monster():
    """
    识别经验怪位置 并点击经验怪战斗
    :return: None
    """
    while True:
        base_path = "img/gouliang/exp_pic"

        file_name_list = os.listdir(base_path)
        file_list = []
        for name in file_name_list:
            file_list.append(os.path.join(base_path, name).replace('\\', '/'))
        print(file_list)

        # 匹配四张经验图片 获取exp的位置
        pos = None
        random.shuffle(file_list)
        for file in file_list:
            tmp = get_click_pos(file, 0.48)
            if pos is not None:
                break
            if tmp is not None:
                pos = tmp

        print("最终EXP位置：", pos)
        # 若找不到EXP位置 返回主程序
        if pos is None:
            return

        # 计算战斗图标位置
        click_pos = cal_battle_pos(pos)

        if click_pos is not None:
            pag.click(x=click_pos[0], y=click_pos[1])
            time.sleep(1.6 + random.choice([0.1, 0.12, 0.09]))
            # 若change_flag=True则执行换人动作 未完成
            global change_flag
            if change_flag == True:
                change_mon()

            # 点击准备图标
            print("即将点击准备图标")
            t1 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/zhunbei.png",))
            t1.run()
            time.sleep(0.5 + random.choice([0.01, 0.02, 0.03, 0.04]))

            # 战斗等待、点击事件
            rand_time = random.choice([6, 6.4, 6.2, 6.6, 7])
            print("等待%d秒战斗时间" % rand_time)
            time.sleep(rand_time)

            t1 = threading.Thread(target=watching_4_full_exp)
            t1.run()
            t1 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/shengli.png",))
            t1.run()
            time.sleep(0.3)
            t2 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/jubaopen.png",))
            t2.run()
        else:
            quit_battle_field()
            return


def analyse_monster():
    """
    无差别攻击 只识别怪物
    :return:
    """
    while True:
        # 找boss
        click_pos = get_click_pos("img/gouliang/jingong_pic/shoulingjingong.png")
        if click_pos is None:
            # 没boss找普通怪
            click_pos = get_click_pos("img/gouliang/jingong_pic/zhandou.png")

        if click_pos is not None:
            pag.click(x=click_pos[0], y=click_pos[1])
            time.sleep(1.6 + random.choice([0.1, 0.12, 0.09]))
            # 监听是否有满级信号
            t1 = threading.Thread(target=watching_4_full_exp)
            t1.run()
            # 若change_flag=True则执行换人动作 未完成
            global change_flag
            if change_flag == True:
                change_mon()

            # 点击准备图标
            print("点击准备图标")
            t1 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/zhunbei.png",))
            t1.run()
            time.sleep(0.5 + random.choice([0.01, 0.02, 0.03, 0.04]))

            # 战斗等待、点击事件
            rand_time = random.choice([6, 6.4, 6.2, 6.6, 7])
            print("等待%d秒战斗时间" % rand_time)
            time.sleep(rand_time)


            t1 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/shengli.png",))
            t1.run()
            time.sleep(0.3)
            t2 = threading.Thread(target=watching_given_pic, args=("img/gouliang/jingong_pic/jubaopen.png",))
            t2.run()
        else:
            quit_battle_field()
            return