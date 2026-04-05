import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("シューティングゲーム")

# キャンバスの作成
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# プレイヤーの初期位置
player_x = 200
player_y = 350

# プレイヤーを描画
player = canvas.create_rectangle(
    player_x - 15, player_y - 15,
    player_x + 15, player_y + 15,
    fill="blue"
)

# キー入力で移動
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

def move_up(event):
    global player_y
    player_y -= 10
    if player_y < 15:
        player_y = 15
    canvas.coords(player, player_x - 15, player_y - 15, player_x + 15, player_y + 15)

def move_down(event):
    global player_y
    player_y += 10
    if player_y > 385:
        player_y = 385
    canvas.coords(player, player_x - 15, player_y - 15, player_x + 15, player_y + 15)

# キーボードイベント
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

# メインループ
root.mainloop()