import socket
import gamemain9

opponent_ip = input("相手(ホスト)のIPアドレスを入力: ")
PORT = 12345

opponent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
opponent.connect((opponent_ip, PORT))
print(f"{opponent_ip} に接続しました!")

gamemain9.start_game(opponent, title="対戦シューティング (クライアント)")
