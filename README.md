# anti-useragent



> info: fake chrome, firefox, opera browser header anti useragent

## Features

- more browser up to date
- more randomize ruler
- grabs up to date `useragent` from [useragentstring.com](http://useragentstring.com/)

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

# and the best one, random via real world browser usage statistic
ua.random
# Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.3.8610.5 Safari/537.36
```



If You want to  specify the platform just: 

```python
from anti_useragent import UserAgent
ua = UserAgent(platform='mac')
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

