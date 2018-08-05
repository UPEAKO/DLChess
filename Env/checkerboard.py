import tkinter as tk
from PIL import Image, ImageTk


class Checkerboard(tk.Tk):
    def __init__(self):
        super(Checkerboard, self).__init__()
        self.title("checkerboard")
        # 每一格的宽度
        self.each = 50
        # 设定棋盘大小
        self.geometry(str(self.each * 10) + 'x' + str(self.each * 11) + '+10+300')
        self.canvas = tk.Canvas(self, width=self.each * 10, height=self.each *11)
        self.draw_lines()
        self.draw_chessman()
        self.canvas.pack()

    def draw_lines(self):
        # 横向线
        for row in range(10):
            self.canvas.create_line(self.each, self.each*(row+1), self.each*9, self.each*(row+1))
        # 纵向左右两条
        self.canvas.create_line(self.each, self.each, self.each, self.each*10)
        self.canvas.create_line(self.each*9, self.each, self.each*9, self.each*10)
        # 纵向断开
        for column in range(7):
            self.canvas.create_line(self.each*(2+column), self.each, self.each*(2+column), self.each*5)
            self.canvas.create_line(self.each * (2 + column), self.each * 6, self.each * (2 + column), self.each * 10)
        # 士lines
        self.canvas.create_line(self.each * 4, self.each, self.each * 6, self.each * 3)
        self.canvas.create_line(self.each * 6, self.each, self.each * 4, self.each * 3)
        self.canvas.create_line(self.each * 4, self.each * 8, self.each * 6, self.each * 10)
        self.canvas.create_line(self.each * 6, self.each * 8, self.each * 4, self.each * 10)
        # 楚河汉界
        self.canvas.create_text(self.each * 2, self.each * 5.5, text="楚河")
        self.canvas.create_text(self.each * 8, self.each * 5.5, text="汉界")

    def draw_chessman(self):
        global b1, b2, b3, b4, b5, b6, b7
        b1 = ImageTk.PhotoImage(Image.open('../src/b1.png').resize((self.each, self.each), Image.ANTIALIAS))
        b2 = ImageTk.PhotoImage(Image.open('../src/b2.png').resize((self.each, self.each), Image.ANTIALIAS))
        b3 = ImageTk.PhotoImage(Image.open('../src/b3.png').resize((self.each, self.each), Image.ANTIALIAS))
        b4 = ImageTk.PhotoImage(Image.open('../src/b4.png').resize((self.each, self.each), Image.ANTIALIAS))
        b5 = ImageTk.PhotoImage(Image.open('../src/b5.png').resize((self.each, self.each), Image.ANTIALIAS))
        b6 = ImageTk.PhotoImage(Image.open('../src/b6.png').resize((self.each, self.each), Image.ANTIALIAS))
        b7 = ImageTk.PhotoImage(Image.open('../src/b7.png').resize((self.each, self.each), Image.ANTIALIAS))
        global b11, b21, b22, b31, b32, b41, b42, b51, b52, b61, b62, b71, b72, b73, b74, b75
        b11 = self.canvas.create_image(self.each * 5, self.each, image=b1)

        b21 = self.canvas.create_image(self.each * 1, self.each, image=b2)
        b22 = self.canvas.create_image(self.each * 9, self.each, image=b2)
        b31 = self.canvas.create_image(self.each * 2, self.each, image=b3)
        b32 = self.canvas.create_image(self.each * 8, self.each, image=b3)
        b41 = self.canvas.create_image(self.each * 3, self.each, image=b4)
        b42 = self.canvas.create_image(self.each * 7, self.each, image=b4)
        b51 = self.canvas.create_image(self.each * 4, self.each, image=b5)
        b52 = self.canvas.create_image(self.each * 6, self.each, image=b5)

        b61 = self.canvas.create_image(self.each * 2, self.each * 3, image=b6)
        b62 = self.canvas.create_image(self.each * 8, self.each * 3, image=b6)

        b71 = self.canvas.create_image(self.each * 1, self.each * 4, image=b7)
        b72 = self.canvas.create_image(self.each * 3, self.each * 4, image=b7)
        b73 = self.canvas.create_image(self.each * 5, self.each * 4, image=b7)
        b74 = self.canvas.create_image(self.each * 7, self.each * 4, image=b7)
        b75 = self.canvas.create_image(self.each * 9, self.each * 4, image=b7)

        global r1, r2, r3, r4, r5, r6, r7
        r1 = ImageTk.PhotoImage(Image.open('../src/r1.png').resize((self.each, self.each), Image.ANTIALIAS))
        r2 = ImageTk.PhotoImage(Image.open('../src/r2.png').resize((self.each, self.each), Image.ANTIALIAS))
        r3 = ImageTk.PhotoImage(Image.open('../src/r3.png').resize((self.each, self.each), Image.ANTIALIAS))
        r4 = ImageTk.PhotoImage(Image.open('../src/r4.png').resize((self.each, self.each), Image.ANTIALIAS))
        r5 = ImageTk.PhotoImage(Image.open('../src/r5.png').resize((self.each, self.each), Image.ANTIALIAS))
        r6 = ImageTk.PhotoImage(Image.open('../src/r6.png').resize((self.each, self.each), Image.ANTIALIAS))
        r7 = ImageTk.PhotoImage(Image.open('../src/r7.png').resize((self.each, self.each), Image.ANTIALIAS))
        global r11, r21, r22, r31, r32, r41, r42, r51, r52, r61, r62, r71, r72, r73, r74, r75
        r11 = self.canvas.create_image(self.each * 5, self.each * 10, image=r1)

        r21 = self.canvas.create_image(self.each * 1, self.each * 10, image=r2)
        r22 = self.canvas.create_image(self.each * 9, self.each * 10, image=r2)
        r31 = self.canvas.create_image(self.each * 2, self.each * 10, image=r3)
        r32 = self.canvas.create_image(self.each * 8, self.each * 10, image=r3)
        r41 = self.canvas.create_image(self.each * 3, self.each * 10, image=r4)
        r42 = self.canvas.create_image(self.each * 7, self.each * 10, image=r4)
        r51 = self.canvas.create_image(self.each * 4, self.each * 10, image=r5)
        r52 = self.canvas.create_image(self.each * 6, self.each * 10, image=r5)

        r61 = self.canvas.create_image(self.each * 2, self.each * 8, image=r6)
        r62 = self.canvas.create_image(self.each * 8, self.each * 8, image=r6)

        r71 = self.canvas.create_image(self.each * 1, self.each * 7, image=r7)
        r72 = self.canvas.create_image(self.each * 3, self.each * 7, image=r7)
        r73 = self.canvas.create_image(self.each * 5, self.each * 7, image=r7)
        r74 = self.canvas.create_image(self.each * 7, self.each * 7, image=r7)
        r75 = self.canvas.create_image(self.each * 9, self.each * 7, image=r7)

    def move_chess(self, event):
        self.canvas.move(b11, 0, self.each * 5)

    def bind_all(self):
        self.canvas.tag_bind(b11, "<Button-1>", self.move_chess)


check = Checkerboard()
check.bind_all()
check.mainloop()

