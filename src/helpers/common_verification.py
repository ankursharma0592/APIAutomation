# HTTP Status Code

def verify_http_code(data, expected_data):
    assert data.status_code == expected_data, "Expected HTTP Satus : " + expected_data


# Any key, should not be null, of empty

def verify_key(key):
    assert key != 0, "Key is non empty : " + key
    assert key > 0, "Key should be greater than zero : " + key
