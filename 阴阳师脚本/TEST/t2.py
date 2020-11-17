import os


def watching_buff():
    """
    监听buff鸟
    """
    base_path = "img/zapiao/buff"
    tmp_list = os.listdir(base_path)
    buff_img_list = []
    for i in tmp_list:
        buff_img_list.append(os.path.join(base_path, i).replace("\\", "/"))
    print(buff_img_list)


if __name__ == '__main__':
    watching_buff()