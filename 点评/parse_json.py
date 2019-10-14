#解析返回的json数据
import jsonpath
import json
import os

def parsefile(filename):
    with open("json/" + filename, encoding="utf-8") as f:
        jsonstr = f.read()

    jsonobj = json.loads(jsonstr)
    len = jsonpath.jsonpath(jsonobj, '$..reviewTotalCount')
    size = int(len[0])
    with open("datas/" + filename, "wb") as f2:
        for i in range(size):  # len
            res = jsonpath.jsonpath(jsonobj, '$..reviewList.' + str(i) + ".reviewBody.children..text")
            # print("".join(res))
            f2.write("".join(res).encode("utf-8"))
            f2.write("\n".encode("utf-8"))

if __name__ == '__main__':
    filenames = os.listdir("./json")
    for filename in filenames:
        parsefile(filename)
        print(filename,"has finished。。。")


