import re

badlines = []
with open("Sat Oct 12 19-28-49 2019.log", encoding="gbk") as f:
	while True:
		line = f.readline()
		if not line:
			break
		else:
			if "'sentiment': 0" in line:
				badlines.append(line)


with open("xiaohongshu_sentiments_bad.txt","w",encoding="utf-8") as f2:
	f2.write("".join(badlines))