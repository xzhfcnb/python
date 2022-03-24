import requests
from lxml import etree
import csv
class baiduSpider:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.baseurl="http://www.baidu.com"

    def readPage(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        html = response.text
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml = etree.HTML(html)
        r_list = parsehtml.xpath('//a[@ class="mnav c-font-normal c-color-t"]/text()')
        self.write(r_list)
        print(r_list)

    def write(self,r_list):
        with open("baidu.csv","w",newline="",encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(r_list)




    def workOn(self):
        url=self.baseurl
        self.readPage(url)



if __name__ == "__main__":
    baidu=baiduSpider()
    baidu.workOn()