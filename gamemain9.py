import tkinter as tk
import threading

def start_game(opponent, title="対戦シューティング"):
    root = tk.Tk()
    root.title(title)

    canvas = tk.Canvas(root, width=400, height=400, bg="black")
    canvas.pack()

    my_hp = 100
    enemy_hp = 100
    hp_text = canvas.create_text(200, 20, text=f"自分:{my_hp} 相手:{enemy_hp}", fill="white", font=("Arial", 14))

    my_x = 200
    my_y = 350
    my_player = canvas.create_rectangle(my_x - 15, my_y - 15, my_x + 15, my_y + 15, fill="blue")

    enemy_x = 200
    enemy_y = 50
    enemy_player = canvas.create_rectangle(enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15, fill="red")

    bullets = []
    game_over = False
    keys_pressed = {"Left": False, "Right": False}

    def key_press(event):
        if event.keysym in keys_pressed:
            keys_pressed[event.keysym] = True

    def key_release(event):
        if event.keysym in keys_pressed:
            keys_pressed[event.keysym] = False

    def receive():
        nonlocal enemy_x, enemy_y, my_hp, game_over
        while True:
            try:
                message = opponent.recv(1024).decode('utf-8')
                if message:
                    data = message.split("|")
                    if data[0] == "POS":
                        enemy_x = 400 - int(data[1])
                        enemy_y = 400 - int(data[2])  # 上下反転して相手視点に合わせる
                        canvas.coords(enemy_player, enemy_x - 15, enemy_y - 15, enemy_x + 15, enemy_y + 15)
                    elif data[0] == "HIT":
                        my_hp -= 10
                        canvas.itemconfig(hp_text, text=f"自分:{my_hp} 相手:{enemy_hp}")
                        if my_hp <= 0 and not game_over:
                            game_over = True
                            canvas.create_text(200, 200, text="負けました!", fill="red", font=("Arial", 30))
            except:
                break

    thread = threading.Thread(target=receive)
    thread.daemon = True
    thread.start()

    def shoot(event):
        if game_over:
            return
        bullet = canvas.create_oval(my_x - 5, my_y - 20, my_x + 5, my_y - 10, fill="yellow")
        bullets.append({"obj": bullet, "x": my_x, "y": my_y - 15})

    def update():
        nonlocal my_x, enemy_hp, game_over

        if not game_over:
            if keys_pressed["Left"]:
                my_x -= 5
                if my_x < 15:
                    my_x = 15
            if keys_pressed["Right"]:
                my_x += 5
                if my_x > 385:
                    my_x = 385

            canvas.coords(my_player, my_x - 15, my_y - 15, my_x + 15, my_y + 15)

            try:
                opponent.send(f"POS|{my_x}|{my_y}".encode('utf-8'))
            except:
                pass

            for bullet in bullets[:]:
                bullet["y"] -= 10
                canvas.coords(bullet["obj"], bullet["x"] - 5, bullet["y"] - 5, bullet["x"] + 5, bullet["y"] + 5)

                distance = ((bullet["x"] - enemy_x) ** 2 + (bullet["y"] - enemy_y) ** 2) ** 0.5
                if distance < 20:
                    enemy_hp -= 10
                    canvas.itemconfig(hp_text, text=f"自分:{my_hp} 相手:{enemy_hp}")
                    try:
                        opponent.send("HIT|0|0".encode('utf-8'))
                    except:
                        pass
                    canvas.delete(bullet["obj"])
                    bullets.remove(bullet)
                    if enemy_hp <= 0 and not game_over:
                        game_over = True
                        canvas.create_text(200, 200, text="勝ちました!", fill="green", font=("Arial", 30))
                    continue

                if bullet["y"] < 0:
                    canvas.delete(bullet["obj"])
                    bullets.remove(bullet)

        root.after(50, update)

    root.bind("<KeyPress>", key_press)
    root.bind("<KeyRelease>", key_release)
    root.bind("<space>", shoot)

    update()
    root.mainloop()
