# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs


class GithupPipeline(object):

    def __init__(self):
        # 将爬下来的数据保存到本地TXT文件
        self.file = codecs.open('projecr_info.txt', 'a', 'utf-8')

    def process_item(self, item, spider):
        print 'item is %s' % item
        self.file.write(str(item) + '\n')
        return item
