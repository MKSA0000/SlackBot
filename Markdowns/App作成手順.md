# Slack Boltを使って簡単なアプリを作ろう

## 手順

### Slack Webpageでの操作

1. 基本的にはこの手順に沿って操作するだけです．
2. <https://api.slack.com/apps> にアクセスして，緑色の「Create New App」をクリック．From Scratchで作成します．適当な名前をつけて，workspaceを選択肢，Create App
3. Bot編集のページで **Revert to Old Design** を選択してください．API tokenを探すのに時間がかかります．
4. OAuth & Permissionsをサイドバーから探して押す．Scopesの欄を見つけたら，Bot Token Scopes/ User Token Scopesに必要な権限を付与する
5. 考えるのが面倒であれば，次を入れておけば良い
   * Bot Token Scopes: app_mentions:read, channels:history, channels:read, chat:write
      * channels:writeではなくchat:writeであるので注意
   * User Token Scopes: users:read, users:write
6. 同じくOauth & Permissionのページ**Install to Workspace**を実行する
7. この段階でローカルの方のslackを見てみると，Botが増えています．
8. <span style="color: red; ">Bot User Oauth Token</span>が出てくるのでコピーしてください(もう一方のUser hogehogeは使わない)
9. サイドバーBasic Informationをクリックして，App Credentialsの<span style="color: red;"> SIgning Secret </span>をコピーする．
10. 同じくBasic Informationページ内でApp-Level Tokensがあり，"Generate Token and Scopes"でアプリレベルのトークンを発行してください．与える権限はconnections:write, authorization:readの2つです．
11. トークンが発行されるので<span style="color: red;"> Token (xapp-1-hogehoge) </span>をコピーする．
12. 以上 Bot User Oauth Token, Signing Secret, App-Level Tokenの3つをどこかに保管しておいてください

### Slackワークスペース上での操作

Botを実際に機能させるためには **「チャンネルに追加」** する必要があります．(セキュリティの観点から，大抵のbotは追加されたチャンネルのメッセージしか監視できません)

Botに監視させたいチャンネルに移動して「インテグレーション」欄のアプリを追加する，で追加できる

### Python Slack boltでのpyファイル作成

1. 適当な作業ディレクトリを作成し，app.pyという名前のファイルを作ってください

   ```python
    import os
    from slack_bolt import App
    from slack_bolt.adapter.socket_mode import SocketModeHandler

    SLACK_BOT_TOKEN = "xoxb-(から始まるトークン)"
    SLACK_APP_TOKEN = "xapp-(から始まるトークン．3つの中で一番文字数が多い)"
    SLACK_SIGNING_SECRET="(英数字の羅列xoxbなどがつかない)"
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
   ```
   
2. 上記コードをapp.pyに貼り付けてください

### 実行

1. app.pyを

    ```shell
    python app.py
    ```

2. Ngrokで

   ```shell
   ngrok http 3000
   ```

   を実行する
3. Ngrok.exeの画面に

   ```shell
   https://xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx/ngrok.io -> http://localhost:3000
   ```

   が出てきたら<span style="color: red;">https</span>の方のリンクをコピーしてください．
4. 先程のSlack Webpageで自分の作成したBotをクリックし，サイドバーから**Event subscription** を探してクリックします．
5. Enable Eventsのスイッチを入れ，**Request URL**に先程のhttps:xxxx.ngrok.ioを代入します．<span style="color: red;"> ここでURLの最後が ngrok.io/slack/events となるように文字を付け加えること </span>
6. URLがverifyされたら下の方のsubscribe to bot eventsで自分がNotifyされたいUser Events(メッセージの投稿だったりスタンプだったり)を登録します
   * <span style="color: red;">message.channels</span>が今回のbotでは必須です．
7. Save Changesでうまく行けば成功です．
8. 完成．(本Tutorialでは messageについてregrexで "hello"という文字列を検索し，ヒットした場合にメッセージを投稿した人の名前を返しています)