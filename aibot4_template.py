import socket
import threading
from openai import OpenAI

# OpenAI APIの設定
# ※事前に pip install openai が必要
# ※APIキーは https://platform.openai.com/api-keys から取得
API_KEY = "ここにAPIキーを入力"  # 各自で取得したキーを入れる
openai_client = OpenAI(api_key=API_KEY)

# サーバーの設定
HOST = '127.0.0.1'
PORT = 12345

# クライアントソケットを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("AIボットがサーバーに接続しました")

# AIに性格設定をする
personality = "あなたは明るくて優しい友達です。短く答えてください。"

# メッセージ受信とAI応答
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"受信: {message}")
                
                # AIに質問
                try:
                    response = openai_client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": personality},
                            {"role": "user", "content": message}
                        ]
                    )
                    reply = response.choices[0].message.content
                except:
                    reply = "ごめん、ちょっと考え中..."
                
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