import pytest
from unittest import mock
from twilio.base.exceptions import TwilioRestException

from src.api import TextApi
from src.config import account_sid, auth_token, user_phone, twilio_phone

api_sub = TextApi()

@pytest.mark.skip("Makes actual call to Twilio API")
def test_send_message():
    message = "Your order will arrive by 9pm"
    to = user_phone
    from_ = twilio_phone
    assert api_sub.send_message(to, from_, message) is not None

def test_send_order_conf():
    with mock.patch('src.api.TextApi.client.messages.create') as create_message_mock:
        message = "Order sent_test"
        expected_sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'
        create_message_mock.return_value.sid = expected_sid

        to = user_phone
        from_ = twilio_phone
        sid = api_sub.send_message(to, from_, message)

        assert create_message_mock.called is True
        assert sid == expected_sid

@mock.patch('src.api.TextApi.client.messages.create')
def test_log_error_when_cannot_send_message(create_message_mock, caplog):
    error_message = (
        "Unable to create record: The 'To' number "
        f"{user_phone} is not a valid phone number."
    )
    status = 500
    uri = '/Accounts/ACXXXXXXXXXXXXXXXXX/Messages.json'
    msg = error_message
    create_message_mock.side_effect = TwilioRestException(status, uri, msg=error_message)

    to = user_phone
    from_ = twilio_phone
    sid = api_sub.send_message(to, from_, "Wrong message")

    assert sid is None
    assert "Error:" in caplog.text
    assert error_message in caplog.text