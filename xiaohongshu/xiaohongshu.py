# 解析小红书返回的json数据，文章

import os
import jsonpath
import json
import logging
# 解析一个文档的json
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

def parsejson(filename):
    with open("./sessions/" + filename, "r", encoding="utf-8") as ftemp:
        jsonobj = json.loads(ftemp.read())
        desc = jsonpath.jsonpath(jsonobj, '$..desc')
        if not desc:
            strlog = filename+"解析出错"
            logging.error(strlog)
            return None
        elif len(desc) > 0:
            strlog = filename + ",解析ok"
            logging.info(strlog)
            return desc[0]
        else:
            strlog = filename+"数据为空"
            logging.error(strlog)
            return None

if __name__ == '__main__':
    filenames = os.listdir("./sessions")
    # print(len(filenames))
    with open("resultdata_weibo","w",encoding="utf-8") as f:
        for filename in filenames:
            desc = parsejson(filename)
            if desc is not None:
                f.write(desc+"\r\n")


