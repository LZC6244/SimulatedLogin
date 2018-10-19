# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
from Githup.items import GithupItem


class GithupspiderSpider(scrapy.Spider):
    name = 'GithupSpider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com']

    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Referer': 'https://github.com/login?return_to=%2Fjoin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    }

    # 重写start_requests方法
    def start_requests(self):
        # 进入登录界面
        # return后需跟一个列表，否则会报TypeError: 'Request' object is not iterable
        return [Request('https://github.com/session',
                        callback=self.githup_login,
                        meta={'cookiejar': 1})]
        # meta：字典格式的元数据,主要用来在解析函数之间传递值
        # 通过meta传入cookiejar特殊key，爬取url作为参数传给回调函数
        # cookiejar：meta的一个特殊key，通过cookiejar参数可以支持多个会话对某网站进行爬取
        # 对cookie做标记1, 2, 3...scrapy即可维持多会话

    def githup_login(self, response):
        # 使用xpath获取authenticity_token值
        authenticity_token = response.xpath('//form[@action="/session"]/input[2]/@value').extract()[0]
        return FormRequest.from_response(
            response,
            # url='https://github.com/session',
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            # 表单数据
            formdata={
                'authenticity_token': authenticity_token,
                'commit': 'Sign+in',
                # 你自己的帐户
                'login': 'xxxxxx',
                # 你自己的密码
                'password': 'xxxxxx',
                'utf8': '✓'
            },
            callback=self.githup_after_login,
            # dont_click为True，表单数据将被提交，而不需要单击任何元素
            dont_click=True
        )

    def githup_after_login(self, response):
        page_content = response.xpath('//div[@class="news column two-thirds"]/div[2]/h3/text()').extract()[0]
        # 判断'Browse activity'是否在页面中，在则说明登录成功
        if 'Browse activity' in page_content:
            print 'login success.'
            item = GithupItem()
            for i in response.xpath('//ul[@class="list-style-none"]//a/@href').extract():
                item['project_name'] = i
                # print 'item is %s--------------2\n' % item
                yield item
            # 示例调用parse方法（可屏蔽）
            yield Request(url=response.url, callback=self.parse)
        else:
            print 'login fail.'

    def parse(self, response):
        # 示例调用parse方法（可屏蔽）
        print 'hello.'
