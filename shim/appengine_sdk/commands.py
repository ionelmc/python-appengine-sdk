def make_shim(script):
    def main():
        from os.path import join, dirname
        global __name__
        global __file__

        __file__ = join(dirname(__file__), "google_appengine", script)
        __name__ = "__main__"

        execfile(__file__, globals(), globals())
    return main

remote_api_shell = make_shim('remote_api_shell.py')
dev_appserver = make_shim('dev_appserver.py')
appcfg = make_shim('appcfg.py')
