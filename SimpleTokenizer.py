import re
'''
SimpleTokenizerV1是基于训练集对文本进行 分词和 反分词 的分词器
分词encode()是将字符转分词ID
反分词 decode()将词组ID转换回字符

问题：
1、这个分词器会有一个问题，如果vocab词组（训练集）中没有hello等单词的ID，那么会报错
解决方法：
引入<|unk|>、<|endoftext|>表示未知词
<|unk|>示未知词
<|endoftext|>通常放在各个文本片段开头，指示出特定文本片段的开始或结束

'''
class SimpleTokenizer:
    def __init__(self, vocab):
        #  字符转数字,格式：{"text":token,}，例如：{"Hello":1,"I":2,"robot":3,",":4}
        self.str_to_int = vocab
        # 转换成词典格式{1:"a",2:"b"}
        # 数字转字符
        self.int_to_str =  {i:s for s,i in vocab.items()}
    
    def encode(self, text):
         # 分割字符，生成list，包括符号  
         preprocessed = re.split(r"([,.:;?!_()'\"]|--|\s)",text)
         # 去除空格
         preprocessed = [ item.strip() for item in preprocessed if item.strip()]
         # 加入未知词源标记
         preprocessed = [ item if item in self.str_to_int else '<|unk|>' for item in preprocessed]
         ids = [self.str_to_int[s] for s in preprocessed]
         return ids
    
    # 将词组ID转换回字符
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # 移除特定标点符号前的空格, \1 的意思为分组1
        text = re.sub(r"\s+([,.?!()'\"])", r'\1', text)
        return text


# s = SimpleTokenizer({"Hello":1,"I":2,"robot":3,",":4,"<|unk|>":100})
# idx = s.encode("vHello, I robot")
# str = s.decode(idx)
# print(str)