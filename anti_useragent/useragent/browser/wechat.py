from anti_useragent.useragent import BaseUserAgent


class WechatAndroidUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 90)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='android')
        _ua = self.settings.get('BASE_USER_AGENT_CHROME_ANDROID') % {
            'android_version': self.utils.android_version(),
            'android_phone': self.utils.system_version(self.s_info, self.s_bit)[0],
            'chrome': self.utils.chrome(),
            'TBS': self.utils.tbs(),
            'safari': self.utils.safari(),
            'micro_messenger': self.utils.micro_message(),
            'net_type': self.utils.system_version(self.s_info, self.s_bit)[1]
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<WechatAndroid-UserAgent/ platform: %s/ max_version: %s>" % (self.platform, self.max_version)


class WechatIphoneUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 90)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='iphone')
        _ua = self.settings.get('BASE_USER_AGENT_WECHAT_IPHONE') % {
            'mac_version': self.utils.mac_version(),
            'safari': self.utils.safari(),
            'mobile': self.utils.key(6),
            'micro_messenger': self.utils.micro_message(),
            'net_type': self.utils.system_version(self.s_info, self.s_bit)[1]
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<WechatIphone-UserAgent/ platform: %s/ max_version: %s>" % (self.platform, self.max_version)
