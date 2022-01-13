from anti_useragent.useragent import BaseUserAgent


class BaiduAndroidUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 90)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='android')
        _ua = self.settings.get('BASE_USER_AGENT_BAIDU_BOX_ANDROID') % {
            'android_version': self.utils.android_version(),
            'android_phone': self.utils.system_version(self.s_info, self.s_bit)[0],
            'chrome': self.utils.chrome(),
            'baidu_box_app_android': self.utils.baidu_box_app(p='android'),
            'safari': self.utils.safari()
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<BaiduAndroid-UserAgent/ platform: %s/ max_version: %s>" % ('android', self.max_version)


class BaiduIphoneUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 90)
        super().__init__(*args, **kwargs)


    @property
    def ua(self):
        self.set_platform(platform='iphone')
        _ua = self.settings.get('BASE_USER_AGENT_BAIDU_BOX_IPHONE').format(**{
            'mac_version': self.utils.mac_version(),
            'safari': self.utils.safari(),
            'mobile': self.utils.key(6),
            'baidu_box_app_iphone': self.utils.baidu_box_app(p='iphone'),
            'key': self.utils.key(51),
        })
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<BaiduIphone-UserAgent/ platform: %s/ max_version: %s>" % ('iphone', self.max_version)
