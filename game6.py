import tkinter as tk

root = tk.Tk()
root.title("シューティングゲーム")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# プレイヤーの位置
player_x = 200
player_y = 350
player = canvas.create_rectangle(player_x - 15, player_y - 15, player_x + 15, player_y + 15, fill="blue")

# 弾のリスト
bullets = []

# プレイヤー移動
def move_left(event):
    global player_x
    player_x -= 10
    if player_x < 15:
        player_x = 15
    canvas.coords(player, player_x - 15, player_y - 15, player_x + 15, player_y + 15)

def move_right(event):
    global player_x
    player_x += 10
    if player_x > 385:
        player_x = 385
    canvas.coords(player, player_x - 15, player_y - 15, player_x + 15, player_y + 15)

# 弾を発射
def shoot(event):
    bullet = canvas.create_oval(player_x - 5, player_y - 20, player_x + 5, player_y - 10, fill="yellow")
    bullets.append({"obj": bullet, "y": player_y - 15})

# 弾を移動
def move_bullets():
    for bullet in bullets[:]:
        bullet["y"] -= 10
        canvas.coords(bullet["obj"], player_x - 5, bullet["y"] - 5, player_x + 5, bullet["y"] + 5)
        
        # 画面外に出たら削除
        if bullet["y"] < 0:
            canvas.delete(bullet["obj"])
            bullets.remove(bullet)
    
    root.after(50, move_bullets)

# キーボードイベント
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", shoot)

# 弾の移動を開始
move_bullets()

root.mainloop()