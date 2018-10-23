# SimulatedLogin

# 目录
-  Githup
- Renrenwang
- Githup_2
---

### Githup
- 目标网站：https://github.com
- 运行：运行项目里的cmdline.py
- 说明：通过scrapy使用post模拟登录githup，并爬取自己项目列表信息到本地TXT文件
```
step:
    （登录页面这里都是一个form表单提交，我们可以通过火狐浏览器对其进行分析）
    1. 用firefox打开[登录页面](https://github.com/session)
    2. 输入githup帐号密码（密码要输错误的，方便查看提交的表单信息），按F12打开页面调试，点击登录
    3. 点击调试页面的"网络">>"POST">>"参数"可以看见提交的post表单内容
    4. 点击调试页面的"网络">>"消息头">>"请求头"可以看见firefox发送的请求头部信息
    5. 根据3 & 4可以进行模拟登录，开始构造爬虫程序
    6. 打开想要cmd，输入：scrapy startproject Githup（项目名称）
    7. 在cmd下，接着输入：cd Githup（进入项目路径）
    8. 进入路径后，接着输入：scrapy genspider GithupSpider（爬虫名） githup.com（目标网站）
    9. 使用pycharm打开项目进行编辑
```
**step 3**  

![step3](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup/images_demo/1.png)

**step 4**  

![step4](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup/images_demo/2.png)
- items.py  --------- 定义要爬取的数据结构
```
# 项目名称
project_name = scrapy.Field()
```
- settings.py  --------- 要修改的设置
```
# Obey robots.txt rules（不遵守ROBOTS协议）
# ROBOTSTXT_OBEY = True

# Configure item pipelines（启用管道）
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Githup.pipelines.GithupPipeline': 300,
}
```
- GithupSpider.py  --------- 爬虫程序，详见代码
- cmdline.py  --------- 启动爬虫程序的代码
```
from scrapy import cmdline

# cmdline.execute内的内容为一个列表
cmdline.execute('scrapy crawl GithupSpider'.split())
```
#### 效果图
- 证明登录成功 --------- 显示githup个人项目信息  
    
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup/images_demo/3.png)  

- 证明保存TXT文件功 --------- 本地存在TXT文件且内容正确  
    
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup/images_demo/4.png)

---

### Renrenwang

- 目标网站：http://renren.com/
- 运行：运行项目里的cmdline.py
- 说明：通过scrapy使用cookie模拟登录人人网，并爬取用户名和RP值验证是否登录成功

Cookie：可分为内存Cookie和硬盘Cookie，按在客户端中的存储位置分类；Cookie具有有效时间限制，最短的浏览器关闭后就消失，最长可以一直保存到被删除。  

Cookie登录优点：把登录过的信息（用户名、密码以及其他的验证信息）打包一起发给服务器，告知服务器我们是登录验证过的，不需要知道登录url和表单字段以及其他参数，不需要了解登录的过程和细节，一般用于避开验证码等。  

Cookie登录缺点：Cookie会被附加在每个请求中，增加了流量。HTTP请求中的Cookie是明文传递的，存在安全隐患（除非用HTTPS）。大小限制在4K左右，对于复杂的存储需求不够用。  


```
step:
    1. 用firefox打开[登录页面](http://www.renren.com/)
    2. 输入人人网帐号密码，按F12打开页面调试，点击登录
    3. 点击调试页面的"网络">>"消息头">>"请求头"可以看见firefox发送的请求头部信息
    4. 由 3 我们可以获取cookie值进行模拟登录，开始构造爬虫程序
    5. 打开想要cmd，输入：scrapy startproject Renrenwang（项目名称）
    6. 在cmd下，接着输入：cd Renrenwang（进入项目路径）
    7. 进入路径后，接着输入：scrapy genspider RenrenwangSpider（爬虫名） renren.com（目标网站）
    8. 使用pycharm打开项目进行编辑
```

**step 3**  

![step3](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Renrenwang/images_demo/3.png)  

- RenrenwangSpider.py  --------- 爬虫程序，详见代码
- cmdline.py  --------- 启动爬虫程序的代码
```
from scrapy import cmdline

cmdline.execute('scrapy crawl RenrenwangSpider'.split())
```

#### 效果图
- 打印出来的爬取下来的信息
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Renrenwang/images_demo/1.png)  
- 网页登录后显示的用户名、RP值信息
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Renrenwang/images_demo/2.png)  

---

### Githup_2
- 目标网站：https://github.com
- 运行：运行项目里的cmdline.py
- 说明：通过scrapy使用cookie模拟登录githup  

```
step:
    1. 用firefox打开[登录页面](https://github.com/session)
    2. 输入Githup帐号密码，按F12打开页面调试，点击登录（已登录的情况下可以F12之后刷新页面）
    3. 点击调试页面的"网络">>"消息头">>"请求头"可以看见firefox发送的请求头部信息
    4. 由 3 我们可以获取cookie值进行模拟登录，开始构造爬虫程序
    5. 打开想要cmd，输入：scrapy startproject Githup_2（项目名称）
    6. 在cmd下，接着输入：cd Githup_2（进入项目路径）
    7. 进入路径后，接着输入：scrapy genspider Githup_2_spider（爬虫名） github.com（目标网站）
    8. 使用pycharm打开项目进行编辑
```

**step 3**  

![step3](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup_2/images_demo/4.png)  

- Githup_2_spider.py  --------- 爬虫程序，详见代码
- cmdline.py  --------- 启动爬虫程序的代码  

```
from scrapy import cmdline

# cmdline.execute内的内容为一个列表
cmdline.execute('scrapy crawl Githup_2_spider'.split())
```
#### 效果图  
- 登录前信息
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup_2/images_demo/1.png)  
- 登录后信息
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup_2/images_demo/2.png)  
- pycharm爬取下来的信息
![效果图](https://raw.githubusercontent.com/LZC6244/SimulatedLogin/master/Githup_2/images_demo/3.png)  
