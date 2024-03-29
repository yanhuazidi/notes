[TOC]




## 爬虫分类

### 通用网络爬虫

搜索引擎用,遵守robots协议
https//www.taobao.com/robots.txt 查看协议内容

搜索引擎如何获取 1 个新网站的 URL
1. 网站主动向搜索引擎提供(百度站长平台)
2. 和 DNS服务商(万网)合作，快速收录新网站

### 聚焦网络爬虫
自己写的爬虫程序 : 面向需求的爬虫



## Anaconda 和 Spyder

### Anaconda :

科学计算的集成开发环境(Python,iPython,大量的库)

### Spyder 
常用快捷键

    1. 注释/取消注释 : Ctrl +1
    2. 保存 :   Ctrl + s
    3. 运行程序  :      F5
   4. TAB 自动补全



## Chrome 浏览器插件

**安装插件步骤**

1. 浏览器右上角 - 更多工具 - 扩展程序
2. 点开右上角 - 打开开发者模式
3. 把插件拖拽到浏览器页面，释放鼠标点击添加扩展



## User-Agent
记录了用户的浏览器、操作系统等

- Mozilla Firefox : (Gecko)
- IE : Trident
- Apple : Webkie(like KHTML)
- Google : Chrome(like Webkit)
- 其他浏览器都是模仿 IE/Chrome



## urllib标准库(Python3)

### 请求模块

`from urllib import request`

1. `urllib.request.urlopen(URL[,data][,timeout])`

   作用: 向网站发起1个请求，并获取响应

   ```python
   with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
       data = f.read()
       print('Status:', f.status, f.reason)
       for k, v in f.getheaders():
           print('%s: %s' % (k, v))
       print('Data:', data.decode('utf-8'))
   ```

2. `urllib.request.Request(url[, data=None][, headers={}][, origin_req_host=None][, unverifiable=False][, method=None])`

   参数:

   - `url`

     ```python
     str  'https://api.douban.com/v2/book/2129650'
     ```

   - `data`(post请求)

     data = `urlencode(dict).encode('utf-8')`
     先编码得到字符串，再转码得到bytes数据类型

   - `headers`

     ```python
     {'User-Agent':'....'}`
     ```

   返回值

   ​	请求对象

   

   模拟浏览器发送GET请求，就需要使用`Request`对象，通过往`Request`对象添加HTTP头，我们就可以把请求伪装成浏览器

   ```python
   from urllib import request
   req = request.Request('http://www.douban.com/')
   req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
   with request.urlopen(req) as f:
       print('Status:', f.status, f.reason)
       for k, v in f.getheaders():
           print('%s: %s' % (k, v))
       print('Data:', f.read().decode('utf-8'))
   ```



**响应对象(response)**

`<class 'http.client.HTTPResponse'>`

1. `response.read()`读取服务器响应的内容

   字节流 = `response.read()`

   字符串 = `response.read().decode('utf-8')`

2. `response.geturl()`   返回实际数据的 URL 地址

3. `response.getheaders()`   返回响应头

   ```python
   [('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'SAMEORIGIN'), ('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Content-Length', '47397'), ('Accept-Ranges', 'bytes'), ('Date', 'Mon, 01 Aug 2016 09:57:31 GMT'), ('Via', '1.1 varnish'), ('Age', '2473'), ('Connection', 'close'), ('X-Served-By', 'cache-lcy1125-LCY'), ('X-Cache', 'HIT'), ('X-Cache-Hits', '23'), ('Vary', 'Cookie'), ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]
   ```

4. `response.getheader(name)`  获指定取响应头信息

5. `response.status`   响应状态码

6. `response.reason`   响应状态码描述

7. `readinto()`

8. `fileno()` 

9. `msg`

10. `version`

11. `debuglevel`

12. `closed`



### URL 编码模块

`from urllib.parse import quote,unquote,urlencode`

#### 非 ascii 字符 url处理

编码

`quote(字符串)`

```python
text = "丽江"
str = quote(text,'utf-8')
print(str)  # "%E6%8C%96%E6%8E%98"
```

解码

`unquote(已编码字符串)`


```python
str = "%E6%8C%96%E6%8E%98"
print(unquote(str,'utf-8'))  # "丽江"
```

#### url 编码

`urlencode(dict)` : 多个键值对会在中间自动加 & 

```python
str= urllib.parse.urlencode({'wd':"美女"})
print(str)
#"wd=%E6%8C%96%E6%8E%98"
```



## 数据的分类
结构化的数据

​        特点: 有固定的格式，如 : HTML XML JSON

非结构化数据

​		如: 图片，音频，视频 这类数据一般存储为二进制



## csv 模块(Excal表格文件)
`import csv`

1. 打开csv文件
   `with open('测试.csv'，'w',newline='') as f:`

   2. 初始化写入对象

       `writer = csv.writer(f)`

    3. 写入数据

       `writer.writerow(列表)`



Anaconda 安装模块

​    

    1. 右键以管理员的身份进入 Anaconda Prompt终端
    2. 执行安装命令
        conda install pymongo
        conda install pymysql


远程存入 mySQL 数据库
    Linux shell
    1. 开启远程连接
        /etc/mysql/mysql.conf.d/mysqld.cnf
        注释掉 bind-address=127.0.0.1
        重启服务

    2. 添加授权用户
        mysql> grant all privileges on *.* to "用户名"@"%" identified by '123456' with grant option;
    
    3. 防火墙
        sudo ufw status 查看状态
    
        sudo ufw disable 关闭防火墙
    
        或添加规则允许外部访问 3306端口
            sudo ufw allow 3306
    程序中
        self.mydb = pymysql.connect(host='176.23.5.140',user='weitianhua',password='123456',database='spider',charset='utf8',port=3306)
        self.cursor = self.mydb.cursor()
        sql = 'insert into mao values(%s,%s)'
        for name,score in rList:
             self.cursor.execute(sql,[name,score])  #只能一条一条插入
             self.mydb.commit()
        self.cursor.close()
        self.mydb.close()


​        
远程存入 mongo 数据库
​    
​    防火墙
​        sudo ufw status 查看状态
​        sudo ufw disable 关闭防火墙
​        或添加规则允许外部访问端口
​            sudo ufw allow 27017
​    
     程序中  
        self.conn = pymongo.MongoClient("176.23.5.140",27017)
        self.db = self.conn["MaoDB"]
        # 集合对象
        self.myset = self.db["film"]
        for rDict in rList:
            name = rDict["title"]
            score = rDict["score"]
            print(name,score)
            d = {
                "name" : name.strip(), 
                "fen" : score.strip()
              }
            self.myset.insert_one(d)    #只能一条一条插入


Ubuntu中防火墙(ufw)基本操作
    sudo ufw status 查看状态
    1. 打开 :   sudo ufw enable
    2. 关闭防火墙 :  sudo ufw disable
    3. 添加规则 : sudo ufw allow 端口



**********************************************************************************************

Cookie 模拟登录
    1. 什么是 cookie  session
        HTTP协议是一种无连接的协议
        客户端和服务器交互仅仅局限于请求/响应之间，下一次再请求时，服务器会认为是一个新的客户，为了维护他们
        之间的连接，让服务器知道是上一个用户发起的请求，必须在一个地方保存客户端信息
        
        cookie : 客户端信息确定用户身份
        session : 服务端信息确定用户身份


​        
​    2. 使用 cookie 模拟登录人人网
​        1. 先登录成功1次，获取到 cookie
​        2. 拿着 带有cookie 的headers(去掉压缩键值对) 去抓取需要登录才能看到的页面


​        
​        

requests 模块
    1. 安装 :以管理员身份去打开 Anaconda Prompt conda install requests
    
    2. 常用方法
        1. get(url,headers=headers)
    
            res = requests.get(url,headers=headers)
        
        2. 响应对象的 res 属性
            1. encoding ： 响应编码
                res.encoding = 'utf-8' 转换响应对象编码
                print(res.encoding)
                
            2. text : 响应对象的字符串文本
                print(res.text)
                
            3. content ：响应对象的bytes文本(用于非格式化文本,图片，MP3，视频...)
                print(res.content)
                
            4. status_code : HTTP响应码
                print(res.status_code)
                
            5. url   ： 返回实际数据的 URL地址
                print(res.url)


​    
​        
get() 方法参数
​    1. 查询参数  params
​        params={}
​        自动对params字典进行编码，自动拼接URL地址，输入搜索内容，再输入第几页
​        params = {
​        'wd':key,
​        'pn':pn,
​            }
​    
​        res = requests.get(url,params=params,headers=headers)


​        
​    2. 使用代理IP  proxies
​        1. 获取 IP 地址的网站
​            快代理
​            全网代理
​            。。。
​            
        2. 普通代理
            1. 格式 :  proxies = {"协议":"协议://IP:端口"}
            
        http://httpbin.org/get 向这个网站发请求会返回 IP和请求头信息
        {
            args: { },
            headers: {
                Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                Accept-Encoding: "gzip, deflate",
                Accept-Language: "zh-CN,zh;q=0.9",
                Connection: "close",
                Host: "httpbin.org",
                Upgrade-Insecure-Requests: "1",
                User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            },
            origin: "122.224.206.179",
            url: "http://httpbin.org/get"
        }


​    
​    
​        3. 私密代理
​            1. 格式 
​                proxies = {
​                    'http':"协议://用户名:密码@IP:端口"
​                }
​    
    3. timeout=5  设置超时,5s之后没响应报错
    
    4. Web客户端验证  auth
        1. auth = ('用户名','密码')


​        
​    5. SSL证书认证  verify
​    
        1. verify = True(默认认证): 进行CA证书认证
        2. verify = Flase  : 不进行认证
        
        ## 参数为True进行认证，去访问HTTPS 网站(没有进行CA认证)，抛出异常: SSLError 
            只需改为 Flase



post()方法
    1. requests.post(url,data=data,.....)
    2. data : 字典，Form表单数据，不用编码，不用转码
    
        


xpath 工具(解析)
    1. 在 XML 文档中查找信息的语言，同样适用于 HTML文档的检索
    
    2. xpath 辅助工具
    
        1. Chrome插件 : XPath Helper
            在浏览器中安装插件后 按Ctrl+Shift+x 鼠标单击浏览器页面空白处
        2. Firefox插件 : XPath Checker
        
        3. XPath编辑工具 : XML quire
    
    3. 演示
        // 表示查找所有后代节点，获取节点对象
        / 表示查找所有子节点，获取节点对象
        
        1. 查找所有的 book 节点对象 : // book
        2. 查找所有 book 节点下的 title节点中,lang属性为'en'的节点对象
            //book/title[@lang='en']
            
        3. 查找 bookstore 下的第2个book节点下的title子节点对象
            /bookstore/book[2]/title
        
        4. 选取节点
            // : 从整个文档中查找节点对象
                //price  //book//price
                
            @ : 选取某个属性值的节点对象
                //title[@lang='en']
                
        5. @的使用
            1. 选取1类节点对象 :    //title[@lang='en']
            2. 选取存在某个属性的节点对象 : //title[@lang]
            3. 选取节点的属性值 : //title/@lang
                常用 @src  @href
                
        6. 匹配多路径
            1. xpath表达式1 | xpath表达式2
            匹配所有book节点下的 title 和 price 节点对象
            
            //book//title | //book//price
            
        7. 函数
            1. contains(): 匹配一个属性值中包含某些字符串的节点对象
            
                //title[contains(@lang,'e')]
                
            2. text() : 获取节点文本值
                //title[contains(@lang,'e')]/text()
            
            或者从获取的节点对象中 for 循环 取一个对象
            用 .text属性取值


lxml 库 及xpath使用
    
    安装:
        管理员 Prompt :  conda install lxml
        
    2. 使用流程
        1. 导入模块
             from lxml import etree
             
        2. 创建解析对象
            paresHtml = etree.HTML(html)
        
        3. 调用 xpath
            rList = paresHtml.xpath('xpath表达式')
            ## 只要调用了xpath，结果一定是列表


​        
​    
1. Fiddler抓包工具设置
  1. 设置Fiddler软件
    1. https: Tools - options - HTTPS - ...from browsers only 
       Actions 添加证书信任
    2. connections: 设置端口号 8888
    3. 重启Fiddler软件
  2. 设置Chrome浏览器     
    1. 安装代理切换插件:Proxy SwitchOmega
    2. 选项 - 新建情景模式 - HTTP 127.0.0.1 8888 - 应用情景模式
    3. 把代理切换到自己新建的情景模式上
2. Fiddler常用菜单
  1. Inspector : 查看数据包详细内容
    1. 分为 请求(request) 和 响应(response) 两部分
  2. 常用子选项卡
    1. Headers : 显示请求头信息
    2. WebForms: 显示POST数据,在body中
    3. Raw     : 将整个请求显示为纯文本
3. 抓取百度贴吧帖子中所有图片
  1. 目标 : 指定贴吧所有帖子的图片
  2. 思路
    1. 获取贴吧主页URL,下一页,找URL规律
    2. 获取1页中每个贴的URL
    3. 对每个帖子URL发请求,获取帖子中图片URL
    4. 依次对图片URL发请求,以wb方式保存到本地
  3. 思路梳理
    帖子链接列表 = parseHtml.xpath('....')
    for 1个帖子链接 in 帖子链接列表:
        html = 对每个帖子发请求得到响应
        图片链接列表 = parseHtml.xpath('..')
        for 1个图片链接 in 图片链接列表:
            html = 对每个图片发请求得到响应
            with open("aaa.jpg","wb") as f:
                f.write(html)
  4. 步骤
    1. 获取贴吧主页URL
      http://tieba.baidu.com/f? + 查询参数
    2. 提取页面中所有帖子的URL
      href : /p/5991484415
        域名 + href 为帖子链接
        http://tieba.baidu.com/p/5991484415
      xpath表达式 ：//div[@class="t_con cleafix"]/div/div/div/a/@href
    3. 每个帖子中图片的URL
      //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src





4. 抓取百度贴吧帖子中所有视频以及图片
  1. 视频小path匹配
    //div[@class="video_src_wrapper"]/embed/@data-video
  2. 注意 
    在浏览器中匹配的不一定是真实的,此时
    1. 更换User-Agent为IE
    2. 把页面下载到本地,去查找位置
5. 糗事百科(xpath高级用法)
  1. 目标 : 用户昵称 内容 好笑数 评论数
  2. 步骤
    1. URL 
      https://www.qiushibaike.com/text/
    2. xpath表达式
      1. 匹配出所有段子的对象
        //div[contains(@id,"qiushi_tag_")]
        结果:[<element...>,<element...>,..]
      2. 利用节点对象调用xpath
        for base in baseList:
          用户昵称 : ./div/a/h2
          段子内容 : 
            ./a/div[@class="content"]/span
          好笑数量 : .//i[@class="number"]
                   [好笑数量对象,评论对象]
          评论数量 : .//i[@class="number"]
6. json模块
  1. json格式的字符串和Python数据类型之间转换
  2. json.loads(html) : json -> Python 
  3. json.dumps(python)
7. 动态网站数据抓取(Ajax)
  1. 特点 : 滚动鼠标滑轮时加载
  2. 案例 : 豆瓣电影排行榜数据抓取
    1. 抓取目标 : 豆瓣电影 - 排行榜 - 剧情
                 电影名称 评分
    
  
1. 豆瓣电影


2. selenium + phantomjs/chrome 强大网络爬虫组合
	1. selenium
		1. Web自动化测试工具，应用于Web自动化测试
		2. 特点
			1. 可以运行在浏览器，根据指定命令操作浏览器，让浏览器自动加载页面
			2. 只是工具，需要与第三方浏览器结合使用
		
		3.安装
			管理员 Anaconda Prompt
				conda install selenium
	
	2. phantomjs 
		1. 无界面浏览器(无头浏览器)
		2. 特点
			1. 把网站加载到内存进行页面的加载
			2.运行高效
		3. 安装
			Windows安装
				把下载的 exe文件，拷贝到 python 安装目录的 Scripts目录下
				在终端 'where python'   查找python位置
		4. Ubuntu安装
			1. 下载安装包并解压 : phantomjs-2.1.1-.
			2. cd 到解压的路径的 bin 目录下
			3. 把文件拷贝到  /usr/bin/  目录下
		
	3. chromedriver
		1. 安装
			1. 查看浏览器版本 
				浏览器 - 设置 - 帮助 - 关于Google chrome
					chrome浏览器版本  71.0.3578.98	
				
			2. 下载对应的chromedriver.exe版本
				https://chromedriver.storage.googleapis.com/index.html
			3. 拷贝 chromedriver.exe 到 Scripts目录下
			4. chromedriver -v

3. 打开百度页面截图
	from selenium import webdriver

	#获取浏览器对象
	#driver = webdriver.PhantomJS() #phantomjs
	driver = webdriver.Chrome()  #chrome浏览器

	driver.get('http://www.baidu.com/')
	driver.find_element_by_id('kw').send_keys('美女')

	driver.find_element_by_id('su').click()

	#获取 html
	html = driver.page_source
	with open('baidu.html','w',encoding='utf-8') as f:
		f.write(html)

	#保留页面截图
	driver.save_screenshot('baidu.png')
	#关闭浏览器
	driver.quit()			
	
4. 浏览器对象(driver)的方法
	1. driver.get(url) : 发请求，获相应
	
	2. driver.page_source : 获取html源码
	
	3. driver.page_source.find('查询字符串')
		查找失败返回 ：-1
		成功返回：字符下标
		
	4. 单元素查找,只返回第一个节点对象
		1. element=driver.find_element_by_id('')
		2. driver.find_element_by_name('')
		3. driver.find_element_by_class_name('')
		4. driver.find_element_by_class_xpath('xpath表达式')
		
		获取节点对象文本
			element.text
		
		给节点对象输入值
			element.send_keys('')
			
		点击节点对象
			element.click()
		
	
	5.多元素查找,返回节点对象列表
		1. elementList = driver.find_elements_by_id('')
		2. driver.find_elements_by_name('')
		3. driver.find_elements_by_class_name('')
		4. driver.find_elements_by_class_xpath('xpath表达式')
		
	
	人人网登陆，验证码输入
		#获取浏览器对象
		#driver = webdriver.PhantomJS() #phantomjs
		#设置chrome无界面
		opt = webdriver.ChromeOptions()
		opt.set_headless()	消除Chrome界面
		
	opt.add_argument("windows-size=1920x3000")  指定窗口大小
		
	driver = webdriver.Chrome(options=opt)  #chrome浏览器
		
	driver.get('http://www.renren.com/')
		
	driver.maximize_window()  以最大窗口打开
		
		uname = driver.find_element_by_name('email')
		uname.send_keys('18633615542')
		pwd = driver.find_element_by_name('password')
	pwd.send_keys('zhanshen001')
		
		time.sleep(1)
		保留页面截图
		if driver.find_element_by_name('icode'): #有问题
			driver.save_screenshot('test/yzm.png')
			yzm = input('请输入验证码: ')
  		driver.find_element_by_name('icode').send_keys(yzm)
	
	driver.find_element_by_id('login').click()
		
		time.sleep(1)
		driver.save_screenshot('test/yes.png')
		#关闭浏览器
		time.sleep(10)
		driver.quit()
	
	6. driver 如何执行js脚本
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	
5. 斗鱼爬取
		import time

		from selenium import webdriver
		#opt = webdriver.ChromeOptions()
		#opt.set_headless()
		#driver = webdriver.Chrome(options=opt)  #chrome浏览器
		driver = webdriver.PhantomJS()
	
		driver.get('https://www.douyu.com/directory/all')
		time.sleep(2)
		while True:
			text = driver.find_element_by_class_name('jumppage')
			key= input('爬取第几页(1~200):')
			if not 0<int(key)<201:
				print('页码不对')
				q = input('退出爬取(y/n):')
				if q=='y':
					break
				continue
			text.send_keys(int(key))
	
			button = driver.find_element_by_class_name('shark-pager-submit')
			button.click()
			time.sleep(2)
	
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			time.sleep(3)
			xpath = "//div[@class='mes']"
			rList = driver.find_elements_by_xpath(xpath)
			for r in rList:
				contentList = r.text.split('\n')
				if len(contentList)==4:
					d = {
						"标题":contentList[0],
						"类型":contentList[1],
						"主播":contentList[2],
						"人气":contentList[3],
						}
					with open('test/douyu.json','a',encoding='utf-8') as f:
						f.write(str(d)+'\n')
		#关闭浏览器
		driver.quit()


​	
多线程爬虫
​	1. 进程
​		1. 系统中正在运行的一个程序
​		2. 1个CPU核心1次只能执行1个进程，其他进程处于非运行状态
​		3. N个CPU核心可同时执行N个任务
​	2. 线程
​		1. 进程中包含的执行单元，1个进程中可以有多个线程
​		2. 线程使用所属进程空间/资源
​		3. 互斥锁， 防止多个线程同时使用共享资源
​		
​	3. GIL ： 全局解释锁
​		执行通行证，仅此1个，拿到通行证就执行
​		
	4. 应用场景
		1. 多进程 : 大量的密集的计算
		2. 多线程 : I/O密集
			1. 爬虫 : 网络I/O
			2. 写文件 : 本地磁盘I/O

1. 多线程爬虫
	1. 队列(from multiprocessing import Queue)
		UrlQueue = Queue()
		UrlQueue.put(url)
		UrlQueue.get() #为空时默认阻塞,block=True(阻塞),timeout=2(超时报错)
		UrlQueue.empty() 判空
		
	2. 线程(from threading import Thread)
		t = Thread(target=getPage)
		t.start()
		t.join()
		

小米应用商城
		headers = random.choice(hLis)
		class XiaomiSpider:
			def __init__(self):
				self.baseurl = 'http://app.mi.com/category/12#page='
				self.mainUrl = 'http://app.mi.com'
				self.headers = headers
				self.urlQueue = Queue()
				self.parseQueue = Queue()
        
			def getUrl(self):
				for page in range(20):
					url = self.baseurl + str(page)
					self.urlQueue.put(url)
	
			def getHtml(self):
				while True:
					if not self.urlQueue.empty():
						url = self.urlQueue.get()
						res = requests.get(url,headers=self.headers)
						res.encoding='utf-8'
						html = res.text
						self.parseQueue.put(html)
					else:
						break
	
			def getDate(self):
				while True:
					try:
						html = self.parseQueue.get(block=True,timeout=0.5)
					except:
						break
					else:
						parseHtml = etree.HTML(html)
						baseList = parseHtml.xpath("//ul[@id='all-applist']//li//h5")
						for base in baseList:
							name = base.xpath("./a/text()")[0]
							link = self.mainUrl+base.xpath("./a/@href")[0]
							d = {
									'应用名称':name,
									'链接地址':link
									}
							with open('test/xiaomi.json','a',encoding='utf-8') as f:
								f.write(str(d)+'\n')
	        
	def workOn(self):
	    self.getUrl()
	    tList = []
	    for i in range(5):
	        t1 = Thread(target=self.getHtml)
	        t2 = Thread(target=self.getDate)
	        tList.append(t1)
	        tList.append(t2)
	        t1.start()
	        t2.start()
	    for i in tList:
	        i.join()


if __name__=='__main__':
    start = time.time() 
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print('运行时间为: ',str(end-start))
		

3. BeautifulSoup(解析)
		详解 :  http://www.cnblogs.com/hanmk/p/8724162.html
	
	1. HTML或者XML解析器，依赖于lxml
	2. 安装 : conda install beautifulsoup4
	3. 使用流程
		1. 导入模块
			from bs4 import BeautifulSoup
		
		2. 创建解析对象
			soup = BeautifulSoup(html,'lxml')
			
		3. 查找节点对象
			rList = soup.find_all('div',{'id':''})
			info = r.find('div',attrs={"class":"houseInfo"})
			
		4.获取文本
			.get_text()
	
	4. 示例
		from bs4 import BeautifulSoup
		
		html = "<div class='test'>秀儿</div><div class='test2'>地狱诗人</div>"
		soup = BeautifulSoup(html,'lxml')
		rList = soup.find_all('div',{'class':'text})
		for r  in rList:
			Info = r.find('div',attrs={"class":"houseInfo"}).get_text().split('/')
			print(info[0])
		
	5. 支持的解析库
		1. lxml   :  速度快，文档容错能力强
		2. html.parser  ： python 标准库，速度一般，文档容错能力一般
		3. xml	: 速度快，文档容错能力强

Scrapy网络爬虫框架
		1. 异步处理框架,可配置和可扩展程度非常高
		2. 安装
			1. Windows
				Anaconda Prompt : conda install Scrapy
				如果安装慢(使用如下清华镜像) :
				conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
				conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
				conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
				conda config --set show_channel_urls yes
				conda install Scrapy
			2. Ubuntu  安装scrapy框架
					1、安装依赖包 ：
						1、sudo apt-get install python3-dev
						2、sudo apt-get install python-pip
						3、sudo apt-get install libxml2-dev
						4、sudo apt-get install libxslt1-dev
						6、sudo apt-get install libffi-dev
						5、sudo apt-get install zlib1g-dev
						7、sudo apt-get install libssl-dev
					2. sudo pip3 install pyasn1==0.4.1
					3、安装Scrapy
							1、sudo pip3  install Scrapy           ####注意此处S为大写
Scrapy框架组成
		1. 引擎(Engine) : 整个框架核心
		
		2. 调度器(Scheduler)
				接受从引擎发过来的URL,入队列
				
		3. 下载器(Downloader)
				获取response,返回给爬虫程序
				
		4. 项目管道(Item Pipeline)
					数据处理
					
		5. 中间件
				1. 下载器中间件(Downloader Middlewares)
					处理引擎与下载器之间的请求及响应
				2. 蜘蛛中间件(Spider Middlewares)
					处理爬虫程序输入响应和输出结果以及新的请求

制作Scrapy爬虫项目步骤
		1. 新建项目
				scrapy startproject 项目名
				
		2. 明确目标(items.py)
			定义要爬取的数据结构
		
		3. 制作爬虫程序
				cd spiders
				scrapy genspider 文件名 域名
				
		4. 处理数据(pipelines.py)
		
		5. 全局配置(settings.py)
		
		6. 运行爬虫项目
			scrapy crawl 爬虫名
			
		7. scrapy项目文件
			1. 目录结构
				Baidu/
					|-- scrapy.cfg : 项目基本配置,不用改
					|-- Baidu/     : 项目目录
						|--items.py : 定义爬取数据结构
						|--middlewares.py : 中间件
						|--pipelines.py : 管道文件(数据)
						|--settings.py  : 全局配置
						|--spiders/ 
							|--baidu.py : 爬虫程序
				
		2. settings.py配置
			# 设置User-Agent
				USER_AGENT = 'Mozilla/5.0'
			
			#不输出试调信息
				LOG_LEVEL='WARNING'
				
			# 是否遵循robots协议,设置为False
				ROBOTSTXT_OBEY = False
				
			# 最大并发量,默认16
				CONCURRENT_REQUESTS = 32
				
			# 下载延迟时间
				DOWNLOAD_DELAY = 1
				
			# 请求头(也可以设置User-Agent)
				DEFAULT_REQUEST_HEADERS = {
					'User-Agent': 'Mozilla/5.0',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					'Accept-Language': 'en',
					}
			# 下载器中间件
				DOWNLOADER_MIDDLEWARES = {
					'Baidu.middlewares.randomProxyMiddleware': 543,
					'Baidu.middlewares.randomUserAgentMiddleware' : 300,
					}
					
			# 项目管道
				ITEM_PIPELINES = {
					'Baidu.pipelines.BaiduPipeline': 300,
					'Baidu.pipelines.BaiduMongoPipeline' : 200,
					'Baidu.pipelines.BaiduMysqlPipeline' : 100,
					}
				## 优先级1-1000,数字越小优先级越高

Pycharm运行Scrapy项目
		1. 项目写完之后创建begin.py(和scrapy.cfg同目录)
		2. begin.py
			from scrapy import cmdline
			cmdline.execute('scrapy crawl baidu'.split()) 
			
		3. 配置pycharm的python环境
			File -> settings -> Project Interpreter -> 右上角...add -> 
			existinig environment -> 选择你自己Anaconda中python的路径
			(C:\ProgramData\Anaconda3\python.exe) -> 点击OK



1. yield回顾
  1. 作用 : 把1个函数当做1个生成器使用
  2. 特点 : 让函数暂停,等待下1次调用
2. Csdn
  1. 网址https://blog.csdn.net/XiaoYi_Eric/article/details/85559389
  2. 标题 发表时间 阅读数
   标题://h1[@class="title-article"]/text()
   时间://span[@class="time"]/text()
   数量://span[@class="read-count"]/text()
3. 知识点
  1. extract() : 获取选择器对象中的文本内容
    response.xpath('')
    结果: [<selector ....,data='文本内容'>]
    response.xpath('').extract()[0]
    结果: '文本内容'
  2. 爬虫程序中,start_urls必须为列表
    start_urls = []
  3. pipelines.py中必须有1个函数叫:
     class CsdnPipeline(object):
        def process_item(self,item,spider):
            pass 
4. 腾讯招聘项目(数据持久化存储)
  1. 网站 : https://hr.tencent.com/position.php?&start=0
  2. Xpath匹配
    基准Xpath表达式 ：
    //tr[@class="even"]|//tr[@class="odd"]
    职位名称 : ./td[1]/a/text()
    职位类别 : ./td[2]/text()
    招聘人数 : ./td[3]/text()
    工作地点 : ./td[4]/text()
    发布时间 : ./td[5]/text()
    职位链接 : ./td[1]/a/@href
5. 日志级别及保存日志文件
   LOG_LEVEL = ''
   LOG_FILE = '文件名.log'
   5层警告级别
     1. CRITICAL 严重错误
     2. ERROR    一般错误
     3. WARNING  警告信息
     4. DEBUG    调试信息
     5. INFO     一般信息
	
6. 保存为csv或json文件
	1. scrapy crawl tengxun -o Tencent.json
			json文件编码问题 : 在settings.py中添加
	
				FEED_EXPORT_ENCODING = 'utf-8'
	
	2. scrapy crawl tengxun -o Tencent.csv
		csv文件出现空行的解决方法(修改源文件exporters.py):
		路径 C:\ProgramData\Anaconda3\Lib\site-packages\scrapy
		在exporters.py中搜索 csv,找csv的类,在 
			self.stream = io.TextIOWrapper(
				file,
				newline = ""  ## 添加此参数
		
	6. yield scrapy.Request(url,callback=self.parseHtml)
	
7. Daomu
  1. URL : http://www.daomubiji.com/dao-mu-bi-ji-1 
  2. 目标
    基准: 
      response.xpath('//article/a/text()').extract()
      # ["七星鲁王 第一章 血尸","... .. .."]
      i = 0 
      for r in []:
        标题
        章节数
        章节名称
        链接  '//article/a/@href'[i]
        i += 1
        yield item    
    

1. 创建项目Daomu
2. 创建爬虫文件 daomu 
3. 在pipelines.py中创建2个类(mysql和mongo)
4. 在settings.py中设置好管道(3个管道)
5. 在settings.py中设置相关选项(级别 DEBUG)	
		



scrapy shell 使用
	1. scrapy shell URL地址
	2. response.body ： bytes类型
	3. response.text  :  string 类型
	4. request.headers ： 请求头（字典)
	5. request.meta ： 定义代理等参数相关信息(字典)
	6. request.xpath('xpath表达式')

scrapy.Pequest()常用参数
	1. url ： URL地址
	2. callback ： 指定解析函数
	3. headers ：字典，请求头(不需要)
	4. meta ： 字典
			1.代理
			2. 在不同的请求之间传递数据
	5. dont_filter ： 是否忽略域组限制
		默认 False : 检查 allowed_domains
	
	6. encoding ： 默认utf-8


​	
下载器中间件(随机User-Agent)
​	1. settings.py(少量的User_Agent切换）
​		1. USER_AGENT = ''
​		2. DEFAULT_REQUEST_HEADERS={}
​	
​	2. middlewares.py 设置中间件
​		1. 项目目录中新建useragents.py 存放大量 User_Agent的列表
​		2. middlewares.py  定义相关类
​			import useragents
​			import random
​			class RandomUAmiddleware(object):
​					def process_request(self,request,spider):
​						useragent = random.choice(useragents.UA)
​						request.headers['User-Agent']=useragent
​						
		3. setting.py
			DOWNLOADER_MIDDLEWARES = [
				'项目名.middlewares.类名':200,
			]

下载器中间件(设置随机代理)
	1. 新建文件(proxies.py)
	2. middlewares.py(新建类)
	3. settings.py(启用中间件)
	
	
5. 升级Scrapy方法
	scrapy -v
	管理员 : Anaconda Prompt
	升级pip
		python -m pip install --upgrade pip 
	升级Scrapy
		pip install --upgrade Scrapy
	
6. CrawlSpider类
	1. Spider的派生类
		from scrapy.spiders import CrawlSpider
		定义了一些规则(Rule)来提供跟进链接,从爬取的网页中提取链接并继续爬取
		
	2. 提取链接的流程(LinkExtractor)
		1. scrapy shell 腾讯第一页的URL地址
		2. from scrapy.linkextractors import LinkExtractor
		3. LinkExtractor(allow='').extract_links(response)
	
  3. 创建爬虫文本模板(CrawlSpider类)
		scrapy genspider -t crawl 爬虫名 域名
		

分布式爬虫 安装工具	
	Anaconda Prompt
	1. pip install scrapy_redis
	
	2. redis

7. 腾讯招聘子页面爬取
	1. items.py去定义要爬取的数据结构
	2. 爬虫文件.py逻辑(不同解析函数间使用meta属性传递数据)
		def parse1():
			yiled scrapy.Request(url,callback=..,
                         meta={"item":item})
		def parse2():
			item = response.meta['item']
	
8. 分布式部署
	1. scrapy_redis模块
		Anaconda Prompt : 
		pip install scrapy_redis
	2. Redis 


9. 分布式原理 : 多台机器共享1个爬取队列 

10.实现分布式
  scrapy_redis(重写scrapy调度器)

11. 为什么使用redis
		1. Redis是非关系型数据库,key-value形式存储,结构灵活
		2. Redis集合,存储每个request的指纹(加密)
	
12. redis安装
	1. Windows
		1. 直接下载
    2. 启动并连接
		1. 服务端启动 : cmd终端 : redis-server
		2. 客户端连接 : redis-cli -h IP地址
    3. 安装图形界面管理工具
		RedisDesktopManger
		新建连接 + Connect to Redis Server 
  2. Ubuntu
		1.安装 
			sudo apt-get install redis-server
		2.启动 
			redis-server
		3.客户端连接
			redis-cli -h IP地址
	
13. scrapy_redis安装
		Anaconda Prompt

		pip install scrapy_redis



Day08回顾
1. Scrapy.Request()常用参数
  1. meta
    字典,定义代理信息,也可在不同请求之间传递数据
  2. dont_filter
    是否忽略域组限制,默认False
2. Downloader Middlewares(UA proxy)
  1. 新建文件存放列表 : 项目目录中
  2. middlewares.py定义相关类,方法名
    def process_request(self,request,spider):
      1. request.headers['User-Agent'] = ''
      2. request.meta['proxy'] = ''
  3. settings.py中开启下载器中间件
    DOWNLOADER_MIDDLEWARES={
      '项目名.middlewares.类名' : 200,
    }
3. CrawlSpider类
  1. 链接提取器
    scrapy shell中测试链接提取:
    from scrapy.linkextractors import LinkExtractor 
    LinkExtractor(allow=r'').extract_links(response)
  2. 快速创建CrawlSpider爬虫文件
    scrapy genspider -t crawl 爬虫名 域名
  3. 使用流程
    1. 导入模块
      from scrapy.linkextractors import LinkExtractor
      from scrapy.spiders import CrawlSpider,Rule
    2. 提取链接
      Link1 = LinkExtractor(allow=r'')
      Link2 = LinkExtractor(allow=r'')
    3. 定义Rule规则
      rules = (
        Rule(Link1,
             callback='',
             follow=True),
        Rule(Link2,
             callback='',
             follow=True)
      )
  4. CrawlSpider运行机制
    1. 爬虫名 允许域
    2. start_urls,获取第1个要爬取的URL
      1. LinkExtractor()提取链接
      2. 创建Rule()对象,指定解析函数,并继续跟进链接
4. 分布式原理(共享爬取队列)  
***********************************
1. redis_key使用
  1. 爬虫文件
    from scrapy_redis.spiders import RedisSpider
    class TengxunSpider(RedisSpider):
        # 去掉start_urls
        redis_key = 'tengxunspider:start_urls'
  2. 把项目拷贝到分布式的不同服务器上,运行项目
    scrapy crawl tengxun 
    或者
    cd spiders
    scrapy runspider tengxun.py
  3. 进入windows的redis,发送redis_key
    redis-cli -h IP地址
    
    >>>lpush tengxunspider:start_urls https://hr.tencent.com/...start=0
2. 验证码处理
  1. OCR(Optical Character Recognition)
     光学字符识别,通过字符形状-->电子文本
  2. tesseract-ocr(谷歌维护的OCR开源库,不能import))
    1. windows安装
      下载网址https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download
      安装完成后添加到环境变量
      默认安装路径
       C:\Program Files (x86)\Tesseract-OCR
    2. Ubuntu安装
       sudo apt-get install tesseract-ocr
    3. Mac : brew install tesseract
  3. 验证
    终端 ：tesseract test1.jpg XXX.txt
  4. python模块: pytesseract
    Anconda Prompt(管理员):
      conda install pytesseract
      pip install pytesseract
  5. pytesseract使用示例
    s=pytesseract.image_to_string(图片对象)
    示例代码：
    import pytesseract
    # Python的标准图片处理库
    from PIL import Image
    # 创建图片对象
    img = Image.open('test1.jpg')
    # 图片转字符串
    s = pytesseract.image_to_string(img)
    print(s)
3. 打码平台
  1. tesseract-ocr识别率很低,很多文字变形,干扰,识别不了
  2. 在线打码(识别率很高)
    1. 云打码网址 : http://www.yundama.com/
    2. 注册用户 - 充值 - 下载接口文档(开发文档)
    3. 题分价格(类型码,在程序中写正确)
4. scrapy抓取图片(360搜索引擎图片)
  1. 网址 ：http://image.so.com/z?ch=beauty
  2. F12抓包或者Fiddler抓包工具
    json地址：http://image.so.com/zj?ch=beauty&sn=0&listtype=new&temp=1
    通过分析,改变sn的值可以获取到不同图片
    sn = 0 显示1-30张图片信息
    sn = 30 显示31-60张图片信息
    ... ... 
5. 图片管道
  1. settings.py中定义存储路径
    IMAGES_STORE = 'E:\\Images'
  2. pipelines.py
    from scrapy.pipelines import ImagesPipeline
    # 定义类
    class GirlPipeline(ImagesPipeline):
        def get_media_requests(self,item,info):
          yield scrapy.Request(item['url'])
6. 重写爬虫文件的start_requests()方法
  1. 作用 : 不再爬取start_urls中地址
  2. 使用
    1. 先把start_urls去掉
    2. def start_requests(self):
           pass 
7. 手机端app抓取
  1. 设置手机(见图)
    1. 手动
      IP地址 ： 你电脑的IP(ipconfig)
      端口号 ： 8888(和Fiddler保持一致)
  2. 设置电脑(更改注册表)
  3. 设置Fiddler
    1. HTTPS选项卡 ：...from all processes 
    2. Connections选项卡
      1. 端口号 ：8888(和手机保持一致)
      2. Allow remote computers to Connect
    3. 重启Fiddler 	
		
























​        








​            


​        

​    






