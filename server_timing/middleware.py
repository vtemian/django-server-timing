import time
import threading
from contextlib import contextmanager

from django.utils.deprecation import MiddlewareMixin


_thread_local = threading.local()


def get_services():
    return _thread_local.__dict__.setdefault("services", [])


def discard_all_services():
    _thread_local.__dict__["services"] = []


def add_service(service):
    get_services().append(service)


class TimedService(object):
    def __init__(self, name, description=''):
        self.name = name
        self.description = description
        self._start = self._end = None

    def start(self):
        self._start = time.time()
        add_service(self)

    def end(self):
        self._end = time.time()

    @property
    def duration(self):
        return int(((self._end or time.time()) - self._start) * 1000)


@contextmanager
def timed(name, description=""):
    service = TimedService(name, description)
    service.start()
    yield service
    service.end()


def timed_wrapper(name, description=""):
    def wrapper(function):
        def func(*args, **kwargs):
            service = TimedService(name, description)
            service.start()

            result = function(*args, **kwargs)

            service.end()

            return result
        return func
    return wrapper


class ServerTiming(MiddlewareMixin):
    def process_response(self, request, response):
        services = [
            service.name + ';desc="' + service.description + '";dur=' + str(service.duration)
            for service in get_services()
        ]
        if services:
            response._headers['server-timing'] = ('Server-Timing', ','.join(services))
            discard_all_services()
        return response
