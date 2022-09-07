from random import choice
from typing import Set, Optional

from anti_useragent.useragent import browser
from anti_useragent.settings import Settings
from anti_useragent.exceptions import UserAgentError, AntiUserAgentError


class UserAgent(object):
    _shortcut = {
        'chrome': browser.ChromeUA,
        'firefox': browser.FirefoxUA,
        'opera': browser.OperaUA,
        'chrome_android': browser.ChromeAndroidUA,
        'chrome_iphone': browser.ChromeIphoneUA,
        'wechat_android': browser.WechatAndroidUA,
        'wechat_iphone': browser.WechatIphoneUA,
        'baidu_android': browser.BaiduAndroidUA,
        'baidu_iphone': browser.BaiduIphoneUA,
        'uc': browser.UcUA
    }

    def __init__(self, 
                platform: Optional[str] = None,
                versions: Set[int]=None, 
                logger: object=False,
                min_version: Optional[int] = None,
                max_version: Optional[int] = None
                ):
        self.logger = logger
        self.platform = platform
        if versions is not None:
            self.min_version = versions[0]
            self.max_version = versions[1]
        else:
            self.min_version = min_version
            self.max_version = max_version
        self.settings = self.from_settings
        self._platform_ua_map = self.settings.get('PLATFORM_UA_MAP')

    @property
    def from_settings(self) -> Settings:
        return Settings()

    def __getitem__(self, rule):
        return self.__getattr__(rule)

    def __getattr__(self, rule: str) -> Optional[str]:
        try:
            if rule != 'random':
                _item_rule = [item for item in list(self._shortcut.keys()) if rule in item]
                _item_rule = [item for item in self._platform_ua_map[self.platform]
                                  if rule in item] if self.platform else _item_rule
                return getattr(
                    self._shortcut[
                        ''.join(choice(_item_rule) if _item_rule else []) or rule
                        ](
                            platform=self.platform, 
                            min_version=self.min_version, 
                            max_version=self.max_version, 
                            logger=self.logger
                        ),
                    'ua')
            if not self.platform:
                _attr = choice(list(self._shortcut.keys()))
                _ua = self._shortcut[_attr](
                    platform=self.platform, 
                    min_version=self.min_version, 
                    max_version=self.max_version, 
                    logger=self.logger
                )
                _ua.set_platform(choice(_ua.settings.get('PLATFORM')))
                return getattr(_ua, 'ua')
            else:
                _attr = choice(self._platform_ua_map[self.platform])
                _ua=self._shortcut[_attr](
                    platform=self.platform, 
                    min_version=self.min_version, 
                    max_version=self.max_version, 
                    logger=self.logger
                )
                return getattr(_ua, 'ua')
        except UserAgentError:
            raise AntiUserAgentError('Error occurred during getting useragent.')
        except KeyError:
            raise AntiUserAgentError('The platform unsupported browser.')

AntiUserAgent = UserAgent
