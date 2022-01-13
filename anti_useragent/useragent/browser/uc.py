from anti_useragent.useragent import BaseUserAgent


class UcUA(BaseUserAgent):

    def __init__(self, *args, **kwargs):
        self.min_version = getattr(self, 'min_version', 55)
        self.max_version = getattr(self, 'max_version', 90)
        super().__init__(*args, **kwargs)

    @property
    def ua(self):
        self.set_platform(platform='android')
        _ua = self.settings.get('BASE_USER_AGENT_UC') % {
            'android_version': self.utils.android_version(),
            'android_phone': self.utils.system_version(self.s_info, self.s_bit)[0],
            'safari': self.utils.safari()
        }
        if self.logger:
            self.logger.debug(_ua)
        return _ua

    def __repr__(self):
        return "<Uc-UserAgent/ platform: %s/ max_version: %s>" % ("android", self.max_version)
