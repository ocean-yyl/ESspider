bad = 0
good = 0
middle = 0
erro = 0

with open("xiaohongshu_sentiments.txt", encoding="utf-8") as f:
	lines = f.readlines()

for i in lines:
	i = int(i.strip())
	if i == 0:
		bad += 1
	elif i == 1:
		middle += 1
	elif i == 2:
		good += 1
	elif i == -1:
		erro += 1
	else:
		print(i)
		print("超出范围")

sum = good+bad+middle

print("积极态度：",good,"\t",good/sum)
print("中间态度：",middle,"\t",middle/sum)
print("消极态度",bad,"\t",bad/sum)
print("情感分析错误：",erro)
