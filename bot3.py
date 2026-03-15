import socket
import threading

# サーバーの設定
HOST = '127.0.0.1'
PORT = 12345

# ボットの応答辞書
responses = {
    "こんにちは": "こんにちは!今日はいい天気ですね!",
    "元気": "元気ですよ!ありがとう!",
    "天気": "今日は晴れみたいですよ!",
    "ゲーム": "ゲーム楽しいですよね!何が好きですか?",
    "好き": "私も好きです!",
    "ありがとう": "どういたしまして!",
    "bye": "またね!バイバイ!"
}

# クライアントソケットを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("ボットがサーバーに接続しました")

# メッセージ受信と自動応答
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"受信: {message}")
                
                # 応答を探す
                reply = "そうなんですね!"  # デフォルト応答
                for key in responses:
                    if key in message:
                        reply = responses[key]
                        break
                
                print(f"送信: {reply}")
                client.send(reply.encode('utf-8'))
                
                if message == "bye":
                    break
        except:
            break

thread = threading.Thread(target=receive)
thread.start()
thread.join()

client.close()