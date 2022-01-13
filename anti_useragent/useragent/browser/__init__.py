from .baidu import BaiduAndroidUA, BaiduIphoneUA
from .chrome import ChromeAndroidUA, ChromeIphoneUA, ChromeUA
from .firefox import FirefoxUA
from .opera import OperaUA
from .uc import UcUA
from .wechat import WechatIphoneUA, WechatAndroidUA


__all__ = [
    BaiduAndroidUA, BaiduIphoneUA,
    ChromeAndroidUA, ChromeIphoneUA, ChromeUA,
    FirefoxUA,
    OperaUA,
    UcUA,
    WechatIphoneUA, WechatAndroidUA
]
