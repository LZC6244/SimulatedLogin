from scrapy import cmdline

# cmdline.execute内的内容为一个列表
cmdline.execute('scrapy crawl GithupSpider'.split())
