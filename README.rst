===================================================
Un-official `pip install`-able AppEngine SDK
===================================================

| |version| |downloads| |wheel|

.. |version| image:: http://img.shields.io/pypi/v/appengine-sdk.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/appengine-sdk

.. |downloads| image:: http://img.shields.io/pypi/dm/appengine-sdk.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/appengine-sdk

.. |wheel| image:: https://pypip.in/wheel/appengine-sdk/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/appengine-sdk

It provides working bins for ``appcfg``, ``dev_appserver`` and ``remote_api_shell``. And they work on Windows!

Usage::

    pip install appengine-sdk

You can always `waste your time manually copying files <https://cloud.google.com/appengine/downloads>`_
if you don't like this un-official package.

-----

Packager instructions
=====================

.. note::

    You need to ``git clone git@github.com:ionelmc/python-appengine-sdk.git`` to do these.

To rebuild this package (in case I'm too slow or you want to build it yourself)::

    tox -e build

If something is broken and a rebuild is required, to make a new `post release`::

    tox -e build -- 1

..

    The default `post release` number is ``0``.

To upload it to PyPI::

    tox -e upload -- dist/appengine_sdk-<VERSION>-py2-none-any.whl

