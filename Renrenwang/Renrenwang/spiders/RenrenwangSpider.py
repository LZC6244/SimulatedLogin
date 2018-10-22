# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class RenrenwangspiderSpider(scrapy.Spider):
    name = 'RenrenwangSpider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Referer': 'http://www.renren.com/SysHome.do?origURL=http%3A%2F%2Fwww.renren.com%2F959050106',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    }

    def start_requests(self):
        # 用于保存scrapy格式的cookie的字典
        cookies_content_list = {}

        # 将抓包获取的cookie字符串修改为保存到cookies_content_list字典所需的格式
        cookies_content = 'anonymid=jnk0j5qq-4pgcf; depovince=GW; jebecookies=7f48f58f-abe1-4092-89cb-87c11531c671|||||; _r01_=1; ick_login=e13b4382-093f-40a7-8a5f-581e4d170178; jebe_key=c2fee6cd-40c7-422e-9afe-100b1d1a408c%7C5e520b5d2becfd135fbcb5151632e5b3%7C1540195364903%7C1%7C1540195367320; first_login_flag=1; ln_uact=18377172154; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=null; wp_fold=0; _de=FBF025714A59DC6C03DD14CF1A09F15A; p=0718da03b877b619f05bb021fe8a00316; t=039e9cb02f71371c9a90e36c24dd7dde6; societyguester=039e9cb02f71371c9a90e36c24dd7dde6; id=959050106; xnsid=65335a28; ver=7.0'
        cookies_content = cookies_content.replace(' ', '')
        for i in cookies_content.split(';'):
            # 只分割一次
            key, value = i.split('=', 1)
            cookies_content_list[key] = value
        # yield Request() 或 return [Request()]
        return [Request('登录人人网后的用户主页',
                        headers=self.headers,
                        cookies=cookies_content_list,
                        callback=self.parse)]

    def parse(self, response):
        # 打印当前网页的URL
        # 当前URL应为登录后的URL
        print 'response.url is %s ' % response.url

        try:
            # 用户名
            user_name = response.xpath('//a[@class="hd-name"]/text()').extract()[0]
            print user_name

            # 总RP值
            total_rp = response.xpath('//span[@class="total"]/text()').extract()[0]
            total_rp_num = response.xpath('//span[@class="total"]/b/text()').extract()[0]
            print total_rp + total_rp_num

            # 今日RP值
            today_rp = response.xpath('//a[@class="for_content"]/span[2]/text()').extract()[0]
            today_rp_num = response.xpath('//a[@class="for_content"]/span[2]/b/text()').extract()[0]
            print today_rp + today_rp_num
        except Exception, e:
            print '登录失败！'
