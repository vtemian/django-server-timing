import time

from django.conf.urls import url
from django.http import HttpResponse

from server_timing.middleware import TimedService, timed, timed_wrapper


@timed_wrapper('index', 'Index View')
def index(request):
    home_service = TimedService('first', 'First service')
    home_service.start()

    time.sleep(0.003)

    home_service.end()

    with timed('second', 'Second service'):
        time.sleep(0.005)

    return HttpResponse('This page shows a list of most recent posts.')


urlpatterns = [
    url('', index)
]
