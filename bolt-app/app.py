"""
https://slack.dev/bolt-python/ja-jp/tutorial/getting-started
"""
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = "xoxb-(トークンを貼る)"
SLACK_APP_TOKEN = "xapp-(トークンを貼る)"
SLACK_SIGNING_SECRET="(トークンを貼る)"
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