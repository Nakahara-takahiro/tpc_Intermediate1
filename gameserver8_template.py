import tkinter as tk
import socket
import threading

"""
資料を見て追加する
"""

root = tk.Tk()
root.title("対戦シューティング")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# 自分のプレイヤー
my_x = 200
my_y = 350
my_player = canvas.create_rectangle(my_x - 15, my_y - 15, my_x + 15, my_y + 15, fill="blue")

# 相手のプレイヤー
enemy_x = 200
enemy_y = 50
enemy_player = canvas.create_rectangle(enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15, fill="red")

# キー押下状態を記録
keys_pressed = {"Left": False, "Right": False, "Up": False, "Down": False}

# キーが押された時
def key_press(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True

# キーが離された時
def key_release(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False

# 位置情報を受信
def receive():
    global enemy_x, enemy_y
    while True:
        try:
            message = opponent.recv(1024).decode('utf-8')
            if message:
                x, y = message.split(",")
                """
                資料を見て追加する
                """
        except:
            break

# 受信スレッド開始
thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()

# 定期的に位置を更新・送信
def update_position():
    global my_x, my_y
    
    # キー状態に応じて移動
    if keys_pressed["Left"]:
        my_x -= 5
        if my_x < 15:
            my_x = 15
    if keys_pressed["Right"]:
        my_x += 5
        if my_x > 385:
            my_x = 385
    if keys_pressed["Up"]:
        my_y -= 5
        if my_y < 15:
            my_y = 15
    if keys_pressed["Down"]:
        my_y += 5
        if my_y > 385:
            my_y = 385
    
    # 画面更新
    canvas.coords(my_player, my_x - 15, my_y - 15, my_x + 15, my_y + 15)
    canvas.coords(enemy_player, enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15)
    
    # 位置を送信(定期的に)
    try:
        """
        資料を見て追加する
        """
    except:
        pass
    
    # 50msごとに実行
    root.after(50, update_position)

# キーイベント
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# 位置更新開始
update_position()

root.mainloop()