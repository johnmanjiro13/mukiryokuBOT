import os
import requests


class SendSlack():

    def __init__(self, channel_id):
        self.channel_id = channel_id
    
    def post_slack_message(self, message, user_name, emoji=':ghost:'):
        post_data = {
            'channel': self.channel_id,
            'text': message,
            'username': user_name,
            'icon_emoji': emoji,
            'as_user': False
        }
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        url = os.getenv("SLACK_MUKIRYOKU_ENDPOINT")
        requests.post(url, headers=headers, data=post_data)
