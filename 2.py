import requests
from lxml import etree
import csv
class baiduSpider:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.baseurl="http://www.qnzy.net/public/consultletter/letterlist?searchType=4&consultId=7"

    def readPage(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        html = response.text
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml = etree.HTML(html)
        r_list = parsehtml.xpath('//a[@ class="mnav c-font-normal c-color-t"]/text()')
        r_list1 = parsehtml.xpath('//a[@ class="mnav c-font-normal c-color-t"]/@href')
        # print(r_list)
        # print(r_list1)
        list=[]
        for i in range(len(r_list1)):
            new_list=[r_list[i],r_list1[i]]
            list.append(new_list)
        print (list)
        self.write(list)


    def write(self,list):
        with open ("baidu3.csv","a",newline="",encoding="gb18030") as f:
                write = csv.writer(f)
                write.writerow(["±ÍÃ‚","¡¥Ω”"])
        for r in list:
            with open("baidu3.csv","a",newline="",encoding="gb18030") as f:
                write = csv.writer(f)
                write.writerow(r)
        # print(r)

    def workOn(self):
        url=self.baseurl
        self.readPage(url)

if __name__ == "__main__":
    baidu=baiduSpider()
    baidu.workOn()