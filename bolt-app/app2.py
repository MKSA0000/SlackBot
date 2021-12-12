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

@app.message('add me a reaction!')
def message_reaction(message,say):
    print(message)
    channelid = message['channel']
    ts = message['ts']
    app.client.reactions_add(channel=channelid,name='eyes',timestamp=ts)
    say('We`ve added eyes rreaction for you')

@app.event("reaction_added")
def handle_reaction_added_events(body, logger):
    channelid = body['event']['item']['channel']
    ts = body['event']['item']['ts']
    app.client.reactions_add(channel=channelid,name='eyes',timestamp=ts)

# アプリを起動します
if __name__ == "__main__":
    print('app start')
    app.start(port=3000)