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
    if os.startswith('Darwin'):
        return 'mac'
    elif os.startswith('Windows'):
        return 'windows'
    else:
        return 'linux'


def get_arch():
    arch = platform.machine()
    if '64' in arch:
        return '64bit'
    elif '686' in arch:
        return '32bit'
    elif '386' in arch:
        return '32bit'
    else:
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
       'configlet-{}-{}.{}}')
sys.exit(fetch('-x', '--dir', 'bin', URL.format(VERSION, OS, ARCH, EXT)))
