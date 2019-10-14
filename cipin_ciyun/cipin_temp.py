import jieba
import jieba.analyse

print("***案例1***"*3)
txt='那些你很冒险的梦，我陪你去疯，折纸飞机碰到雨天终究会坠落，伤人的话我直说，因为你会懂，冒险不冒险你不清楚，折纸飞机也不会回来，做梦的人睡不醒！'
Key=jieba.analyse.extract_tags(txt,topK=3)
print(Key)
#-----------------------------------------------------------------------------------
print("***案例2***"*3)
# 第一个参数：待提取关键词的文本
# 第二个参数：返回关键词的数量，重要性从高到低排序
# 第三个参数：是否同时返回每个关键词的权重
# 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
keywords = jieba.analyse.extract_tags(txt, topK=5, withWeight=True, allowPOS=())
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(item[0], item[1])


print("***案例3***"*3)
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
# 即仅提取地名、名词、动名词、动词
keywords = jieba.analyse.textrank(txt, topK=5, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# 访问提取结果
for item in keywords:
    # 分别为关键词和相应的权重
    print(item[0], item[1])