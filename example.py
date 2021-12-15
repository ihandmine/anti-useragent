# encoding=utf8
import random as rd
import string

net_type = ['4G', 'WIFI']

# 感谢chrome
# https://www.fynas.com提供Android机型、手机浏览器大全
android_phone_list = [
    'Nexus 4 Build/KOT49H', 'Nexus 5 Build/MRA58N', 'Nexus 6 Build/LYZ28E',
    'Nexus 7 Build/JSS15Q', 'Nexus 5 Build/MRA58N', 'Nexus 6 Build/LYZ28E',
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


def rand_android_version():
    return '{0}.{1}.{2}'.format(rd.randint(4, 7), rd.randint(0, 9), rd.randint(0, 9))


def rand_android_phone():
    return rd.choice(android_phone_list)


def rand_chrome():
    return '{0}.{1}.{2}.{3}'.format(rd.randint(20, 59), rd.randint(0, 9), rd.randint(1000, 9999), rd.randint(10, 99))


def rand_safari():
    return '{0}.{1}'.format(rd.randint(100, 999), rd.randint(0, 99))


def rand_mac_version():
    return '{}_{}_{}'.format(rd.randint(6, 12), rd.randint(1, 9), rd.randint(1, 9))


def rand_windows_version():
    return '{}.{}'.format(rd.randint(6, 10), rd.randint(0, 9))


def rand_key(length=6):
    return ''.join(rd.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def rand_firefox():
    return '{}.0'.format(rd.randint(20, 60))


class ImNotSpider:
    def random(self):
        d = rd.choice([self.pc, self.wap])
        return d()

    def pc(self):
        d = rd.choice([self.pc_linux, self.pc_windows, self.pc_mac])
        return d()

    def wap(self):
        d = rd.choice([self.android, self.iphone])
        return d()

    def pc_linux(self):
        d = rd.choice([self.chrome_pc_linux, self.firefox_pc_linux])
        return d()

    def pc_windows(self):
        d = rd.choice(
            [self.chrome_pc_windows, self.firefox_pc_windows, self.internet_explorer])
        return d()

    def pc_mac(self):
        d = rd.choice([self.chrome_pc_mac, self.firefox_pc_mac])
        return d()

    def internet_explorer(self):
        return rd.choice(['Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko',
                          'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
                          'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)', ])

    def chrome_pc(self):
        d = rd.choice(
            [self.chrome_pc_linux, self.chrome_pc_mac, self.chrome_pc_windows])
        return d()

    def chrome_pc_linux(self):
        return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Safari/{Safari}'.format(
            **{'Chrome': rand_chrome(), 'Safari': rand_safari(), })

    def chrome_pc_mac(self):
        return 'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Safari/{Safari}'.format(
            **{'mac_version': rand_mac_version(), 'Chrome': rand_chrome(), 'Safari': rand_safari(), })

    def chrome_pc_windows(self):
        return 'Mozilla/5.0 (Windows NT {WindowsNT}; WOW64) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Safari/{Safari}'.format(
            **{'WindowsNT': rand_windows_version(), 'Chrome': rand_chrome(), 'Safari': rand_safari(), })

    def firefox_pc(self):
        d = rd.choice(
            [self.firefox_pc_linux, self.firefox_pc_mac, self.firefox_pc_windows])
        return d()

    def firefox_pc_linux(self):
        return 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{Firefox}) Gecko/20100101 Firefox/{Firefox}'.format(
            **{'Firefox': rand_firefox(), })

    def firefox_pc_mac(self):
        return 'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}; rv:{Firefox}) Gecko/20100101 Firefox/{Firefox}'.format(
            **{'mac_version': rand_mac_version(), 'Firefox': rand_firefox(), })

    def firefox_pc_windows(self):
        return 'Mozilla/5.0 (Windows NT {WindowsNT}; WOW64; rv:{Firefox}) Gecko/20100101 Firefox/{Firefox}'.format(
            **{'WindowsNT': rand_windows_version(), 'Firefox': rand_firefox(), })

    def android(self):
        d = rd.choice(
            [self.wechat_android, self.uc_browser_android, self.baidu_box_app_android, self.chrome_wap_android])
        return d()

    def iphone(self):
        d = rd.choice(
            [self.wechat_iphone, self.baidu_box_app_iphone, self.chrome_wap_iphone])
        return d()

    def chrome_wap(self):
        d = rd.choice([self.chrome_wap_android, self.chrome_wap_iphone])
        return d()

    def chrome_wap_android(self):
        return 'Mozilla/5.0 (Linux; Android {androidVersion}; {androidPhone}) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Mobile Safari/{Safari}'.format(
            **{'androidVersion': rand_android_version(), 'androidPhone': rand_android_phone(),
               'Chrome': rand_chrome(), 'Safari': rand_safari(), })

    def chrome_wap_iphone(self):
        return 'Mozilla/5.0 (iPhone; CPU iPhone OS {mac_version} like Mac OS X) AppleWebKit/{Safari} (KHTML, like Gecko) Version/9.0 Mobile/{Mobile} Safari/{Safari}'.format(
            **{'mac_version': rand_mac_version(), 'Safari': rand_safari(), 'Mobile': rand_key(6), })

    def wechat(self):
        return rd.choice([self.wechat_android, self.wechat_iphone])

    def wechat_android(self):
        return 'Mozilla/5.0 (Linux; Android {androidVersion}; {androidPhone}) AppleWebKit/{Safari} (KHTML, like Gecko) Version/4.0 Chrome/{Chrome} Mobile MQQBrowser/6.2 TBS/{TBS} Safari/{Safari} MicroMessenger/{MicroMessenger} NetType/{NetType} Language/zh_CN'.format(
            **{'androidVersion': rand_android_version(), 'androidPhone': rand_android_phone(),
               'Chrome': rand_chrome(), 'TBS': str(rd.randint(1, 999999)).zfill(6), 'Safari': rand_safari(),
               'MicroMessenger': '6.{0}.{1}.{2}'.format(rd.randint(0, 9), rd.randint(0, 9), rd.randint(1, 9999)),
               'NetType': rd.choice(net_type)})

    def wechat_iphone(self):
        return 'Mozilla/5.0 (iPhone; CPU iPhone OS {mac_version} like Mac OS X) AppleWebKit/{Safari} (KHTML, like Gecko) Mobile/{Mobile} MicroMessenger/{MicroMessenger} NetType/{NetType} Language/zh_CN'.format(
            **{'mac_version': rand_mac_version(), 'Safari': rand_safari(), 'Mobile': rand_key(6),
               'MicroMessenger': '6.{0}.{1}.{2}'.format(rd.randint(0, 9), rd.randint(0, 9), rd.randint(1, 9999)),
               'NetType': rd.choice(net_type)})

    def uc_browser_android(self):
        '''android only'''
        return 'Mozilla/5.0 (Linux; U; Android {androidVersion}; zh-cn; {androidPhone}) AppleWebKit/{Safari} (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/{Safari} AliApp(TB/6.6.4) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21'.format(
            **{'androidVersion': rand_android_version(), 'androidPhone': rand_android_phone(),
               'Safari': rand_safari(), })

    def baidu_box_app(self):
        '''手机百度'''
        return rd.choice([self.baidu_box_app_android, self.baidu_box_app_iphone])

    def baidu_box_app_android(self):
        return 'Mozilla/5.0 (Linux; Android {androidVersion}; {androidPhone}) AppleWebKit/{Safari} (KHTML, like Gecko) Version/4.0 Chrome/{Chrome} Mobile Safari/{Safari} T7/7.4 baiduboxapp/8.4 (Baidu; P1 {androidVersion})'.format(
            **{'androidVersion': rand_android_version(), 'androidPhone': rand_android_phone(),
               'Chrome': rand_chrome(),
               'baiduboxapp': '{}.{}'.format(rd.randint(1, 8), rd.randint(0, 9)), 'Safari': rand_safari(), })

    def baidu_box_app_iphone(self):
        return 'Mozilla/5.0 (iPhone; CPU iPhone OS {mac_version} like Mac OS X) AppleWebKit/{Safari} (KHTML, like Gecko) Mobile/{Mobile} baiduboxapp/{baiduboxapp}/2.01_4C2%258enohPi/1099a/{key}/1'.format(
            **{'mac_version': rand_mac_version(), 'Safari': rand_safari(), 'Mobile': rand_key(6),
               'baiduboxapp': '0_{}.{}.{}.{}_enohpi_{}_{}'.format(rd.randint(1, 20), rd.randint(0, 9),
                                                                  rd.randint(
                                                                      0, 9), rd.randint(0, 9),
                                                                  str(rd.randint(999, 9999)).zfill(
                                                                      4),
                                                                  str(rd.randint(1, 999)).zfill(3)),
               'key': rand_key(51),
               }
        )


if __name__ == '__main__':
    ins = ImNotSpider()
    print(ins.chrome_pc())
