# anti-useragent



> 信息: 伪装PC端APP端浏览器的用户浏览器UA头，反用户代理, UA指纹，和其他实用的工具方法

## 特性

- 更多的浏览器支持
- 更多的随机规则
- 更多有趣的工具集

[English](../README.md) | 中文

### 安装

```shell
pip install anti-useragent
```

### 用法

```python
from anti_useragent import UserAgent
ua = UserAgent()

ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36
ua['chrome']
# Mozilla/5.0 (Windows NT 5.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.2.3576.5 Safari/537.36
ua.firefox
# Mozilla/5.0 (Windows NT 5.1; WOW64; rv:47.0) Gecko/20100101 Firefox/45.0
ua['firefox']
# Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/31.0
ua.android
# Mozilla/5.0 (Linux; Android 7.5.2; M571C Build/LMY47D) AppleWebKit/666.7 (KHTML, like Gecko) Chrome/72.7.7953.78 Mobile Safari/666.7
ua.iphone
# Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/349.56 (KHTML, like Gecko) Mobile/J9UMJN baiduboxapp/0_17.7.6.6_enohpi_8957_628/2.01_4C2%258enohPi/1099a/P0SJ2RX4DXJT3RW906040KVOSH2E76RJUNHVIJUPCJQCZMEM2GL/1
ua.wechat
# Mozilla/5.0 (Linux; Android 10.9.8; MI 5 Build/NRD90M) AppleWebKit/536.93 (KHTML, like Gecko) Chrome/81.7.8549.56 Mobile Safari/536.93

# and the best one, random via real world browser usage statistic
ua.random
# Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36
```

### 支持平台

| browser/platfom | windows | mac  | linux | iphone | android |
| :-------------: | :-----: | :--: | :---: | :----: | :-----: |
|   **chrome**    |    ✔    |  ✔   |   ✔   |   ✔    |    ✔    |
|   **firefox**   |    ✔    |  ✔   |   ✔   |   ❌    |    ❌    |
|    **opera**    |    ✔    |  ✔   |   ✔   |   ❌    |    ❌    |
|   **wechat**    |    ❌    |  ❌   |   ❌   |   ✔    |    ✔    |
|    **baidu**    |    ❌    |  ❌   |   ❌   |   ✔    |    ✔    |
|     **uc**      |    ❌    |  ❌   |   ❌   |   ❌    |    ✔    |

如果你想要指定平台: 

```python
from anti_useragent import UserAgent
ua = UserAgent(platform='mac') # windows, iphone, android, linux
```

如果你想要指定最大最小随机版本: 

```python
from anti_useragent import UserAgent
ua = UserAgent(max_version=90)

ua = UserAgent(min_version=50)
```

如果你要使用了loguru日志开启: 

```python
from anti_useragent import UserAgent
ua = UserAgent(logger=True)

# the default install loguru
try:
    from loguru import logger
except:
    install("loguru")
    from loguru import logger
```



确保你的包是最新版本

```
pip install -U anti-useragent
```

检查你的版本通过python控制台: 

```
import anti_useragent

print(anti_useragent.VERSION)
```
增加一些实用的工具使用方法:
```python
# requests:
from anti_useragent.utils.cipers import set_requests_cipers, set_tls_protocol

# ja3 tls verify
@set_requests_cipers
def get_html():
    requests.get(...)

# ja3 tls version
session = set_tls_protocol(version="TLSv1_2")


# aiohttp:
from anti_useragent.utils.cipers import sslgen
async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
    # ja3 tls verify
    await session.get(..., ssl=sslgen())

    # ja3 tls version
    await session.get(..., ssl=sslgen(_ssl="TLSv1_2"))

# scrapy:
# settings.py ja3 tls verify
DOWNLOADER_CLIENTCONTEXTFACTORY = 'anti_useragent.utils.scrapy_contextfactory.Ja3ScrapyClientContextFactory'

```
