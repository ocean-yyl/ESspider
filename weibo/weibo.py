# 获取微博搜索结果原始页面的url
import requests
from urllib.request import urljoin
from fake_useragent import UserAgent
from lxml import etree


class weibo(object):

    def __init__(self):
        self.file = open("PaperUrls","w+",encoding="utf-8")
        self.ua = UserAgent()
        self.urls = self.getURLS()

    def getURLS(self):
        urls = ['https://s.weibo.com/weibo?q=china&wvr=6&b=1&Refer=SWeibo_box&page=%s' % str(i + 1) for i in
                range(15)]
        return urls

    def getpage(self,txt,url):
        html = etree.HTML(txt)
        cards = html.xpath('//div[@class="card-wrap"]')
        for card in cards:
            link  = card.xpath('.//p[@class="from"]/a[1]/@href')
            if len(link) > 0:
                quanwenUrl = urljoin(url,link[0])
                # print(quanwenUrl)
                self.file.write(quanwenUrl+"\n") # 将抓取的全文连接写入文件。


        # return datas

    def download(self,url, ua):
        headers = {'User-Agent': ua.random}
        cookies = dict(SUB='_2A25wmoxBDeRhGeBM71AR9C_OyjyIHXVT0fqJrDV8PUNbmtAKLRjhkW9NRPJ_ZGtjL8Uu6jrtq8wfLoKsmhXGKmU3')
        req = requests.get(url, headers=headers, cookies=cookies).text
        return req

    def run(self):
        for url in self.urls:
            txt = self.download(url, self.ua)
            self.getpage(txt,url)

    def __del__(self):
        self.file.close()

if __name__ == '__main__':
    weibo = weibo()
    weibo.run()



