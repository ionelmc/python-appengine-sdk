def make_shim(script):
    def main():
        import os
        global __name__
        global __file__
        global __path__

        sdk_root = os.path.join(os.path.dirname(__file__), "google_appengine")
        if 'GAE_SDK_ROOT' not in os.environ:
            os.environ['GAE_SDK_ROOT'] = sdk_root
        __file__ = os.path.join(sdk_root, script)
        __name__ = "__main__"
        del os, sdk_root

        execfile(__file__, globals(), globals())
    return main

remote_api_shell = make_shim('remote_api_shell.py')
dev_appserver = make_shim('dev_appserver.py')
appcfg = make_shim('appcfg.py')
