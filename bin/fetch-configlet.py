#!/usr/bin/env python
import platform
import re
import sys
from fetch import fetch

LATEST = 'https://github.com/exercism/configlet/releases/latest'

try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen


def get_os():
    os = platform.system()
    mappings = {
        'Darwin': 'mac',
        'Windows': 'windows'
    }
    for k, v in mappings.items():
        if os.startswith(k):
            return v
    return 'linux'


def get_arch():
    arch = platform.machine()
    mappings = {
        '64': '64bit',
        '686': '32bit',
        '386': '32bit',
        'armv5': 'arm-v5',
        'armv6': 'arm-v6',
        'armv7': 'arm-v6'
    }
    for k, v in mappings.items():
        if k in arch:
            return v
    return '64bit'


OS = get_os()
ARCH = get_arch()

url = urlopen(LATEST).geturl()
VERSION = re.search('tag/(v\d+\.\d+\.\d+)$', url).group(1)
if OS == 'windows':
    EXT = 'zip'
else:
    EXT = 'tgz'
URL = ('https://github.com/exercism/configlet/releases/download/{}/'
       'configlet-{}-{}.{}')
sys.exit(fetch('-x', '--dir', 'bin', URL.format(VERSION, OS, ARCH, EXT)))
