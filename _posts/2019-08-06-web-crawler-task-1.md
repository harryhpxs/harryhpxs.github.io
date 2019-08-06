---
layout: post
title:  "爬虫 Task1"
author: Harry
---

### 1. 学习get与post请求

#### 1.1 学习get与post请求，尝试使用requests或者是urllib用get方法向 https://www.baidu.com/ 发出一个请求，并将其返回结果输出。

```python
import requests
res = requests.get('https://www.baidu.com/')

print(res.status_code)
print(res.headers)
#print(res.text)
```

```bash
200
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 06 Aug 2019 12:38:50 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:24:33 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
```

#### 1.2 如果是断开了网络，再发出申请，结果又是什么。了解申请返回的状态码。

断网后再发出申请会报错：

```bash
SSLError: HTTPSConnectionPool(host='www.baidu.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: SysCallError(10053, 'WSAECONNABORTED')",),))
```

HTTP 响应代码
- 200 OK 请求成功
- 404 Not Found 请求失败
等等...

参考: https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status

#### 1.3 了解什么是请求头，如何添加请求头。

> 请求头可以被定义为：被用于http请求中并且和请求主体无关的那一类HTTP header。某些请求头如Accept, Accept-*,  If-*允许执行条件请求。某些请求头如：Cookie, User-Agent 和Referer描述了请求本身以确保服务端能返回正确的响应。

参考: https://developer.mozilla.org/zh-CN/docs/Glossary/%E8%AF%B7%E6%B1%82%E5%A4%B4

Requests 添加请求头
```python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

res = requests.get(url, headers=headers)
```
参考: https://2.python-requests.org/en/latest/user/quickstart/#custom-headers

### 2. 正则表达式

#### 2.1 学习什么是正则表达式并尝试一些正则表达式并进行匹配。

```bash
# 匹配 URL
^(((https?|ftp):\/\/)?([\w\-\.])+(\.)([\w]){2,4}([\w\/+=%&_\.~?\-]*))*$
```

参考:
1. https://regex101.com/
2. https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

#### 2.2 结合requests、re两者的内容爬取 https://movie.douban.com/top250 里的内容。

#### 2.3 抓取名次、影片名称、年份、导演等字段。
