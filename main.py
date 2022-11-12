import numpy as np

import tkinter.messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from functools import partial

# グローバル変数
ini_x = 0.0
ini_y = 45.0
ini_angle = 0.0
fin_angle = 90.0



def DrawCanvas(canvas, ax):
    # 縦線           x軸(点1x , 点2x           y軸
    ax.plot(np.array([-45.0, -45.0]), np.array([0.0, 180.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([0.0, 0.0]), np.array([0.0, 180.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([45.0, 45.0]), np.array([0.0, 180.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([90.0, 90.0]), np.array([0.0, 180.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([135.0, 135.0]), np.array([0.0, 180.0]), color="gray", linestyle="dashed")

    # 横線
    ax.plot(np.array([-45.0, 135.0]), np.array([0.0, 0.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 135.0]), np.array([45.0, 45.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 135.0]), np.array([90.0, 90.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 135.0]), np.array([135.0, 135.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 135.0]), np.array([180.0, 180.0]), color="gray", linestyle="dashed")

    # 斜め線（右上）
    ax.plot(np.array([0.0, -45.0]), np.array([180.0, 135.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([90.0, -45.0]), np.array([180.0, 45.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([135.0, 0.0]), np.array([135.0, 0.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([135.0, 90.0]), np.array([45.0, 0.0]), color="gray", linestyle="dashed")

    # 斜め線（右下）
    ax.plot(np.array([90.0, 135.0]), np.array([180.0, 135.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([0.0, 135.0]), np.array([180.0, 45.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 90.0]), np.array([135.0, 0.0]), color="gray", linestyle="dashed")
    ax.plot(np.array([-45.0, 0.0]), np.array([45.0, 0.0]), color="gray", linestyle="dashed")

    # 柱(6mm x 6mm)
    ax.plot(np.array([-48, -48, -42, -42, -48]), np.array([-3, 3, 3, -3, -3]), color="red", linestyle="solid")
    ax.plot(np.array([-48, -48, -42, -42, -48]), np.array([87, 93, 93, 87, 87]), color="red", linestyle="solid")
    ax.plot(np.array([-48, -48, -42, -42, -48]), np.array([177, 183, 183, 177, 177]), color="red", linestyle="solid")
    ax.plot(np.array([42, 42, 48, 48, 42]), np.array([-3, 3, 3, -3, -3]), color="red", linestyle="solid")
    ax.plot(np.array([42, 42, 48, 48, 42]), np.array([87, 93, 93, 87, 87]), color="red", linestyle="solid")
    ax.plot(np.array([42, 42, 48, 48, 42]), np.array([177, 183, 183, 177, 177]), color="red", linestyle="solid")
    ax.plot(np.array([132, 132, 138, 138, 132]), np.array([-3, 3, 3, -3, -3]), color="red", linestyle="solid")
    ax.plot(np.array([132, 132, 138, 138, 132]), np.array([87, 93, 93, 87, 87]), color="red", linestyle="solid")
    ax.plot(np.array([132, 132, 138, 138, 132]), np.array([177, 183, 183, 177, 177]), color="red", linestyle="solid")

    canvas.draw()  # キャンバスの描画

def DrawTrace(canvas, ax):
    # speed = 300  # mm/s
    # low_AngVel = 10980  # 最大角速度(ジャイロ生値)
    # Low_AngAcl = 180  # 角加速度(ジャイロ生値)

    # ini_x = 0.0
    # ini_y = 45.0
    # ini_angle = 0.0
    # fin_angle = 90.0
    # pri_offset = 55
    # post_offset = 55

    speed = int(Set_Speed.get())
    low_AngVel = int(Set_low_AngVel.get())
    Low_AngAcl = int(Set_Low_AngAcl.get())
    pri_offset = int(Set_pri_offset.get())
    post_offset = int(Set_post_offset.get())
    K_slip_angle = float(Set_K_SP.get())
    Width = int(Set_Width.get())

    speed_ms = speed / 1000

    # 角速度[°/sec]
    AngVel = low_AngVel / 16.384
    # 角加速度[°/sec^2]
    AngAcl = Low_AngAcl / 16.384 * 1000


    ax.cla()  # 前の描画データの消去
    DrawCanvas(Canvas, ax)

    # 最初の直線
    pi = np.pi
    fin_x = ini_x + pri_offset * np.sin(np.deg2rad(ini_angle))
    fin_y = ini_y + pri_offset * np.cos(np.deg2rad(ini_angle))
    ax.plot(np.array([ini_x, fin_x]), np.array([ini_y, fin_y]), color="blue", linestyle="solid")

    ax.plot(np.array([ini_x+(Width/2)*np.cos(np.deg2rad(ini_angle)), fin_x+(Width/2)*np.cos(np.deg2rad(ini_angle))]), np.array([ini_y-(Width/2)*np.sin(np.deg2rad(ini_angle)), fin_y-(Width/2)*np.sin(np.deg2rad(ini_angle))]), color="#888888", linestyle="solid")
    ax.plot(np.array([ini_x-(Width/2)*np.cos(np.deg2rad(ini_angle)), fin_x-(Width/2)*np.cos(np.deg2rad(ini_angle))]), np.array([ini_y+(Width/2)*np.sin(np.deg2rad(ini_angle)), fin_y+(Width/2)*np.sin(np.deg2rad(ini_angle))]), color="#888888", linestyle="solid")

    now_Angle = ini_angle
    s_now_Angle = ini_angle
    now_AngVel = 0



    # 台形加速
    while now_AngVel < AngVel:
        befor_x = fin_x
        befor_y = fin_y
        now_AngVel = now_AngVel + (AngAcl / 1000)
        now_Angle = now_Angle + (now_AngVel / 1000)

        if (now_Angle - (now_AngVel * speed_ms * K_slip_angle)) < 0:
            s_now_Angle = 0
        else:
            s_now_Angle = now_Angle - (now_AngVel * speed_ms * K_slip_angle)  # 角速度と速度(≒遠心力)に比例

        fin_x = befor_x + speed_ms * np.sin(np.deg2rad(s_now_Angle))
        fin_y = befor_y + speed_ms * np.cos(np.deg2rad(s_now_Angle))

        ax.plot(np.array([befor_x, fin_x]), np.array([befor_y, fin_y]), color="green", linestyle="solid")
        ax.plot(np.array([befor_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")
        ax.plot(np.array([befor_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")

    now_AngVel = AngVel
    use_angle = now_Angle - ini_angle  # 台形加速にかかった角度

    # 定常円
    while now_Angle < ((ini_angle + fin_angle) - use_angle):
        befor_x = fin_x
        befor_y = fin_y
        now_Angle = now_Angle + (AngVel / 1000)

        s_now_Angle = now_Angle - (AngVel * speed_ms * K_slip_angle)
        fin_x = befor_x + speed_ms * np.sin(np.deg2rad(s_now_Angle))
        fin_y = befor_y + speed_ms * np.cos(np.deg2rad(s_now_Angle))

        ax.plot(np.array([befor_x, fin_x]), np.array([befor_y, fin_y]), color="red", linestyle="solid")
        ax.plot(np.array([befor_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")
        ax.plot(np.array([befor_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")


    # 台形減速
    while now_AngVel > 0:
        befor_x = fin_x
        befor_y = fin_y
        now_AngVel = now_AngVel - (AngAcl / 1000)
        now_Angle = now_Angle + (now_AngVel / 1000)

        s_now_Angle = now_Angle - (now_AngVel * speed_ms * K_slip_angle)
        fin_x = befor_x + speed_ms * np.sin(np.deg2rad(s_now_Angle))
        fin_y = befor_y + speed_ms * np.cos(np.deg2rad(s_now_Angle))

        ax.plot(np.array([befor_x, fin_x]), np.array([befor_y, fin_y]), color="green", linestyle="solid")
        ax.plot(np.array([befor_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x+(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y-(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")
        ax.plot(np.array([befor_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle)), fin_x-(Width/2)*np.cos(np.deg2rad(s_now_Angle))]), np.array([befor_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle)), fin_y+(Width/2)*np.sin(np.deg2rad(s_now_Angle))]), color="#888888", linestyle="solid")

    # 最後の直線
    befor_x = fin_x
    befor_y = fin_y

    fin_x = befor_x + post_offset * np.sin(np.deg2rad(ini_angle + fin_angle))
    fin_y = befor_y + post_offset * np.cos(np.deg2rad(ini_angle + fin_angle))
    ax.plot(np.array([befor_x, fin_x]), np.array([befor_y, fin_y]), color="blue", linestyle="solid")
    ax.plot(np.array([befor_x+(Width/2)*np.cos(np.deg2rad(ini_angle + fin_angle)), fin_x+(Width/2)*np.cos(np.deg2rad(ini_angle + fin_angle))]), np.array([befor_y-(Width/2)*np.sin(np.deg2rad(ini_angle + fin_angle)), fin_y-(Width/2)*np.sin(np.deg2rad(ini_angle + fin_angle))]), color="#888888", linestyle="solid")
    ax.plot(np.array([befor_x-(Width/2)*np.cos(np.deg2rad(ini_angle + fin_angle)), fin_x-(Width/2)*np.cos(np.deg2rad(ini_angle + fin_angle))]), np.array([befor_y+(Width/2)*np.sin(np.deg2rad(ini_angle + fin_angle)), fin_y+(Width/2)*np.sin(np.deg2rad(ini_angle + fin_angle))]), color="#888888", linestyle="solid")
    canvas.draw()  # キャンバスの描画

def SetAngle(foge):
    global ini_x
    global ini_y
    global ini_angle
    global fin_angle

    if foge == 90:
        ini_x = 0.0
        ini_y = 45.0
        ini_angle = 0.0
        fin_angle = 90.0

    if foge == 180:
        ini_x = 0.0
        ini_y = 45.0
        ini_angle = 0.0
        fin_angle = 180.0

    if foge == 45:
        ini_x = 0.0
        ini_y = 45.0
        ini_angle = 0.0
        fin_angle = 45.0

    if foge == 135:
        ini_x = 0.0
        ini_y = 45.0
        ini_angle = 0.0
        fin_angle = 135.0

    if foge == 91:
        ini_x = 0.0
        ini_y = 90.0
        ini_angle = 45.0
        fin_angle = 90.0

    if foge == 46:
        ini_x = 0.0
        ini_y = 90.0
        ini_angle = 45.0
        fin_angle = 45.0

    if foge == 136:
        ini_x = 0.0
        ini_y = 90.0
        ini_angle = 45.0
        fin_angle = 135.0



if __name__ == "__main__":
    try:
        #speed = 300  # mm/s
        #low_AngVel = 10980  # 最大角速度(ジャイロ生値)
        #Low_AngAcl = 180  # 角加速度(ジャイロ生値)

        #pri_offset = 55
        #post_offset = 55

        #GUIの生成
        root = tkinter.Tk()
        root.title("たーんしみゅれーた")

        #グラフの設定
        fig,ax1 = plt.subplots(figsize=(7.0, 7.0))
        fig.gca().set_aspect('equal', adjustable='box') #グラフ領域の調整

        #キャンバスの生成
        Canvas = FigureCanvasTkAgg(fig, master=root)
        Canvas.get_tk_widget().grid(row=0, rowspan=10, column=1)

        #ラベルに関する諸々の設定
        GridLabel = tkinter.Label(text="速度(mm/s)")
        GridLabel.grid(row=0, column=2)
        GridLabel = tkinter.Label(text="最大角速度(生値)\n32768=2000 °/s")
        GridLabel.grid(row=1, column=2)
        GridLabel = tkinter.Label(text="角加速度(生値)")
        GridLabel.grid(row=2, column=2)
        GridLabel = tkinter.Label(text="入口オフセット(mm)")
        GridLabel.grid(row=3, column=2)
        GridLabel = tkinter.Label(text="出口オフセット(mm)")
        GridLabel.grid(row=4, column=2)
        GridLabel = tkinter.Label(text="スリップアングル係数")
        GridLabel.grid(row=5, column=2)
        GridLabel = tkinter.Label(text="機体の横幅(mm)")
        GridLabel.grid(row=6, column=2)

        #テキストボックスに関する諸々の設定
        Set_Speed = tkinter.Entry(width=10)
        Set_Speed.grid(row=0, column=3)

        Set_low_AngVel = tkinter.Entry(width=10)
        Set_low_AngVel.grid(row=1, column=3)

        Set_Low_AngAcl = tkinter.Entry(width=10)
        Set_Low_AngAcl.grid(row=2, column=3)

        Set_pri_offset = tkinter.Entry(width=10)
        Set_pri_offset.grid(row=3, column=3)

        Set_post_offset = tkinter.Entry(width=10)
        Set_post_offset.grid(row=4, column=3)

        Set_K_SP = tkinter.Entry(width=10)
        Set_K_SP.grid(row=5, column=3)

        Set_Width = tkinter.Entry(width=10)
        Set_Width.grid(row=6, column=3)

        Set_Speed.insert(0, '300')
        Set_low_AngVel.insert(0, '10980')
        Set_Low_AngAcl.insert(0, '180')
        Set_pri_offset.insert(0, '55')
        Set_post_offset.insert(0, '55')
        Set_K_SP.insert(0, '0.002')
        Set_Width.insert(0, '39')

        DrawCanvas(Canvas, ax1)

        ReDrawButton = tkinter.Button(text="90°", width=10, command=partial(SetAngle, 90))  # ボタンの生成
        ReDrawButton.grid(row=0, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="180°", width=10, command=partial(SetAngle, 180))  # ボタンの生成
        ReDrawButton.grid(row=1, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="入45°", width=10, command=partial(SetAngle, 45))  # ボタンの生成
        ReDrawButton.grid(row=2, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="出45°", width=10, command=partial(SetAngle, 46))  # ボタンの生成
        ReDrawButton.grid(row=3, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="V90°", width=10, command=partial(SetAngle, 91))  # ボタンの生成
        ReDrawButton.grid(row=4, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="入135°", width=10, command=partial(SetAngle, 135))  # ボタンの生成
        ReDrawButton.grid(row=5, column=0)  # 描画位置(テキトー)

        ReDrawButton = tkinter.Button(text="出135°", width=10, command=partial(SetAngle, 136))  # ボタンの生成
        ReDrawButton.grid(row=6, column=0)  # 描画位置(テキトー)


        ReDrawButton = tkinter.Button(text="軌道生成", width=10, command=partial(DrawTrace, Canvas, ax1))  # ボタンの生成
        ReDrawButton.grid(row=8, column=2)  # 描画位置(テキトー)
        # rawTrace(Canvas,ax1)

        root.mainloop()#描画し続ける

    except:
        import traceback
        traceback.print_exc()
    finally:
        input(">>")#エラー吐き出したときの表示待ち


