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
        cookies_content = 'anonymid=jnk6wmm5-vhn4nh; depovince=GW; jebecookies=c08eab0d-e5fa-41c9-bd18-8b5d49420a18|||||; _r01_=1; JSESSIONID=abc2466G_CdBF75_VBBAw; ick_login=f4d7118b-c7b1-4853-979c-81896ddf35d9; jebe_key=61b06720-bd7d-4ec1-8776-537d2b53d26e%7Ccfcd208495d565ef66e7dff9f98764da%7C1540206035949%7C0%7C1540206037921; _de=FBF025714A59DC6C03DD14CF1A09F15A; p=6e605b7dcd0c31d920dd3e51386780e76; first_login_flag=1; ln_uact=18377172154; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1bf20810e341dad6dd105a2d5174a6fe6; societyguester=1bf20810e341dad6dd105a2d5174a6fe6; id=959050106; xnsid=6490e3be; loginfrom=syshome'
        cookies_content = cookies_content.replace(' ', '')
        for i in cookies_content.split(';'):
            # 只分割一次
            key, value = i.split('=', 1)
            cookies_content_list[key] = value
        # yield Request() 或 return [Request()]
        return [Request('http://www.renren.com/959050106',
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
