#!python3
page_access_token = "EAAJIZAiUxvB8BO1bkXuVPSnhbxjZBLHBQum9vdPX7aZBCgnInZB81ydnZAzrqBWqgpCT20vKxGRqwCdaPOsLaMh7UkDpaiN1gHKlDwZCRIqDG3BRcvNOLOpDNHRxHMJGb1vzfZALBKVeW1zCxitu2bStGZBX9hFw0D83yiKY74JABitGBb4CGxnM1IILewWbFvns"

verify_token = "thisisatest"

from fbmessenger import BaseMessenger, MessengerClient


class Messenger(BaseMessenger):
    def __init__(self, page_access_token, app_secret=None):
        self.page_access_token = page_access_token
        self.app_secret = app_secret
        self.client = MessengerClient(self.page_access_token, app_secret=self.app_secret)

    def message(self, message):
        self.send({'text': 'Received: {0}'.format(message['message']['text'])}, 'RESPONSE')

    def delivery(self, message):
        pass

    def read(self, message):
        pass

    def account_linking(self, message):
        pass

    def postback(self, message):
        pass

    def optin(self, message):
        pass

import os
from flask import Flask, request

app = Flask(__name__)
app.debug = True

messenger = Messenger(os.environ.get('FB_PAGE_TOKEN'))

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if (request.args.get('hub.verify_token') == os.environ.get('FB_VERIFY_TOKEN')):
            return request.args.get('hub.challenge')
        raise ValueError('FB_VERIFY_TOKEN does not match.')
    elif request.method == 'POST':
        messenger.handle(request.get_json(force=True))
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0')

