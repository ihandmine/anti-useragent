from random import choice

from anti_useragent.useragent.chrome import ChromeUA
from anti_useragent.useragent.firefox import FirefoxUA
from anti_useragent.useragent.opera import OperaUA
from anti_useragent.exceptions import UserAgentError, AntiUserAgentError


class UserAgent(object):
    shortcut = {
        'chrome': ChromeUA,
        'firefox': FirefoxUA,
        'opera': OperaUA
    }

    def __init__(self, platform=None, version=None, logger=False):
        self.logger = logger
        self.platform = platform
        self.version = version

    def __getitem__(self, item):
        return self.__getattr__(item)

    def __getattr__(self, item):
        try:
            if item == 'random':
                attr = choice(list(self.shortcut.keys()))
                _ua = self.shortcut[attr](self.platform, self.version, self.logger)
                if not _ua.platform:
                    platform = choice(_ua.settings.get('PLATFORM'))
                    _ua.set_platform(platform)
                return getattr(_ua, 'ua')
            else:
                return getattr(self.shortcut[item](self.platform, self.version, self.logger), 'ua')
        except UserAgentError:
            raise AntiUserAgentError('Error occurred during getting useragent')


AntiUserAgent = UserAgent
