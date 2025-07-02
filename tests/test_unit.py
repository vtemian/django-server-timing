import time
from unittest.mock import PropertyMock, patch

from server_timing.middleware import (
    TimedService,
    add_service,
    discard_all_services,
    get_services,
    timed,
    timed_wrapper,
)


def test_timed_service(discard):
    with patch(
        "server_timing.middleware.TimedService.duration", new_callable=PropertyMock
    ) as mock_duration:
        mock_duration.return_value = 9

        service = TimedService("dummy")
        service.start()
        time.sleep(0.009)
        service.end()

        assert get_services() == [service]
        assert service.duration == 9
        assert service.name == "dummy"


def test_timed_context_manager(discard):
    with patch(
        "server_timing.middleware.TimedService.duration", new_callable=PropertyMock
    ) as mock_duration:
        mock_duration.return_value = 8

        with timed("dummy") as service:
            time.sleep(0.008)
            assert get_services() == [service]

        assert get_services()[0].duration == 8
        assert get_services()[0].name == "dummy"


def test_timed_decorator(discard):
    with patch(
        "server_timing.middleware.TimedService.duration", new_callable=PropertyMock
    ) as mock_duration:
        mock_duration.return_value = 7

        @timed_wrapper("dummy")
        def sleepy_function():
            time.sleep(0.007)

        sleepy_function()

        assert get_services()[0].duration == 7
        assert get_services()[0].name == "dummy"


def test_discard_all_services(discard):
    service = TimedService("drummy")

    service.start()
    time.sleep(0.009)
    service.end()

    assert get_services() == [service]
    discard_all_services()
    assert get_services() == []


def test_add_service(discard):
    service = TimedService("drummy")

    add_service(service)
    assert get_services() == [service]
