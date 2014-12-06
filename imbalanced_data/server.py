# import os
# from swampdragon.swampdragon_server import run_server

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imbalanced_data.settings")

# run_server()

import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys
import django.core.handlers.wsgi
#sys.path.append('/home/lawgon/') # path to your project ( if you have it in another dir).


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'imbalanced_data.settings' # path to your settings module
    application = django.core.handlers.wsgi.WSGIHandler()
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()