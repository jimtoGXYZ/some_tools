import os
import win32com.client as wc


def read_word(base_path, file_name_list):
    print(file_name_list)
    for file_name in file_name_list:
        word = wc.Dispatch('Word.Application')
        print(base_path + file_name + ".doc")
        doc = word.Documents.Open(base_path + file_name + ".doc")
        doc.SaveAs("D:/My_IDE/PyCharm/Project/python_basic/英语二词频分析/data/English_2_new/" + file_name + ".docx", 12,
                   False,
                   "", True, "", False, False, False, False)
    doc.Close()
    word.Quit()


if __name__ == '__main__':
    base_path = "D:/My_IDE/PyCharm/Project/python_basic/英语二词频分析/data/English_2_origin/"
    file_name_list = []
    for file_name in os.listdir(base_path):
        print(base_path + file_name)
        if file_name.endswith(".doc"):
            file_name_list.append(file_name.replace(".doc", ""))

    read_word(base_path, file_name_list)
