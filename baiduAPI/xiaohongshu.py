from baiduAPI.getApi import get_sentiment
from baiduAPI.API.client import get_AipNlp_client
import time
if __name__ == '__main__':
    client = get_AipNlp_client()
    sentiments_list = []
    flagline = "code18813015780-for-rplace\n"
    with open("resultdata_xiaohongshu_temp.txt",encoding="utf-8") as f:
        pages = f.read()
    page_list = pages.split(flagline)

    for i in range(len(page_list)):
        num = get_sentiment(client, page_list[i].encode("gbk","ignore").decode("gbk"))
        sentiments_list.append(str(num))
        time.sleep(2)

    with open("xiaohongshu_sentiments.txt","w",encoding="utf-8") as f2:
        f2.write("\n".join(sentiments_list))

