import socket

# サーバーの設定
HOST = '127.0.0.1'  # ローカルホスト
PORT = 12345        # ポート番号

# サーバーソケットを作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"サーバー起動中... {HOST}:{PORT}")
print("クライアントの接続を待っています...")

# クライアントの接続を待つ
client, address = server.accept()
print(f"接続されました: {address}")

# メッセージを受信
message = client.recv(1024).decode('utf-8')
print(f"受信: {message}")

# メッセージを送信
reply = "メッセージを受け取りました!"
client.send(reply.encode('utf-8'))

# 接続を閉じる
client.close()
server.close()
print("通信終了")