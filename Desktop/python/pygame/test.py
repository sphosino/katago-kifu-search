import tkinter as tk
import random
import math

# ウィンドウを作成
window = tk.Tk()

# ウィンドウのタイトルを設定
window.title("当たり判定付き動く図形")

# ウィンドウのサイズを設定
window.geometry("400x300")

# Canvasウィジェットを作成
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# 最初に描画する矩形を作成
rect = canvas.create_rectangle(50, 100, 150, 200, fill="blue")

# 最初に描画する円を作成
circle = canvas.create_oval(200, 100, 250, 150, fill="red")

# 矩形の動きのための変数
dx = 5  # 水平方向の移動量
dy = 5  # 垂直方向の移動量

# 円のランダムな動きのための変数
circle_dx = random.choice([-5, 5])  # ランダムな水平方向の移動量
circle_dy = random.choice([-5, 5])  # ランダムな垂直方向の移動量

# 矩形を動かす関数
def move_rectangle(event):
    if event.keysym == 'Right':  # 右矢印キー
        canvas.move(rect, dx, 0)
    elif event.keysym == 'Left':  # 左矢印キー
        canvas.move(rect, -dx, 0)
    elif event.keysym == 'Up':  # 上矢印キー
        canvas.move(rect, 0, -dy)
    elif event.keysym == 'Down':  # 下矢印キー
        canvas.move(rect, 0, dy)

# ランダムに動く円を更新する関数
def move_random_circle():
    global circle_dx, circle_dy

    # 円をランダムに動かす
    canvas.move(circle, circle_dx, circle_dy)

    # 円の位置がウィンドウの端に達した場合、方向を反転させる
    coords = canvas.coords(circle)
    if coords[2] >= 400 or coords[0] <= 0:  # 円の右端または左端がウィンドウの端に達した
        circle_dx = random.choice([-5, 5])
    if coords[3] >= 300 or coords[1] <= 0:  # 円の下端または上端がウィンドウの端に達した
        circle_dy = random.choice([-5, 5])

    # 当たり判定をチェック
    check_collision()

    # 50ms後に再度この関数を呼び出す
    window.after(50, move_random_circle)

# 当たり判定を行う関数
def check_collision():
    # 矩形の座標取得
    rect_coords = canvas.coords(rect)  # (x1, y1, x2, y2)
    # 円の座標取得
    circle_coords = canvas.coords(circle)  # (x1, y1, x2, y2)

    # 矩形と円の当たり判定
    rect_x1, rect_y1, rect_x2, rect_y2 = rect_coords
    circle_x1, circle_y1, circle_x2, circle_y2 = circle_coords

    # 円の中心座標と半径を計算
    circle_center_x = (circle_x1 + circle_x2) / 2
    circle_center_y = (circle_y1 + circle_y2) / 2
    circle_radius = (circle_x2 - circle_x1) / 2

    # 円の中心が矩形内にあるかチェック
    if rect_x1 <= circle_center_x <= rect_x2 and rect_y1 <= circle_center_y <= rect_y2:
        print("矩形と円が当たった！")
        canvas.itemconfig(rect, fill="green")  # 当たったら矩形を緑色に変更
        canvas.itemconfig(circle, fill="yellow")  # 当たったら円を黄色に変更
    else:
        canvas.itemconfig(rect, fill="blue")  # 当たっていなければ元に戻す
        canvas.itemconfig(circle, fill="red")  # 当たっていなければ元に戻す

# キー入力を処理するためにbindメソッドを使う
window.bind('<KeyPress>', move_rectangle)

# ランダムに動く円を開始
move_random_circle()

# ウィンドウを表示
window.mainloop()
