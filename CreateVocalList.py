'''
CreateVocalList - 词源制作工具，主要功能：
1、下载文本
2、读取文本
3、分词：保留标点符号，去除空格、空白字符
    正则表达式的写法：re.split(r"([,.:;?!_()'\"]|--|\s)",text)
4、排序: 对词组进行去重
'''
import re
from SimpleTokenizer import *
class CreateVocalList:
    def __init__(self,txtFile):
        self.file = txtFile

    # 下载文本
    def downFile():
        url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")
        file_path = "the-verdict.txt"
        urllib.request.urlretrieve(url, file_path)

    # 获取文本
    def openFile(self,file=""):
        print("====获取文本====")
        f = self.file
        if file != "":
            f = file
        # 读取文本
        with open(f, "r", encoding="utf-8" ) as f:
            raw_text = f.read()
        print("文本总字数： ", len(raw_text))
        # 获取前100个字符
        print(raw_text[:99])

        return raw_text

    # 分词：分割文本，保留逗号、句号，去除空白符号
    def regText(self,text):
        print("====分割文本====")
        # 正则加了括号()的作用：表示分割组，保留被分割的标点符号在数组中。
        result = re.split(r"([,.:;?!_()'\"]|--|\s)",text)
        # 去除空白字符
        result = [r for r in result if r.strip()]

        print("文本总大小：",len(result))
        # 打印前三十个字符
        print(result[:30])
        return result


    # 排序: 对词组进行去重、排序， set()去重复，sorted()排序
    '''
    set()去重复:
    a = ["hello","john","alex","hello"]
    a = set(a)
    output: a = ["hello","john","alex"]
    '''
    def sortText(self, result):
        print("====对词组进行排序====")
        sorted_result = sorted(set(result))

        sorted_result = self.appendTextFlag(sorted_result)

        # 获取文本词组大小
        vocab_size = len(sorted_result)
        print("词组大小：",vocab_size)
        return sorted_result
    
    # 解决未知词的问题，在VocabList最后，加入<|unk|>和<|endoftext|>
    def appendTextFlag(self, vocabList):
        vocabList.extend(["<|endoftext|>","<|unk|>"])
        return vocabList


    def getVocabList(self):
        return self.sortText(
            self.regText(
                self.openFile("the-verdict.txt")
                        )
                           )
    '''
    分词阶段
    '''
    # 为词组分配索引，词源ID
    def enumerateText(self, vocabList):
        # 通过enumerate()创建词典，自动增加序列
        vocabDict = {token:integer for integer, token in enumerate(vocabList)}
        # 打印倒数前5项
        #for i, item in enumerate(list(vocabDict.items())[-5:]):
            #print(item)
            # if i >= 6:
            #     break
        return vocabDict
    
        # 汇总上面三个方法


# 测试
createVocalList  = CreateVocalList("the-verdict.txt")
# 排序的词组
vocabList = createVocalList.getVocabList()
# 添加了序号的词组
vocabDict = createVocalList.enumerateText(vocabList)
print("=====文本分词====")
# 加载词组
simpleTokenizer = SimpleTokenizer(vocabDict)
# 对词组没有的未知词源，会自动添加 <|unk|>
text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace. "
text = " <|endoftext|> ".join((text1,text2))
idx = simpleTokenizer.encode(text)
idx_str = simpleTokenizer.decode(idx)
print("对应的词组：{0}\n对应的字符：{1}".format(idx,idx_str))
 