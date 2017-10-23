# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import os
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

class UrllistPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='192.168.3.232',db='caiji',user='zwj',passwd='123456',charset='utf8')
        cursor = conn.cursor()

        sql='insert into DZDP_URLLIST(fenlei,href) values("%s","%s")'%(item['fenlei'],item['href'])
        cursor.execute(sql)
        conn.commit()
        return item
