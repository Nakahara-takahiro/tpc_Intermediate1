import tkinter as tk

root = tk.Tk()
root.title("シューティングゲーム")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# スコア表示
score = 0
score_text = canvas.create_text(50, 20, text=f"スコア: {score}", fill="white", font=("Arial", 16))

# プレイヤーの位置
player_x = 200
player_y = 350
player = canvas.create_rectangle(player_x - 15, player_y - 15, player_x + 15, player_y + 15, fill="blue")

# 敵の位置
enemy_x = 200
enemy_y = 50
enemy = canvas.create_rectangle(enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15, fill="red")

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
    bullets.append({"obj": bullet, "x": player_x, "y": player_y - 15})

# 弾を移動と当たり判定
def move_bullets():
    global score, enemy_x, enemy_y
    
    for bullet in bullets[:]:
        bullet["y"] -= 10
        canvas.coords(bullet["obj"], bullet["x"] - 5, bullet["y"] - 5, bullet["x"] + 5, bullet["y"] + 5)
        
        # 当たり判定(距離計算)
        distance = ((bullet["x"] - enemy_x) ** 2 + (bullet["y"] - enemy_y) ** 2) ** 0.5
        if distance < 20:
            # ヒット!
            score += 10
            canvas.itemconfig(score_text, text=f"スコア: {score}")
            canvas.delete(bullet["obj"])
            bullets.remove(bullet)
            
            # 敵を別の場所に移動
            import random
            enemy_x = random.randint(50, 350)
            enemy_y = random.randint(50, 150)
            canvas.coords(enemy, enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15)
            continue
        
        # 画面外に出たら削除
        if bullet["y"] < 0:
            canvas.delete(bullet["obj"])
            bullets.remove(bullet)
    
    root.after(50, move_bullets)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", shoot)

move_bullets()
root.mainloop()