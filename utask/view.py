from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='timelines')
def timelines(request):
      return Response('OK')

@view_config(route_name='tasks')
def tasks(request):
      return Response('OK')

@view_config(route_name='projects')
def projects(request):
      return Response('OK')
