from anti_useragent.settings import Settings
from anti_useragent.utils import logging


class BaseUserAgent:
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            cls._INSTANCE = super().__new__(cls)
        return cls._INSTANCE

    def __init__(self, platform: str, min_version: int, max_version: int, logger, *args, **kwargs):
        self.settings = self._settings
        if min_version or max_version:
            assert isinstance(min_version, int), 'Min Version must be int'
            assert isinstance(max_version, int), 'Max Version must be int'
        if platform:
            assert isinstance(platform, str), 'Platform must be string'
        if all([platform, (platform not in self.settings.get('PLATFORM'))]):
            raise TypeError('Unknown platform type: %s' % platform)

        self.logger = logger
        self.platform = platform
        self.min_version = min_version
        self.max_version = max_version
        self.s_info = None
        self.s_bit = None

        if logger:
            self.logger = logging.get_logger('anti_useragent')

    def set_platform(self, platform):
        if not platform:
            platform = 'windows'
        self.platform = platform
        self.select_params(self.platform)

    def select_params(self, platform):
        assert platform, 'Must be have param platform'
        self.s_info = self.settings.get('PLATFORM_OVERRIDES')[platform][0]
        self.s_bit = self.settings.get('PLATFORM_OVERRIDES')[platform][1]

    @property
    def _settings(self) -> Settings:
        return Settings()
