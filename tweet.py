import os
import oauth
import tweepy
from tweepy.error import TweepError
from send_slack import SendSlack


def post_speech():
    api = oauth.create_twitter_api()
    try:
        api.update_status("……好きな人の傍いると、辺りに雪を降らせてしまう。そんな女の子がいるそうです（伊勢崎多奈/演劇少女は古都鎌倉を雪で潰す）")
    except TweepError as e:
        service = SendSlack(channel_id=os.getenv("SLACK_MUKIRYOKU_CHANNEL"))
        message = "<!here> mukiryokuBOT raised Error\n" + e.reason
        service.post_slack_message(message, 'mukiryokuBOT')

if __name__ == '__main__':
    post_speech()
