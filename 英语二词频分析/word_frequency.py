from wordcloud import WordCloud
import jieba as jb
import os
from docx import Document


def read_DOCX(base_path, file_name):
    document = Document(base_path + file_name)
    full_text = ""
    for paragraph in document.paragraphs:
        # print(paragraph.text)
        full_text += paragraph.text
    return full_text


def is_alphabet(char):
    if (char >= '\u0041' and char <= '\u005a') or (char >= '\u0061' and char <= '\u007a'):
        return True
    else:
        return False


def draw_wordCloud(total_text):
    WC = WordCloud(width=940, height=1080, background_color="white")
    WC.generate(total_text)
    WC.to_file("./data/wordCloud.png")


def read_exclude_text():
    file_path = "./data/exclud_words.txt"
    exclude_list = []
    for line in open(file_path):
        exclude_list.append(line.strip('\r\n'))
    return exclude_list

if __name__ == '__main__':
    base_path = "D:/My_IDE/PyCharm/Project/python_basic/英语二词频分析/data/English_2_new/"
    file_name_list = os.listdir(base_path)
    total_word_dict = {}
    total_text = ""
    exclude_list = read_exclude_text()
    # 1' 读取文件
    for file_name in file_name_list:
        full_text = read_DOCX(base_path, file_name)
        total_text += full_text
        # 2' 分词
        word_list = jb.cut(full_text)
        for word in word_list:
            if is_alphabet(word):
                total_word_dict[word] = total_word_dict.get(word, 0) + 1
    print(total_word_dict)
    # 按频次排序
    total_word_list = sorted(total_word_dict.items(), key=lambda x: x[1], reverse=True)
    print(total_word_list)
    for item in total_word_list:
        # 找对应翻译
        # 找不到接口批量翻译，可以尝试破解百度翻译的接口遍历实现
        # 转字符串
        if item[0] not in exclude_list:
            item = str(item[0]) + " " + str(item[1])

            with open("word_frequency.txt", 'a', encoding='utf-8') as f:
                f.write(item + "\n")

    # 3' 词云
    draw_wordCloud(total_text)
