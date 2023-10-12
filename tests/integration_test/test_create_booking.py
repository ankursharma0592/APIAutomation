import pytest
import requests

from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *


class TestIntegration(object):

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

    # def test_create_booking_tc2(self):
    #     assert True == False
    #
    # def test_create_booking_tc3(self):
    #     assert True == True
