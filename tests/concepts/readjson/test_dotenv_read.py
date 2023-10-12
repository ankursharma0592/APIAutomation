import os
import pytest
from dotenv import load_dotenv
import requests


@pytest.fixture
def test_post_create_booking():
    pyload_create_booking = {
        "firstname": "Ankur",
        "lastname": "Sharma",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2023-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers,
                             json=pyload_create_booking)
    print(response.json())
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print(response.headers)
    assert response.status_code == 200
    return booking_id


def test_put_req(test_post_create_booking):
    pyload_update_booking = {
        "firstname": "Amit",
        "lastname": "Thakur",
        "totalprice": 11111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    load_dotenv()
    temp_token = "token=" + os.getenv("token")
    print(temp_token)
    print(os.getenv("user_name"))
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
    response = requests.put(url_put, headers=headers,
                            json=pyload_update_booking)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200
