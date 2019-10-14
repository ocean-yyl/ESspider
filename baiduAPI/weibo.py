from baiduAPI.getApi import get_sentiment
from baiduAPI.API.client import get_AipNlp_client
import time
if __name__ == '__main__':
	client = get_AipNlp_client()
	sentiments_list = []
	with open("resultdata_weibo",encoding="utf-8") as f:
		while True:
			time.sleep(2)
			line = f.readline()
			if not line:
				break
			else:
				num = get_sentiment(client, line.encode("gbk","ignore").decode("gbk"))
				sentiments_list.append(str(num))
	with open("weibo_sentiments.txt", "w", encoding="utf-8") as f2:
		f2.write("\n".join(sentiments_list))