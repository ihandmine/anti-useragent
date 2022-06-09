# anti-useragent



> info: fake pc or app browser useragent, anti useragent, and other awesome tools

## Features

- more browser up to date
- more randomize ruler
- more fun awesome tools

English | [中文](./doc/README_ZH.md)

### Installation

```shell
pip install anti-useragent
```

### Usage

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

### Supported platform

| browser/platfom | windows | mac  | linux | iphone | android |
| :-------------: | :-----: | :--: | :---: | :----: | :-----: |
|   **chrome**    |    ✔    |  ✔   |   ✔   |   ✔    |    ✔    |
|   **firefox**   |    ✔    |  ✔   |   ✔   |   ❌    |    ❌    |
|    **opera**    |    ✔    |  ✔   |   ✔   |   ❌    |    ❌    |
|   **wechat**    |    ❌    |  ❌   |   ❌   |   ✔    |    ✔    |
|    **baidu**    |    ❌    |  ❌   |   ❌   |   ✔    |    ✔    |
|     **uc**      |    ❌    |  ❌   |   ❌   |   ❌    |    ✔    |

If You want to  specify the platform just: 

```python
from anti_useragent import UserAgent
ua = UserAgent(platform='mac') # windows, linux, android, iphone
```

If You want to  specify the browser max version or min version just: 

```python
from anti_useragent import UserAgent
ua = UserAgent(max_version=90)

ua = UserAgent(min_version=50)
```

If You want to  specify the enable logger just: 

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



Make sure that You using latest version

```
pip install -U anti-useragent
```

Check version via python console: 

```
import anti_useragent

print(anti_useragent.VERSION)
```
Add awesome tools usage:
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
