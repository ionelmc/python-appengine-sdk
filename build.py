import stat
import re
import hashlib
import os
import glob
import urllib
import shutil
import zipfile

SDK_FILENAME = 'google_appengine_{}.zip'
SDK_URL = 'https://storage.googleapis.com/appengine-sdks/featured/' + SDK_FILENAME
SDK_CACHE = os.path.join(os.path.dirname(__file__), 'sdks')
SDK_CACHED_NAME = os.path.join(SDK_CACHE, SDK_FILENAME)
SDK_DEST = os.path.join(os.path.dirname(__file__), 'src')
SDK_DEST_PKG = os.path.join(SDK_DEST, 'google_appengine')
FIXUPS = os.path.join(os.path.dirname(__file__), 'fixups', '*')
SDK_URL_RE = re.compile('{}".*?>(?P<checksum>[0-9a-f]{{40}})<'.format(SDK_URL.format('(?P<version>[^\'"]*?)')), re.MULTILINE | re.DOTALL)


def open_sdk(version, checksum):
    path = SDK_CACHED_NAME.format(version)
    url = SDK_URL.format(version)

    if os.path.exists(path):
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
            print("Cleaning up {} ...".format(SDK_DEST))
            shutil.rmtree(SDK_DEST)
            print("Unpacking {} to {}".format(fh, SDK_DEST))
            zf.extractall(SDK_DEST)


def get_latest():
    page = urllib.urlopen('https://cloud.google.com/appengine/downloads').read()
    match = SDK_URL_RE.search(page)
    assert match, "SDK url not found in {!r:.100}".format(page)
    print("Got latest version {}".format(match.groupdict()))
    return match.group('version'), match.group('checksum')


if __name__ == "__main__":
    unpack(*get_latest())
    for path in glob.glob(FIXUPS):
        shutil.copy(path, SDK_DEST_PKG)
