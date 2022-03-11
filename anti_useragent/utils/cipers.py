import random
import ssl
import requests

from loguru import logger
from copy import deepcopy
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


ORIGIN_CIPHERS = 'ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-AES128-CCM8:ECDHE-ECDSA-AES256-CCM8:DHE-RSA-AES128-CCM:DHE-RSA-AES256-CCM:AES128-CCM8:AES256-CCM8:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8:ADH-AES128-SHA256:ADH-AES256-SHA256:ADH-AES128-GCM-SHA256:ADH-AES256-GCM-SHA384:AES128-CCM:AES256-CCM:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-DSS-AES128-SHA256:DHE-DSS-AES256-SHA256:DHE-DSS-AES128-GCM-SHA256:DHE-DSS-AES256-GCM-SHA384:DHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:RSA+AES128:ALL:!ADH:@STRENGTH:HIGH:DEFAULT:!DH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS'


class _SSLMethod(object):
    ssl_method = {
        'SSLv23': ssl.PROTOCOL_SSLv23,
        'TLSv1': ssl.PROTOCOL_TLSv1,
        'TLSv1_1': ssl.PROTOCOL_TLSv1_1,
        'TLSv1_2': ssl.PROTOCOL_TLSv1_2,
        'TLS': ssl.PROTOCOL_TLS,
        'TLS_CLIENT': ssl.PROTOCOL_TLS_CLIENT,
        'TLS_SERVER': ssl.PROTOCOL_TLS_SERVER,
    }

    ssl_context = {
        'SSLv2': ssl.OP_NO_SSLv2,
        'SSLv3': ssl.OP_NO_SSLv3,
        'TLSv1': ssl.OP_NO_TLSv1,
        'TLSv1_1': ssl.OP_NO_TLSv1_1,
        'TLSv1_2': ssl.OP_NO_TLSv1_2,
        'TLSv1_3': ssl.OP_NO_TLSv1_3,
    }

    def __init__(self, version=None):
        self.version: str = version or "TLSv1_2"

    @property
    def gen(self):
        return self.ssl_method[self.version]

    @property
    def context(self):
        del self.ssl_context[self.version]
        return self.ssl_context


class SSLFactory:
    def __init__(self):
        self.ciphers = ORIGIN_CIPHERS.split(":")

    def __call__(self, _ssl: str = 'TLSv1_2') -> ssl.SSLContext:
        _verion_set = _SSLMethod(_ssl).context
        random.shuffle(self.ciphers)
        ciphers = ":".join(self.ciphers) + ":!aNULL:!eNULL:!MD5"

        context = ssl.create_default_context()
        for ssl_option in _verion_set.values():
            context.options |= ssl_option
        context.set_ciphers(ciphers)
        return context


sslgen = SSLFactory()


def set_requests_cipers(func):
    """[jar3 anti spider] decorator requests package to use random cipers"""
    def inner(*args, **kwargs):
        global ORIGIN_CIPHERS
        cipers = deepcopy(ORIGIN_CIPHERS)
        requests.adapters.DEFAULT_RETRIES = 50
        requests.packages.urllib3.disable_warnings()
        cipers_list = cipers.split(':')
        random.shuffle(cipers_list)
        cipers_real = ':'.join(cipers_list)
        # logger.debug(cipers_real)
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = cipers_real
        return func(*args, **kwargs)
    return inner


def set_tls_protocol(version: str) -> requests.Session:
    """[jar3 anti spider] requtest package set tls version"""

    _version = _SSLMethod(version).gen

    class Ssl3HttpAdapter(HTTPAdapter):
        """"Transport adapter" that allows us to use SSLv3."""

        def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
            self.poolmanager = PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=_version)

    s = requests.Session()
    s.mount('https://', Ssl3HttpAdapter())
    return s


__all__ = [
    sslgen,
    set_tls_protocol,
    set_requests_cipers
]
