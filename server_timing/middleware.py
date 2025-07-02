import threading
import time
from contextlib import contextmanager

import django
from django.utils.deprecation import MiddlewareMixin

_thread_local = threading.local()


def get_services():
    return _thread_local.__dict__.setdefault("services", [])


def discard_all_services():
    _thread_local.__dict__["services"] = []


def add_service(service):
    get_services().append(service)


class TimedService:
    def __init__(self, name, description="", duration=None):
        self.name = name
        self.description = description
        self._duration = duration
        self._start = self._end = None

        if self._duration:
            add_service(self)

    def start(self):
        self._start = time.time()
        add_service(self)

    def end(self):
        self._end = time.time()

    @property
    def duration(self):
        if not self._start and self._duration:
            return self._duration
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
            service.name
            + ';desc="'
            + service.description
            + '";dur='
            + str(service.duration)
            for service in get_services()
        ]
        if services:
            if django.VERSION >= (3, 2):
                response.headers["Server-Timing"] = ",".join(services)
            else:
                response._headers["Server-Timing"] = ",".join(services)
            discard_all_services()
        return response
