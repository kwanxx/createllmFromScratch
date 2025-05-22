import urllib.request
import re
'''
第一部分
1、下载文本
2、读取文本
3、分词：保留标点符号，去除空格、空白字符
    正则表达式的写法：re.split(r"([,.:;?!_()'\"]|--|\s)",text)

'''
# 下载文本
def downFile():
    url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")
    file_path = "the-verdict.txt"
    urllib.request.urlretrieve(url, file_path)

# 获取文本
def openFile(file):
    print("====获取文本====")
    # 读取文本
    with open(file, "r", encoding="utf-8" ) as f:
        raw_text = f.read()
    print("文本总字数： ", len(raw_text))
    # 获取钱100个字符
    print(raw_text[:99])

    return raw_text

# 分词：分割文本，保留逗号、句号，去除空白符号
def regText(text):
    print("====分割文本====")
    # 正则加了括号()，表示分割组，保留被分割的标点符号在数组中。
    result = re.split(r"([,.:;?!_()'\"]|--|\s)",text)
    # 去除空白字符
    result = [r for r in result if r.strip()]

    print("文本总大小：",len(result))
    # 打印前三十个字符
    print(result[:30])
    return result

# 排序: 对词组进行去重、排序， set()去重复；sorted()排序
def sortText(result):
    print("====对词组进行排序====")
    sorted_result = sorted(set(result))
    vocab_size = len(sorted_result)
    print(vocab_size)

# req()
# openFile("the-verdict.txt")
# text = "Hello, I am winky."
# regText(text)
sortText(regText(openFile("the-verdict.txt")))