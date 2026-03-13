import socket
import threading

# サーバーの設定
HOST = '127.0.0.1'
PORT = 12345

# クライアントソケットを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f"サーバーに接続しました")

# メッセージ受信用の関数
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"サーバー: {message}")
        except:
            break

# 受信を別スレッドで実行
thread = threading.Thread(target=receive)
thread.start()

# メッセージ送信
while True:
    message = input()
    client.send(message.encode('utf-8'))
    if message == "bye":
        break

client.close()