import re
'''
SimpleTokenizerV1是基于训练集对文本进行 分词和 反分词 的分词器
分词encode()是将字符转分词ID
反分词 decode()将词组ID转换回字符

这个分词器会有一个问题，如果vocab词组（训练集）中没有hello等单词的ID，那么会报错

'''
class SimpleTokenizerV1:
    def __init__(self, vocab):
        #  字符转数字
        self.str_to_int = vocab
        # 转换成词典格式{1:"a",2:"b"}
        # 数字转字符
        self.int_to_str =  {i:s for s,i in vocab.items()}
    
    def encode(self, text):
         preprocessed = re.split(r"([,.:;?!_()'\"]|--|\s)",text)
         preprocessed = [ item.strip() for item in preprocessed if item.strip()]
         ids = [self.str_to_int[s] for s in preprocessed]
         return ids
    
    # 将词组ID转换回字符
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # 移除特定标点符号前的空格, \1为分组1
        text = re.sub(r"\s+([,.?!()'\"])", r'\1', text)
        return text


# s = SimpleTokenizerV1({1:"Hello",2:"I",3:"robot"})
# idx = s.encode("Hello, I robot")
# print(idx)