def make_shim(script):
    def main():
        import os, sys
        global __name__
        global __file__
        global __path__

        sdk_root = os.path.dirname(__file__)
        sdk_path = os.path.join(sdk_root, "google_appengine")
        if 'GAE_SDK_ROOT' not in os.environ:
            os.environ['GAE_SDK_ROOT'] = sdk_root

        # import paths fixup, just in case
        if 'PYTHONPATH' in os.environ:
            os.environ['PYTHONPATH'] += os.pathsep + sdk_path
        else:
            os.environ['PYTHONPATH'] = sdk_path
        sys.path = [sdk_path] + sys.path

        __file__ = sys.argv[0] = os.path.join(sdk_path, script)
        __name__ = "__main__"
        del os, sdk_root, sys

        execfile(__file__, globals(), globals())
    return main

remote_api_shell = make_shim('remote_api_shell.py')
dev_appserver = make_shim('dev_appserver.py')
appcfg = make_shim('appcfg.py')
