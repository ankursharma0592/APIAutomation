from src.constants.apiconstants import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *


class TestIntegration(object):

    def test_verify_creating_booking_by_updating_deleting(self):
        pass


# Create a booking, update the booking name, get the booking by id and verify
# Create bo  oking_by_updating_deleting
# Try to update on a deleted id - 404
# Get an Existing Booking from get All Bookings Ids, update a booking and verify using GET by id
# Create Booking enter a wrong payload or wring JSON
