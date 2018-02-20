import time

from server_timing.middleware import (TimedService, timed, timed_wrapper,
                                      get_services, add_service,
                                      discard_all_services)


def test_timed_service(discard):
    service = TimedService('dummy')

    service.start()
    time.sleep(0.009)
    service.end()

    assert get_services() == [service]
    assert service.duration == 9
    assert service.name == 'dummy'


def test_timed_context_manager(discard):
    with timed('dummy') as service:
        time.sleep(0.008)
        assert get_services() == [service]

    assert get_services()[0].duration == 8
    assert get_services()[0].name == 'dummy'


def test_timed_decorator(discard):
    @timed_wrapper('dummy')
    def sleepy_function():
        time.sleep(0.007)

    sleepy_function()

    assert get_services()[0].duration == 7
    assert get_services()[0].name == 'dummy'


def test_discard_all_services(discard):
    service = TimedService('drummy')

    service.start()
    time.sleep(0.009)
    service.end()

    assert get_services() == [service]
    discard_all_services()
    assert get_services() == []


def test_add_service(discard):
    service = TimedService('drummy')

    add_service(service)
    assert get_services() == [service]
