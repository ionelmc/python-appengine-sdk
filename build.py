from os.path import join, dirname, exists
import re
import hashlib
import glob
import urllib
import shutil
import zipfile
import sys
import os


SDK_FILENAME = 'google_appengine_{}.zip'
SDK_URL = 'https://storage.googleapis.com/appengine-sdks/featured/' + SDK_FILENAME
SDK_CACHE = join(dirname(__file__), 'sdks')
SDK_CACHED_NAME = join(SDK_CACHE, SDK_FILENAME)
SDK_URL_RE = re.compile('{}".*?>(?P<checksum>[0-9a-f]{{40}})<'.format(SDK_URL.format('(?P<version>[^\'"]*?)')), re.MULTILINE | re.DOTALL)

SRC_PATH = join(dirname(__file__), 'src')
SDK_DEST = join(SRC_PATH, 'appengine_sdk')
SHIM_PATH = join(dirname(__file__), 'shim')


def open_sdk(version, checksum):
    path = SDK_CACHED_NAME.format(version)
    url = SDK_URL.format(version)

    if exists(path):
        print("Already downloaded {}".format(path))
    else:
        print("Downloading {} ...".format(url))
        urllib.urlretrieve(url, path)

    with open(path, 'rb') as fp:
        print("Checking checksum for {} ...".format(path))
        sha1sum = hashlib.sha1(fp.read()).hexdigest()
    assert sha1sum == checksum
    print("Checksum OK.")

    return open(path, 'rb')


def unpack(version, checksum):
    with open_sdk(version, checksum) as fh:
        with zipfile.ZipFile(fh) as zf:
            print("Unpacking {} to {}".format(fh, SDK_DEST))
            zf.extractall(SDK_DEST)


def get_latest():
    page = urllib.urlopen('https://cloud.google.com/appengine/downloads').read()
    match = SDK_URL_RE.search(page)
    assert match, "SDK url not found in {!r:.100}".format(page)
    print("Got latest version {}".format(match.groupdict()))
    return match.group('version'), match.group('checksum')


if __name__ == "__main__":
    if not exists(SDK_CACHE):
        os.mkdir(SDK_CACHE)

    if exists(SRC_PATH):
        shutil.rmtree(SRC_PATH)

    shutil.copytree(SHIM_PATH, SRC_PATH)

    unpack(*get_latest())

    if len(sys.argv) > 1:
        build_number = int(sys.argv[1])
    else:
        build_number = 0

    with open(join(SRC_PATH, 'appengine-sdk.build'), 'w') as fh:
        fh.write(str(build_number))
