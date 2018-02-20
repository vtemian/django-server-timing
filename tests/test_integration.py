def test_header_complex_header(client):
    response = client.get('/complex')

    assert response.has_header('Server-Timing')
    assert response._headers['server-timing'] == (
        'Server-Timing',
        'index;desc="Index View";dur=8,first;desc="First '
        'service";dur=3,second;desc="Second service";dur=5'
    )


def test_header_no_header(client):
    response = client.get('/no-header')
    assert not response.has_header('Server-Timing')
