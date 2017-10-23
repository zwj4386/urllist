#!/usr/bin/python
# coding: utf-8
import scrapy
from scrapy.http.request import Request
from scrapy import Selector
from URLLIST.items import UrllistItem
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

class spider_urllist(scrapy.Spider):
    name = 'urllist'
    start_urls=['http://www.dianping.com']
    allowed_domain=['www.dianping.com']

    def parse(self, response):
        url = [#'美食$http://www.dianping.com/search/category/110/10/g0r0',
               #'酒吧$http://www.dianping.com/search/category/110/30',
               #'周边游$http://www.dianping.com/search/category/110/35',
               #'运动健身$http://www.dianping.com/search/category/110/45/g0r0',
               #'医疗健康$http://www.dianping.com/search/category/110/85/g0r0',
               #'爱车$http://www.dianping.com/search/category/110/65/g0r0',
               '剧院$http://www.dianping.com/search/category/110/25'
               ]
        for i in range(0,len(url)):
            list = url[i].split('$')
            fenlei = list[0]
            dlurl = list[1]
            yield Request(dlurl, meta={'fenlei':fenlei} , callback= self.getUrl)

    def getUrl(self,response):
        xp = Selector(response)
        fenlei = response.meta['fenlei']
        div = xp.xpath('//div[@id="classfy"]/a')
        for i in range(0,len(div)):
            item = UrllistItem()
            item['fenlei'] = fenlei.encode('utf-8')
            href = xp.xpath('//div[@id="classfy"]/a/@href')[i].extract()
            item['href'] = href
            yield item


