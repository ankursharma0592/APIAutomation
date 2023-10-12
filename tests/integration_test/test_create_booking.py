import allure
import pytest
import requests

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *


class TestIntegration(object):

    @pytest.mark.smoke
    @allure.feature('TC#1 - Verify Create Booking Feature')
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(booking_id)

# URL = Separate URL
# Payload = Separate Payload Manager
# Headers = Headers Utils
# Verify = Separate Verify
    @pytest.mark.smoke
    @allure.feature('TC#2 - Verify Update Booking Feature')
    def test_update_put(self):
        assert True

    @pytest.mark.smoke
    @allure.feature('TC#3 - Verify Delete Booking Feature')
    def test_delete_(self):
        assert True
