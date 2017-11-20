#!/usr/bin/env python
from __future__ import print_function
import os
import sys

PLATFORM = os.name
if PLATFORM == 'nt':
    import zipfile

    def extractall(archive):
        with zipfile.ZipFile(archive, 'r') as zip:
            zip.extractall()
else:
    import tarfile

    def extractall(archive):
        with tarfile.open(archive, mode='r:gz') as tar:
            tar.extractall()

try:
    # Python 3
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    # Python 2
    from urllib2 import urlopen, HTTPError


def fetch(*args):
    args = list(args)
    try:
        is_tar = False
        while args[0].startswith('-'):
            if args[0] == '-x':
                is_tar = True
                args.pop(0)
            elif args[0] == '--dir':
                args.pop(0)
                os.chdir(args.pop(0))
        URL = args[0]
        dest = os.path.basename(URL)
        file_contents = urlopen(URL).read()
        if is_tar:
            with open(dest, "wb") as f:
                f.write(file_contents)
            try:
                extractall(dest)
            finally:
                os.remove(dest)
        else:
            with open(dest, "wb") as f:
                f.write(file_contents)
        return 0
    except IndexError:
        print("usage: fetch.py [--tar] [--dir <destination directory>] <url>")
    except ValueError as e:
        print(str(e))
    except HTTPError as e:
        print(str(e))
    return 1


if __name__ == '__main__':
    sys.exit(fetch(sys.argv[1:]))
