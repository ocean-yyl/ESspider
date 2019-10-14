from baiduAPI.API.client import get_AipNlp_client
import re
import logging
import time
# 解析一个文档的json
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename=str(time.ctime()).replace(":","-")+".log",
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
def get_sentiment(client,text):
	try:
		res = client.sentimentClassify(text)
		logging.info(res)
		sentiment_num = re.findall('sentiment.:.(\d+)',str(res))[0]
		return int(sentiment_num)
	except Exception as e:
		print(e)
		return -1

if __name__ == '__main__':
	client = get_AipNlp_client()
	num = get_sentiment(client,"效果不错")
	print(num)


