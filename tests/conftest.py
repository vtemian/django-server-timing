import pytest

from server_timing.middleware import discard_all_services


@pytest.fixture
def discard():
    discard_all_services()
