from anti_useragent.settings import Settings
from anti_useragent.utils import logging
from anti_useragent.utils import misc


class BaseUserAgent:
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    def __init__(self, platform: str, min_version: int, max_version: int, logger, *args, **kwargs):
        self.settings = self._settings

        assert isinstance(self.min_version, int), 'Min Version must be int'
        assert isinstance(self.max_version, int), 'Max Version must be int'
        assert isinstance(platform or "", str), 'Platform must be string or NoneType'

        if all([platform, (platform not in self.settings.get('PLATFORM'))]):
            raise TypeError('Unknown platform type: %s' % platform)
        self.logger = logger
        self.platform = platform or 'windows'
        self.s_info = None
        self.s_bit = None

        if logger:
            self.logger = logging.get_logger('anti_useragent')

        self.utils = misc


    def set_platform(self, platform):
        self.platform = platform
        self.s_info = self.settings.get('PLATFORM_OVERRIDES')[platform][0]
        self.s_bit = self.settings.get('PLATFORM_OVERRIDES')[platform][1]

    @property
    def _settings(self) -> Settings:
        return Settings()
