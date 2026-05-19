import socket
import gamemain9

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("=" * 50)
print("ホストとして待機中...")
print("自分のIPアドレスを相手に教えてください")
import socket as s
my_ip = s.gethostbyname(s.gethostname())
print(f"自分のIP: {my_ip}")
print("=" * 50)

opponent, address = server.accept()
print(f"相手が接続しました: {address}")

gamemain9.start_game(opponent, title="対戦シューティング (ホスト)")
