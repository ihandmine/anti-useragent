from twisted.internet.ssl import CertificateOptions, AcceptableCiphers
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

from anti_useragent.utils.cipers import generate_cipher


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
