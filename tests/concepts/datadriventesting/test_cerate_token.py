import pytest
import requests


def test_post_create_token():
    pyload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=pyload)
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])
    return response.json()["token"]   
