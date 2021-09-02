from anti_useragent import UserAgent
# from fake_useragent import FakeUserAgent


if __name__ == '__main__':
    print(UserAgent(platform='mac').random)
    print(UserAgent()['firefox'])

    print(UserAgent(min_version=90, max_version=100).chrome)
    # print(FakeUserAgent().chrome)

    import anti_useragent

    print(anti_useragent.VERSION)
