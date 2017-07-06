import re
import urllib.request
import os
from bs4 import BeautifulSoup

class ImageSpider(object):
    def __init__(self,url):
        self.url = url
        self.num = 0

    def getImage(self):
        respone = urllib.request.urlopen(self.page_url)
        # print(respone.getcode())
        #获取网页文本
        text = respone.read()
        text = str(text, 'utf-8')
        #解析网页
        soup = BeautifulSoup(text, 'html.parser')
        images = soup.find_all('img', class_='height_min')
        return images

    def saveImage(self):
        if not os.path.exists(r'F:\test\image'):
            os.mkdir(r'F:\test\image')

        images = self.getImage()
        for image in images:
            # print(image['title'])
            # print(image['src'])
            image_url = image['src']
            image_name = image['title']
            image_name = image_name[0:-1]
            urllib.request.urlretrieve(image_url, r'F:\test\image\%d_%s.jpg' % (self.num, image_name))
            print('%d_%s正在保存' % (self.num, image_name))
            self.num += 1

    def getPageImage(self):

        startPage = int(input("请输入开始页："))
        stopPage = int(input("请输入尾页："))
        while startPage <= stopPage:
            self.page_url = self.url +str(startPage)
            startPage += 1
            self.saveImage()


ImageSpider = ImageSpider('http://www.dbmeinv.com/dbgroup/show.htm?cid=7&pager_offset=')
ImageSpider.getPageImage()


