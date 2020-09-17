import logging
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from src.config import account_sid, auth_token

class TextApi:

    client = Client(account_sid, auth_token)

    def send_message(self, to, from_, message):
        try:
            sent_message = self.client.messages.create(
                to=to,
                from_=from_,
                body=message
            )
        except TwilioRestException as e:
            logging.error(f'Error: {e}')
            return
        return sent_message.sid

