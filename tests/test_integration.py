from unittest import skipUnless
from unittest.mock import PropertyMock, patch

import django


@skipUnless(
    django.VERSION[0] == 3 and django.VERSION[1] >= 2,
    "response.headers not included until Django 3.2",
)
def test_header_complex_header_django_32(client):
    with patch(
        "server_timing.middleware.TimedService.duration", new_callable=PropertyMock
    ) as mock_duration:
        mock_duration.return_value = 10
        response = client.get("/complex")

    assert response.has_header("Server-Timing")
    res = response.headers["server-timing"]
    target = (
        'index;desc="Index View";dur=10,first;'
        'desc="First service";dur=10,second;desc="Second service";dur=10'
    )
    assert res == target


def test_header_no_header(client):
    response = client.get("/no-header")
    assert not response.has_header("Server-Timing")
