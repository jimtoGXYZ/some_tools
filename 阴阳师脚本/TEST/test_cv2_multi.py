import threading
import os


class multi_cv2(threading.Thread):

    def __init__(self, base_path):
        super(multi_cv2, self).__init__()
        self.base_path = base_path
        self.pos = None


    def run(self):
        file_name_list = os.listdir(self.base_path)
        file_list = []
        for name in file_name_list:
            file_list.append(os.path.join(self.base_path, name).replace('\\', '/'))
        print(file_list)

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