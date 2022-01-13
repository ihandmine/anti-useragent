import sys
import string
import subprocess

from random import randint, choice


class Utils(object):

    def install(self, package):
        subprocess.call([sys.executable, "-m", "pip", "install", package])

    def android_version(self) -> str:
        return '{0}.{1}.{2}'.format(randint(4, 11), randint(0, 9), randint(0, 9))

    def system_version(self, info, bit) -> tuple:
        return choice(info), choice(bit)

    def chrome(self, miv=50, mav=90) -> str:
        return '{0}.{1}.{2}.{3}'.format(randint(miv, mav), randint(0, 9), randint(3000, 9999), randint(10, 99))

    def safari(self) -> str:
        return '{0}.{1}'.format(randint(100, 999), randint(0, 99))

    def mac_version(self) -> str:
        return '{}_{}_{}'.format(randint(6, 12), randint(1, 9), randint(1, 9))

    def windows_version(self) -> str:
        return '{}.{}'.format(randint(6, 10), randint(0, 9))

    def key(self, length=6) -> str:
        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(length))

    def firefox(self, miv=10, mav=50) -> tuple:
        return '{}.0'.format(randint(miv, mav)), '{}.0'.format(randint(20, 60))

    def opera(self, mav=90) -> str:
        return '{}.{}.{}'.format(randint(30, mav), randint(1000, 9999), randint(10, 99))

    def micro_message(self) -> str:
        return '6.{0}.{1}.{2}'.format(randint(0, 9), randint(0, 9), randint(1, 9999))

    def tbs(self) -> str:
        return str(randint(1, 999999)).zfill(6)

    def baidu_box_app(self, p='android'):
        if p == 'android':
            return '{}.{}'.format(randint(1, 8), randint(0, 9))
        elif p == 'iphone':
            return '0_{}.{}.{}.{}_enohpi_{}_{}'.format(
                randint(1, 20),
                randint(0, 9),
                randint(0, 9),
                randint(0, 9),
                str(randint(999, 9999)).zfill(4),
                str(randint(1, 999)).zfill(3)
            )
