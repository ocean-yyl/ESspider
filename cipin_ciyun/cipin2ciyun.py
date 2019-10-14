import jieba
from matplotlib import pyplot as plt  # 数据可视化
from wordcloud import WordCloud  # 词云


# stop_word_list
def get_stop_words():
    my_add_extend_stop_word_list = [
        "\n","\t", " ", "\r", "～","…",
        "~","[","]",'"',"#","@","+","-","⃣ ","—","🔸","3D",'',
    ] # 自定义stop_words

    stopwordlist = []
    with open("stop_words_chinaese.txt",encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                stopwordlist.append(line.strip())
    stopwordlist.extend(my_add_extend_stop_word_list)
    return stopwordlist


# 获取词频
def cipin(file,Max_num):  # 输出词频前N的词语
    txt = open(file, "r", encoding="utf-8").read()  # 打开文件
    jieba.load_userdict("words.txt") # 加载自定义词典
    words = jieba.lcut(txt,cut_all=True)  # 精确模式，返回一个列表
    counts = {}  # 创建字典
    excludes = get_stop_words() # 规定要去除的没意义的词语
    for word in words:
        if len(word) == 1:  #把意义相同的词语归一
            continue
        elif word == "3D口腔扫描" or word == "3D扫描牙齿":
            rword = "3D口扫"
        elif word == '3D建模' or word == '口扫':
            rword = '3D口扫'
        elif word == '口扫仪器' or word == '扫描仪器':
            rword = '扫描枪'
        else:
            rword = word
        counts[rword] = counts.get(rword,0) + 1     #字典的运用，统计词频
    # for word in words:
    #     counts[word] = counts.get(word, 0) + 1  # 字典的运用，统计词频
    for word in excludes:  # 删除之前所规定的词语
        try:
            counts.pop(word)
        except:
            pass

    items = list(counts.items())  # 返回所有键值对
    items.sort(key=lambda x: x[1], reverse=True)  # 降序排序
    wordlist = []
    cipinlist = []
    if Max_num > len(items):
        print("Max_num过大，总词数为：",len(items))
        Max_num = len(items)
    for i in range(Max_num):
        word, count = items[i]
        str = "{0:<10}{1:<5}".format(word, count)  # 输出前N个词频的词语
        cipinlist.append(str) # 词频
        wordlist.append(word)  # 把词语word放进一个列表

    return wordlist,cipinlist

# 生成词云
def create_word_cloud(filename,Max_num):
    wordlist,cipinlist = cipin(filename,Max_num) #调用函数获取wordlist
    with open(filename+"_词频.txt","w",encoding="utf-8") as f2:
        f2.write("\n".join(cipinlist))

    wl = " ".join(wordlist)
                                    #图片名字 需一致
    # cloud_mask = plt.imread("love.jpg")#词云的背景图，需要颜色区分度高

    wc = WordCloud(
        background_color = "black", #背景颜色
        # mask = cloud_mask,          #背景图cloud_mask
        max_words=Max_num,              #最大词语数目
        font_path="simkai.ttf",  # ***中文字体，解决不能识别中文文字问题.调用font里的simsun.tff字体，需要提前安装
        height=1200,                #设置高度
        width=1600,                 #设置宽度
        max_font_size=1000,         #最大字体号
        min_font_size=20,           #最小字体号
		collocations=True,  # 是否包括两个词的搭配
        ).generate(wl)  # 用 wl的词语 生成词云
    # 展示词云图

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file(filename+'_ciyun.jpg')  # 把词云保存下当前目录（与此py文件目录相同）

if __name__ == '__main__':
    create_word_cloud("datas/resultdata_dianping",Max_num=100)
    create_word_cloud("datas/resultdata_weibo", Max_num=100)
    create_word_cloud("datas/resultdata_xiaohongshu", Max_num=100)
