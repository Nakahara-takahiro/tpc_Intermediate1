import socket
import threading
import google.generativeai as genai

# Gemini APIの設定(無料枠)
# ※事前に pip install google-generativeai が必要
# ※APIキーは https://makersuite.google.com/app/apikey から取得
API_KEY = "ここにAPIキーを入力"  # 各自で取得したキーを入れる
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

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
                    prompt = f"{personality}\n質問: {message}"
                    response = model.generate_content(prompt)
                    reply = response.text
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