import tweepy

from flask import Flask, request, jsonify

from config import current_config

app = Flask(__name__)


auth = tweepy.OAuth1UserHandler(
    current_config.API_KEY,
    current_config.API_KEY_SECRET,
    current_config.ACCESS_TOKEN,
    current_config.ACCESS_TOKEN_SECRET
)

twitter_api = tweepy.API(auth)


@app.route('/webhook/twitter', methods=['POST'])
def twitter_webhook():
    data = request.json

    if 'tweet_create_events' not in data:
        print(f"Incomplete data: {data}")

    for event in data['tweet_create_events']:
        user_mentions = event['entities']['user_mentions']
        for mention in user_mentions:
            if mention['screen_name'] == twitter_api.me().screen_name:
                print(f"Someone mention you: {event['text']}")

    return jsonify(status="ok")


@app.route('/webhook/register', methods=['POST'])
def register_webhook():
    try:
        webhook_url = current_config.WEBHOOK_URL
        endpoint = f"account_activity/all/{current_config.WEBHOOK_ENV}/webhooks.json"

        response = twitter_api.request(
            method="POST",
            endpoint=endpoint,
            params={'url': webhook_url}
        )

        if response.status_code != 200:
            return jsonify(
                message="Failed to register webhook",
            ), response.status_code

        return jsonify(message="Webhook registered successfully!")

    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/status', methods=['GET'])
def status():
    return jsonify(message="Service is running")


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80
    )
