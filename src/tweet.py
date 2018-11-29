import os
import random
import oauth
import tweepy
from tweepy.error import TweepError
from send_slack import SendSlack


SPEECH_PATH = "speeches/speeches.txt"

def post_speech():
    api = oauth.create_twitter_api()
    try:
        speech = get_speech()
        api.update_status(speech)
    except TweepError as e:
        message = "<!channel> mukiryokuBOT raised Error\n" + e.reason
        service = SendSlack(channel_id=os.getenv('SLACK_MUKIRYOKU_CHANNEL'))
        service.post_slack_message(message, 'mukiryokuBOT')


def get_speech():
    with open(SPEECH_PATH, 'r') as file_object:
        line = next(file_object)
        for num, aline in enumerate(file_object, 2):
            if random.randrange(num): continue
            line = aline
        return line


if __name__ == '__main__':
    post_speech()
