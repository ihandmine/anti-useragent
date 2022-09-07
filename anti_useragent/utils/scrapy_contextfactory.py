import random

from twisted.internet.ssl import CertificateOptions, AcceptableCiphers
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

ORIGIN_CIPHERS = 'ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-AES128-CCM8:ECDHE-ECDSA-AES256-CCM8:DHE-RSA-AES128-CCM:DHE-RSA-AES256-CCM:AES128-CCM8:AES256-CCM8:DHE-RSA-AES128-CCM8:DHE-RSA-AES256-CCM8:ADH-AES128-SHA256:ADH-AES256-SHA256:ADH-AES128-GCM-SHA256:ADH-AES256-GCM-SHA384:AES128-CCM:AES256-CCM:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA256:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-DSS-AES128-SHA256:DHE-DSS-AES256-SHA256:DHE-DSS-AES128-GCM-SHA256:DHE-DSS-AES256-GCM-SHA384:DHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES128-GCM-SHA256:AES256-SHA256:AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:RSA+AES128:ALL:!ADH:@STRENGTH:HIGH:DEFAULT:!DH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS'



class CipherFactory:
    def __init__(self, cipher: str = None):
        if cipher is None:
            cipher = ORIGIN_CIPHERS
        self.cipher = cipher

    @classmethod
    def setter_cipher(cls, val: str = None):
        return cls(val)

    def __call__(self) -> str:
        ciphers_list = self.cipher.split(':')
        random.shuffle(ciphers_list)
        ciphers_real = ':'.join(ciphers_list)
        return ciphers_real


generate_cipher = CipherFactory()


class Ja3ScrapyClientContextFactory(ScrapyClientContextFactory):

    def getCertificateOptions(self):
        tls_ciphers = generate_cipher()
        self.tls_ciphers = AcceptableCiphers.fromOpenSSLCipherString(
            tls_ciphers)
        return CertificateOptions(
            verify=False,
            method=getattr(self, 'method', getattr(self, '_ssl_method', None)),
            fixBrokenPeers=True,
            acceptableCiphers=self.tls_ciphers
        )
