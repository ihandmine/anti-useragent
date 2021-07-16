
BASE_USER_AGENT_FIREFOX = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s; rv:%(r_version)s)' \
                          ' Gecko/20100101 Firefox/%(version)s'

BASE_USER_AGENT_CHROME = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome' \
                         '/%(big_version)d.%(mid_version)d.%(small_version)d.%(beta_version)d Safari/537.36'

BASE_USER_AGENT_OPERA = 'Mozilla/5.0 (%(system_info)s; %(system_bit)s) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome' \
                         '/%(big_version)d.%(mid_version)d.%(small_version)d.%(beta_version)d Safari/537.36 ' \
                         'OPR/%(o_version)s.0.%(os_version)s.%(ob_version)s'


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

PLATFORM = ['windows', 'mac', 'linux']

PLATFORM_OVERRIDES = {
    'windows': [WIN_SYSTEM, WIN_SYSTEM_BIT],
    'mac': [MAC_SYSTEM, MAC_SYSTEM_BIT],
    'linux': [LINUX_SYSTEM, LINUX_SYSTEM_BIT]
}
