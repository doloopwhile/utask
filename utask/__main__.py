#!/usr/bin/env python
#encoding: utf-8
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def main():
    config = Configurator()
    config.add_route('projects', '/projects')
    config.add_route('tasks', '/tasks')
    config.add_route('timelines', '/timelines')
    config.scan('utask')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

if __name__ == '__main__':
    main()
