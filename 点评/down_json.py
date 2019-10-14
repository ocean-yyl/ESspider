# 根据网页上的店铺url，访问小程序接口，获取店铺的评论
import requests
import re
from fake_useragent import UserAgent

# 大众点评小程序api  https://m.dianping.com/ugc/review/shop/shopreview?pageSize=10000000&shopuuid=2131231
def formate_to_api_urls(start_urls):
    api_urls = []
    for url in start_urls:
        shopuuid = re.findall("/(\d+).*",url)[0]
        api_urls.append('https://m.dianping.com/ugc/review/shop/shopreview?pageSize=10000000&shopuuid='+shopuuid)
    return api_urls

def get_andsave_url(ua,url):
    shopuuid = re.findall("shopuuid=(\d+)", url)[0]
    # print(shopuuid)
    headers = {'User-Agent': ua.random}
    with open("json/"+shopuuid,"wb") as f:
        f.write(requests.get(url, headers=headers).content)

if __name__ == '__main__':
    #网页上的店铺的url
    start_urls = [
       "url"
       ]
    apiurls = formate_to_api_urls(start_urls)
    ua = UserAgent()
    for url in apiurls:
        get_andsave_url(ua,url)
