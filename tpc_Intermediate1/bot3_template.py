import socket
import threading

# サーバーの設定
HOST = '127.0.0.1'
PORT = 12345

# ボットの応答辞書
"""ここに入力する"""

# クライアントソケットを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("ボットがサーバーに接続しました")

# メッセージ受信と自動応答
"""ここに入力する""" 
                # 応答を探す

thread = threading.Thread(target=receive)
thread.start()
thread.join()

client.close()