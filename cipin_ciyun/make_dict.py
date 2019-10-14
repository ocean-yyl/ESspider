# 根据words制作词典
"""
词典格式:
一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开
my_dict.txt即补充词库示例:
宜信普惠 7 n
宜信 10
极速模式 20
北京清华大学 5
李小福 2 nr
创新办 3 i
easy_install 3 eng
好用 300
韩玉赏鉴 3 nz
八一双鹿 3 nz
台中
凱特琳 nz
Edu Trust认证 2000


https://github.com/baidu/lac
词性和专名类别标签集合如下表
标签	含义		标签		含义	标签	含义		标签	含义
n	普通名词	f	方位名词	s	处所名词	t	时间
nr	人名	ns	地名	nt	机构名	nw	作品名
nz	其他专名	v	普通动词	vd	动副词	vn	名动词
a	形容词	ad	副形词	an	名形词	d	副词
m	数量词	q	量词	r	代词	p	介词
c	连词	u	助词	xc	其他虚词	w	标点符号
PER	人名	LOC	地名	ORG	机构名	TIME	时间
"""





words = []
with open("words.txt",encoding="utf-8") as f:
	while True:
		line = f.readline()
		if not line:
			break
		else:
			words.append(line.strip()+" 100000 n")

with open("my_dict.txt","w",encoding="utf-8") as f2:
	f2.write("\n".join(words))
