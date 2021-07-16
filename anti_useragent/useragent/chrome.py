from random import randint, choice
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
        super().__init__(*args, **kwargs)
        if not self.version:
            self.version = 90

    @property
    def ua(self):
        self.set_platform(self.platform)
        _ua = self.settings.get('BASE_USER_AGENT_CHROME') % {
            'system_info': choice(self.s_info),
            'system_bit': choice(self.s_bit),
            'big_version': randint(55, self.version),
            'mid_version': randint(0, 9),
            'small_version': randint(3000, 9999),
            'beta_version': randint(0, 9),
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<Chrome-UserAgent/ platform: %s/ max_version: %s>" % (self.platform, self.version)


