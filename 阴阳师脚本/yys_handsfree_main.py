import time
from 阴阳师脚本.dog_food import action_utils

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

def menu():
    print("*" * 10 + "阴阳师Hands Free" + "*" * 10)
    print("*" * 10 + "1. 御魂" + "*" * 10)
    print("*" * 10 + "2. 困28" + "*" * 10)
    print("*" * 10 + "3. 砸豆" + "*" * 10)
    print("*" * 10 + "0. 退出" + "*" * 10)

@validate_num
def dog_food(times):
    time.sleep(2)
    # 主界面点击探索
    action_utils.click_action("img/gouliang/tansuo.png", 2)
    # 打开buff
    action_utils.exp_buff()
    for i in range(times):
        print("*" * 10 + "第%d轮狗粮" % (i + 1) + "*" * 10)
        # 点击28章
        action_utils.click_action("img/gouliang/28zhang.png", 2)
        # 点击探索
        action_utils.click_action("img/gouliang/tansuo2.png", 1.5)
        # 滑动屏幕
        action_utils.slide_screen()
        # 识别经验怪 点击战斗
        # action_utils.analyse_exp_monster()
        action_utils.analyse_monster()
    # 关闭buff
    action_utils.exp_buff()


if __name__ == '__main__':
    while True:
        menu()
        choice = input("请选择:")
        choice = int(choice)
        if choice == 1:
            # yuhun()
            pass
        if choice == 2:
            dog_food()
        if choice == 3:
            # zapiao()
            pass
        if choice == 0:
            break
