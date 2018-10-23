# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class Githup2SpiderSpider(scrapy.Spider):
    name = 'Githup_2_spider'
    allowed_domains = ['githup.com']
    start_urls = ['http://githup.com/']

    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Referer': '请求报头的referer值',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    }

    def start_requests(self):
        # 用于保存scrapy格式的cookie的字典
        cookies_content_dict = {}
        # cookies字符串
        cookies_str = '通过firefox抓包获取到的cookies'
        # 将cookies字符串保存为scrapy格式的字典
        for i in cookies_str.split('; '):
            key, value = i.split('=', 1)
            cookies_content_dict[key] = value
        # return [Request()] or yield Request()
        return [Request('登录知乎后的用户主页URL',
                        headers=self.headers,
                        cookies=cookies_content_dict,
                        callback=self.parse)]

    def parse(self, response):
        # 打印当前网页的URL
        print 'response.url is %s.' % response.url

        # xpath获取到则表明登录失败，不带下标[0]是因为获取不到时会报越界错误
        sign_up_info = response.xpath('//h3[@class="pt-2"]/text()').extract()
        # xpath获取到则表明登录成功，不带下标[0]是因为获取不到时会报越界错误
        sign_in_info = response.xpath(
            '//summary[@class="btn-link muted-link float-right mt-1 pinned-repos-setting-link"]/text()').extract()
        if sign_up_info:
            print '-------------登录失败-------------'
            print 'sign_up_info is %s' % sign_up_info
        if sign_in_info:
            print '-------------登录成功-------------'
            print 'sign_in_info is %s' % sign_in_info
