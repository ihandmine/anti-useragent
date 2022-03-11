from anti_useragent import UserAgent, sslgen
import anti_useragent
# from fake_useragent import FakeUserAgent


if __name__ == '__main__':
    # print(UserAgent(platform='mac').random)
    # print(UserAgent()['firefox'])

    # print(UserAgent(min_version=90, max_version=100).chrome)
    # # print(FakeUserAgent().chrome)

    # import anti_useragent

    # print(anti_useragent.VERSION)

    # print(UserAgent()['chrome'])
    # print(UserAgent()['firefox'])
    # print(UserAgent()['opera'])
    # print(UserAgent()['chrome_android'])
    # print(UserAgent()['chrome_iphone'])
    # print(UserAgent()['wechat_android'])
    # print(UserAgent()['wechat_iphone'])
    # print(UserAgent()['baidu_android'])
    # print(UserAgent()['uc'])
    # print(UserAgent()['baidu_iphone'])

    # print(UserAgent().wechat)
    print(sslgen())
