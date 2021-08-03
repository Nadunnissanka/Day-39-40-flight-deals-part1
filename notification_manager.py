from twilio.rest import Client

TWILIO_SID = "AC1769847cda015262b401e487fe9a8bf2"
TWILIO_AUTH_TOKEN = "ae4e3640e07695ee93f52e672cb6990e"
TWILIO_VIRTUAL_NUMBER = "+14159937741"
TWILIO_VERIFIED_NUMBER = "+94756790646"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
