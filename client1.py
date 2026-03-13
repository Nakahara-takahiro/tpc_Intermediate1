import socket

# サーバーの設定
HOST = '127.0.0.1'  # 接続先(サーバーのアドレス)
PORT = 12345        # ポート番号

# クライアントソケットを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"サーバーに接続しました: {HOST}:{PORT}")

# メッセージを送信
message = "こんにちは、サーバー!"
client.send(message.encode('utf-8'))
print(f"送信: {message}")

# 返事を受信
reply = client.recv(1024).decode('utf-8')
print(f"受信: {reply}")

# 接続を閉じる
client.close()
print("通信終了")