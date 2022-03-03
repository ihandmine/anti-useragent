from anti_useragent.useragent import BaseUserAgent


class ChromeUA(BaseUserAgent):
    """
    Mozilla/5.0 是一个通用标记符号，用来表示与 Mozilla 兼容，这几乎是现代浏览器的标配。
    platform 用来说明浏览器所运行的原生系统平台（例如 Windows、Mac、Linux 或 Android），以及是否运行在手机上。搭载 Firefox OS 的手机仅简单地使用了 "Mobile" 这个字符串；因为 web 本身就是平台。注意 platform 可能会包含多个使用 "; " 隔开的标记符号。参见下文获取更多的细节信息及示例。
    Chrome （或 Chromium/blink-based engines）用户代理字符串与 Firefox 的格式类似。为了兼容性，它添加了诸如 "KHTML, like Gecko" 和 "Safari" 这样的字符串。

    example:
        Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
    platform:
        windows
        mac
        linux
    """

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 100)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(self.platform)
        _system = self.utils.system_version(self.s_info, self.s_bit)
        _version = self.utils.chrome(self.min_version, self.max_version).split('.')
        _ua = self.settings.get('BASE_USER_AGENT_CHROME') % {
            'system_info': _system[0],
            'system_bit': _system[1],
            'big_version': _version[0],
            'mid_version': _version[1],
            'small_version': _version[2],
            'beta_version': _version[3],
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<Chrome-UserAgent/ platform: %s/ max_version: %s>" % (self.platform, self.max_version)


class ChromeAndroidUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 100)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='android')
        _ua = self.settings.get('BASE_USER_AGENT_CHROME_ANDROID') % {
            'android_version': self.utils.android_version(),
            'android_phone': self.utils.system_version(self.s_info, self.s_bit)[0],
            'chrome': self.utils.chrome(self.min_version, self.max_version),
            'safari': self.utils.safari()
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<ChromeAndroid-UserAgent/ platform: %s/ max_version: %s>" % ("android", self.max_version)


class ChromeIphoneUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 100)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='iphone')
        _ua = self.settings.get('BASE_USER_AGENT_CHROME_IPHONE') % {
            'mac_version': self.utils.mac_version(),
            'mobile': self.utils.key(),
            'safari': self.utils.safari()
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<ChromeIphone-UserAgent/ platform: %s/ max_version: %s>" % ("iphone", self.max_version)
