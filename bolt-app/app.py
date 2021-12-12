"""
https://slack.dev/bolt-python/ja-jp/tutorial/getting-started
"""
import os,json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

credentials = json.loads(open('credentials.json').read())
SLACK_BOT_TOKEN = credentials['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = credentials['SLACK_APP_TOKEN']
SLACK_SIGNING_SECRET= credentials['SLACK_SIGNING_SECRET']

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(signing_secret=SLACK_SIGNING_SECRET,token=SLACK_BOT_TOKEN)

@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")

# アプリを起動します
if __name__ == "__main__":
    print('app start')
    app.start(port=3000)