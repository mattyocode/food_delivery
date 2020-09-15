import pytest
from unittest import mock

from src.api import send_message
from src.config import account_sid, auth_token, user_phone, twilio_phone

def test_send_message_():
    message = "Your order will arrive by 9pm"
    to = user_phone
    from_ = twilio_phone
    assert send_message(to, from_, message) is not None