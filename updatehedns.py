#!/usr/bin/env python

import ssl
try:
    from urllib2 import Request, urlopen
    from urllib import quote
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.parse import quote


URI = "https://dyn.dns.he.net/nic/update?hostname={hostname}&password={key}"

def run_update(hostname, key, ip):
    url = URI.format(hostname=quote(hostname), key=quote(key))
    if ip:
        url += "&myip={ip}".format(ip=ip)

    req = Request(url)
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    return urlopen(req, context=ssl_ctx).read()

def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Update dns.he.net dynamic zone')
    parser.add_argument('-K', '--key', dest='key', required=True, help='Key')
    parser.add_argument('-H', '--hostname', dest='hostname', required=True, help='Hostname')
    parser.add_argument('--ip', dest='ip', help='IP address')
    args = parser.parse_args()

    print(run_update(args.hostname, args.key, args.ip))

if __name__ == '__main__':
    main()
