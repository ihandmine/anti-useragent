
BASE_USER_AGENT_FIREFOX = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s; rv:%(r_version)s)' \
                          ' Gecko/20100101 Firefox/%(version)s'

BASE_USER_AGENT_CHROME = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome' \
                         '/%(big_version)s.%(mid_version)s.%(small_version)s.%(beta_version)s Safari/537.36'

BASE_USER_AGENT_OPERA = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s) ' \
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome' \
                        '/%(big_version)s.%(mid_version)s.%(small_version)s.%(beta_version)s Safari/537.36 ' \
                        'OPR/%(o_version)s.0.%(os_version)s.%(ob_version)s'

BASE_USER_AGENT_CHROME_ANDROID = 'Mozilla/5.0 (Linux; Android %(android_version)s; '\
                                 '%(android_phone)s) AppleWebKit/%(safari)s (KHTML, like Gecko) '\
                                 'Chrome/%(chrome)s Mobile Safari/%(safari)s'

BASE_USER_AGENT_CHROME_IPHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS %(mac_version)s} like Mac OS X)'\
                                ' AppleWebKit/%(safari)s (KHTML, like Gecko) Version/9.0 Mobile/%(mobile)s Safari/%(safari)s'

BASE_USER_AGENT_WECHAT_IPHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS %(mac_version)s like Mac OS X) '\
                                'AppleWebKit/%(safari)s (KHTML, like Gecko) Mobile/%(mobile)s MicroMessenger/%(micro_messenger)s '\
                                'NetType/%(net_type)s Language/zh_CN'

BASE_USER_AGENT_WECHAT_ANDROID = 'Mozilla/5.0 (Linux; Android %(android_version)s; %(android_phone)s) '\
                                 'AppleWebKit/%(safari)s (KHTML, like Gecko) Version/4.0 Chrome/%(chrome)s Mobile MQQBrowser/6.2 '\
                                 'TBS/%(TBS)s Safari/%(safari)s MicroMessenger/%(micro_messenger)s NetType/%(net_type)s Language/zh_CN'

BASE_USER_AGENT_UC = 'Mozilla/5.0 (Linux; U; Android %(android_version)s; zh-cn; %(android_phone)s AppleWebKit/%(safari)s (KHTML, like Gecko)'\
                     ' Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/%(safari)s AliApp(TB/6.6.4) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21'

BASE_USER_AGENT_BAIDU_BOX_ANDROID = 'Mozilla/5.0 (Linux; Android %(android_version)s; %(android_phone)s) AppleWebKit/%(safari)s (KHTML, like Gecko) '\
                                    'Version/4.0 Chrome/%(chrome)s Mobile Safari/%(safari)s T7/7.4 baiduboxapp/%(baidu_box_app_android)s (Baidu; P1 %(android_version)s)'

BASE_USER_AGENT_BAIDU_BOX_IPHONE = 'Mozilla/5.0 (iPhone; CPU iPhone OS {mac_version} like Mac OS X) AppleWebKit/{safari} '\
                                   '(KHTML, like Gecko) Mobile/{mobile} baiduboxapp/{baidu_box_app_iphone}/2.01_4C2%258enohPi/1099a/{key}/1'

WIN_SYSTEM = [
    'Windows NT 5.0',
    'Windows NT 5.1',
    'Windows NT 6.0',
    'Windows NT 6.1',
    'Windows NT 6.2',
    'Windows NT 6.3',
    'Windows NT 10.0',
]

WIN_SYSTEM_BIT = [
    'Win64; x64',
    'WOW64',
]

MAC_SYSTEM = [
    'Macintosh',
]

MAC_SYSTEM_BIT = [
    'PPC Mac OS X',
    'Intel Mac OS X'
]

LINUX_SYSTEM = [
    'X11'
]

LINUX_SYSTEM_BIT = [
    'Linux ppc',
    'Linux ppc64',
    'Linux i686',
    'Linux x86_64',
]

PLATFORM = ['windows', 'mac', 'linux', 'android', 'iphone']

ANDROID_SYSTEM_LIST = [
    'Nexus 4 Build/KOT49H', 'Nexus 5 Build/MRA58N', 'Nexus 6 Build/LYZ28E',
    'Nexus 7 Build/JSS15Q', 'Nexus 8 Build/MRA58N', 'Nexus 9 Build/LYZ28E',
    # 三星
    'GT-I9152P Build/JLS36C', 'SM-E7000 Build/KTU84P', 'SM-G9200 Build/LMY47X',
    'GT-I9128I Build/JDQ39', 'GT-I9500 Build/JDQ39', 'SM-N9008V Build/LRX21V',
    'SM-N7506V Build/JLS36C', 'SM-G3609 Build/KTU84P', 'SCH-W2013 Build/IMM76D',
    # LG
    'LGMS323 Build/KOT49I.MS32310c',
    # OPPO/VIVO
    'OPPO R7 Build/KTU84P', 'OPPO R7t Build/KTU84P', 'R7007 Build/JLS36C', 'R2017 Build/JLS36C', 'R6007 Build/JLS36C',
    '1105 Build/KTU84P', 'N5117 Build/JLS36C', 'M571C Build/LMY47D', 'R7Plus Build/LRX21M', 'X909T Build/JDQ39',
    'A31t Build/KTU84P', 'A31 Build/KTU84P', 'R8207 Build/KTU84P', 'R833T Build/JDQ39',

    'vivo Y13iL Build/KTU84P', 'vivo X5Pro D Build/LRX21M', 'vivo Y22L Build/JLS36C', 'vivo Y13T Build/JDQ39',
    'vivo X5Max Build/KTU84P', 'ONE A2001 Build/LMY48W',
    # 华为
    'VIE-AL10 Build/HUAWEIVIE-AL10; wv', 'HUAWEI NXT-AL10 Build/HUAWEINXT-AL10', 'HUAWEI NXT-CL00 Build/HUAWEINXT-CL00',
    'Che2-TL00M Build/HonorChe2-TL00M; wv', 'FRD-AL10 Build/HUAWEIFRD-AL10', 'HUAWEI RIO-AL00 Build/HuaweiRIO-AL00',
    'HUAWEI C199 Build/HuaweiC199', 'HUAWEI RIO-TL00 Build/HUAWEIRIO-TL00; wv', 'HUAWEI TAG-TL00 Build/HUAWEITAG-TL00',
    'HUAWEI MT7-CL00 Build/HuaweiMT7-CL00; wv', 'PLE-703L Build/HuaweiMediaPad; wv', 'PLK-TL01H Build/HONORPLK-TL01H',
    'EVA-AL10 Build/HUAWEIEVA-AL10',
    # 小米
    'MI MAX Build/MMB29M', 'MI 5 Build/NRD90M', 'MI NOTE LTE Build/KTU84P', 'MI 3C Build/MMB29M', 'MI 5s Build/MXB48T',
    'MI NOTE LTE Build/MMB29M', 'MI 2S Build/JRO03L', 'MI 5 Build/MXB48T', 'MI NOTE Pro Build/LRX22G',
    # 联想ZUK
    'Z2 Plus Build/N2G47O; wv',
]

NET_TYPE = ['4G', 'WIFI']

PLATFORM_OVERRIDES = {
    'windows': [WIN_SYSTEM, WIN_SYSTEM_BIT],
    'mac': [MAC_SYSTEM, MAC_SYSTEM_BIT],
    'linux': [LINUX_SYSTEM, LINUX_SYSTEM_BIT],
    'android': [ANDROID_SYSTEM_LIST, NET_TYPE],
    'iphone': [ANDROID_SYSTEM_LIST, NET_TYPE],
}

PLATFORM_UA_MAP = {
    'android': [
        'chrome_android',
        'wechat_android',
        'baidu_android',
        'uc'
    ],
    'iphone': [
        'chrome_iphone',
        'wechat_iphone',
        'baidu_iphone',
    ],
    'windows': [
        'chrome',
        'firefox',
        'opera',
    ],
    'linux': [
        'chrome',
        'firefox',
        'opera',
    ],
    'mac': [
        'chrome',
        'firefox',
        'opera',
    ],
}
