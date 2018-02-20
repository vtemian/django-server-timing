def test_header_basic_header(client):
    response = client.get('/')

    assert response.has_header('Server-Timing')
    assert response._headers['server-timing'] == (
        'Server-Timing',
        'index;desc="Index View";dur=8,first;desc="First '
        'service";dur=3,second;desc="Second service";dur=5'
    )
