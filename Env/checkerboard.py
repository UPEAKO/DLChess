import tkinter as tk
import random
from PIL import Image, ImageTk


'''注意训练的时候有卡住不能移动的棋子,当然人工移动不存在这种情况,待会再说'''
'''如何模仿点击动作'''


class Checkerboard(tk.Tk):
    def __init__(self):
        super(Checkerboard, self).__init__()
        self.title("checkerboard")
        # 每一格的宽度
        self.each = 50
        # 记录所有棋子的ID,便于修改棋子
        self.chess_id = [1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1,
                         1, 1, 1, 1, 1,

                         1, 1, 1, 1, 1,
                         1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1]
        # 记录所有棋子位置的列表
        self.locations = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                          20, 26,
                          28, 30, 32, 34, 36,

                          55, 57, 59, 61, 63,
                          65, 71,
                          82, 83, 84, 85, 86, 87, 88, 89, 90]
        # 判断棋子是否存在
        self.is_live = [True, True, True, True, True, True, True, True, True,
                        True, True,
                        True, True, True, True, True,

                        True, True, True, True, True,
                        True, True,
                        True, True, True, True, True, True, True, True, True]
        # 当前棋子所有可走位置
        self.roads = []
        # 当前为红方
        self.is_red = True
        # 设定棋盘大小
        self.geometry(str(self.each * 10) + 'x' + str(self.each * 11) + '+10+300')
        self.canvas = tk.Canvas(self, width=self.each * 10, height=self.each * 11)
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

        self.chess_id[4] = self.canvas.create_image(self.each * 5, self.each, image=b1)

        self.chess_id[3] = self.canvas.create_image(self.each * 4, self.each, image=b2)
        self.chess_id[5] = self.canvas.create_image(self.each * 6, self.each, image=b2)
        self.chess_id[2] = self.canvas.create_image(self.each * 3, self.each, image=b3)
        self.chess_id[6] = self.canvas.create_image(self.each * 7, self.each, image=b3)
        self.chess_id[1] = self.canvas.create_image(self.each * 2, self.each, image=b4)
        self.chess_id[7] = self.canvas.create_image(self.each * 8, self.each, image=b4)
        self.chess_id[0] = self.canvas.create_image(self.each * 1, self.each, image=b5)
        self.chess_id[8] = self.canvas.create_image(self.each * 9, self.each, image=b5)

        self.chess_id[9] = self.canvas.create_image(self.each * 2, self.each * 3, image=b6)
        self.chess_id[10] = self.canvas.create_image(self.each * 8, self.each * 3, image=b6)

        self.chess_id[11] = self.canvas.create_image(self.each * 1, self.each * 4, image=b7)
        self.chess_id[12] = self.canvas.create_image(self.each * 3, self.each * 4, image=b7)
        self.chess_id[13] = self.canvas.create_image(self.each * 5, self.each * 4, image=b7)
        self.chess_id[14] = self.canvas.create_image(self.each * 7, self.each * 4, image=b7)
        self.chess_id[15] = self.canvas.create_image(self.each * 9, self.each * 4, image=b7)

        global r1, r2, r3, r4, r5, r6, r7
        r1 = ImageTk.PhotoImage(Image.open('../src/r1.png').resize((self.each, self.each), Image.ANTIALIAS))
        r2 = ImageTk.PhotoImage(Image.open('../src/r2.png').resize((self.each, self.each), Image.ANTIALIAS))
        r3 = ImageTk.PhotoImage(Image.open('../src/r3.png').resize((self.each, self.each), Image.ANTIALIAS))
        r4 = ImageTk.PhotoImage(Image.open('../src/r4.png').resize((self.each, self.each), Image.ANTIALIAS))
        r5 = ImageTk.PhotoImage(Image.open('../src/r5.png').resize((self.each, self.each), Image.ANTIALIAS))
        r6 = ImageTk.PhotoImage(Image.open('../src/r6.png').resize((self.each, self.each), Image.ANTIALIAS))
        r7 = ImageTk.PhotoImage(Image.open('../src/r7.png').resize((self.each, self.each), Image.ANTIALIAS))

        self.chess_id[27] = self.canvas.create_image(self.each * 5, self.each * 10, image=r1)

        self.chess_id[26] = self.canvas.create_image(self.each * 4, self.each * 10, image=r2)
        self.chess_id[28] = self.canvas.create_image(self.each * 6, self.each * 10, image=r2)
        self.chess_id[25] = self.canvas.create_image(self.each * 3, self.each * 10, image=r3)
        self.chess_id[29] = self.canvas.create_image(self.each * 7, self.each * 10, image=r3)
        self.chess_id[24] = self.canvas.create_image(self.each * 2, self.each * 10, image=r4)
        self.chess_id[30] = self.canvas.create_image(self.each * 8, self.each * 10, image=r4)
        self.chess_id[23] = self.canvas.create_image(self.each * 1, self.each * 10, image=r5)
        self.chess_id[31] = self.canvas.create_image(self.each * 9, self.each * 10, image=r5)

        self.chess_id[21] = self.canvas.create_image(self.each * 2, self.each * 8, image=r6)
        self.chess_id[22] = self.canvas.create_image(self.each * 8, self.each * 8, image=r6)

        self.chess_id[16] = self.canvas.create_image(self.each * 1, self.each * 7, image=r7)
        self.chess_id[17] = self.canvas.create_image(self.each * 3, self.each * 7, image=r7)
        self.chess_id[18] = self.canvas.create_image(self.each * 5, self.each * 7, image=r7)
        self.chess_id[19] = self.canvas.create_image(self.each * 7, self.each * 7, image=r7)
        self.chess_id[20] = self.canvas.create_image(self.each * 9, self.each * 7, image=r7)

    # 此函数用于人工操作,点击进行游戏
    def move_decision(self, event):
        current_num, sign = self.get_num_by_xy(event.x, event.y)
        if self.is_who(current_num) == 2:
            self.move_roads(event.x, event.y)
            self.roads.append(current_num)
        else:
            for num in self.roads:
                if current_num == num:
                    if self.is_who(current_num) == 1:
                        self.canvas.delete(self.chess_id[self.get_subscript_by_num(current_num)])
                        self.is_live[self.get_subscript_by_num(current_num)] = False
                        row, column = self.get_rc_by_num(current_num)
                        self.canvas.coords(self.chess_id[self.get_subscript_by_num(self.roads[-1])], self.each * column,
                                           self.each * row)
                        self.locations[self.get_subscript_by_num(self.roads[-1])] = current_num
                        self.roads.clear()
                        if self.is_red:
                            self.is_red = False
                        else:
                            self.is_red = True
                        break
                    else:
                        row, column = self.get_rc_by_num(current_num)
                        self.canvas.coords(self.chess_id[self.get_subscript_by_num(self.roads[-1])], self.each * column,
                                           self.each * row)
                        self.locations[self.get_subscript_by_num(self.roads[-1])] = current_num
                        self.roads.clear()
                        if self.is_red:
                            self.is_red = False
                        else:
                            self.is_red = True
                        break
                        break

    # 由棋子位置获取下标,否则返回 -1
    def get_subscript_by_num(self, num):
        for subscript in range(len(self.locations)):
            if self.locations[subscript] == num:
                return subscript
        return -1

    # 获取当前棋子所有可行数字位置,存入self.roads
    def move_roads(self, current_x, current_y):
        self.roads.clear()
        current_num, sign = self.get_num_by_xy(current_x, current_y)
        if current_num > 0:
            # 对不同类型的棋子分类处理
            if sign == "j":
                next_num = current_num - 1
                while int((next_num - 1 + 1) / 9) == int((next_num - 1) / 9):
                    if self.is_who(next_num) < 2:
                        self.roads.append(next_num)
                        next_num = next_num - 1
                    else:
                        break
                next_num = current_num + 1
                while int((next_num - 1 - 1) / 9) == int((next_num - 1) / 9):
                    if self.is_who(next_num) < 2:
                        self.roads.append(next_num)
                        next_num = next_num + 1
                    else:
                        break
                next_num = current_num + 9
                while 1 <= next_num <= 90:
                    if self.is_who(next_num) < 2:
                        self.roads.append(next_num)
                        next_num = next_num + 9
                    else:
                        break
                next_num = current_num - 9
                while 1 <= next_num <= 90:
                    if self.is_who(next_num) < 2:
                        self.roads.append(next_num)
                        next_num = next_num - 9
                    else:
                        break
            elif sign == "m":
                base_num = current_num - 2 * 9
                if 1 <= base_num <= 90 and self.is_who(base_num + 9) == 0:
                    if int((base_num - 1) / 9) == int((base_num - 1 - 1) / 9) and self.is_who(base_num - 1) < 2:
                        self.roads.append(base_num - 1)
                    if int((base_num - 1) / 9) == int((base_num - 1 + 1) / 9) and self.is_who(base_num + 1) < 2:
                        self.roads.append(base_num + 1)
                base_num = current_num + 2 * 9
                if 1 <= base_num <= 90 and self.is_who(base_num - 9) == 0:
                    if int((base_num - 1) / 9) == int((base_num - 1 - 1) / 9) and self.is_who(base_num - 1) < 2:
                        self.roads.append(base_num - 1)
                    if int((base_num - 1) / 9) == int((base_num - 1 + 1) / 9) and self.is_who(base_num + 1) < 2:
                        self.roads.append(base_num + 1)
                base_num = current_num - 2
                if int((base_num - 1) / 9) == int((base_num - 1 + 2) / 9) and self.is_who(base_num + 1) == 0:
                    if 1 <= base_num - 9 <= 90 and self.is_who(base_num - 9) < 2:
                        self.roads.append(base_num - 9)
                    if 1 <= base_num + 9 <= 90 and self.is_who(base_num + 9) < 2:
                        self.roads.append(base_num + 9)
                base_num = current_num + 2
                if int((base_num - 1) / 9) == int((base_num - 1 + 2) / 9) and self.is_who(base_num - 1) == 0:
                    if 1 <= base_num - 9 <= 90 and self.is_who(base_num - 9) < 2:
                        self.roads.append(base_num - 9)
                    if 1 <= base_num + 9 <= 90 and self.is_who(base_num + 9) < 2:
                        self.roads.append(base_num + 9)
            elif sign == "x":
                base_num = current_num - 9 - 1
                if (46 if self.is_red else 1) <= base_num <= (90 if self.is_red else 45) and self.is_who(base_num) == \
                        0 and self.is_who(base_num - 9 - 1) < 2 and int((base_num - 1) / 9) == int((base_num - 1 + 1) / 9):
                    self.roads.append(base_num - 9 - 1)
                base_num = current_num - 9 + 1
                if (46 if self.is_red else 1) <= base_num <= (90 if self.is_red else 45) and self.is_who(base_num) == \
                        0 and self.is_who(base_num - 9 + 1) < 2 and int((base_num - 1) / 9) == int((base_num - 1 - 1) / 9):
                    self.roads.append(base_num - 9 + 1)
                base_num = current_num + 9 - 1
                if (46 if self.is_red else 1) <= base_num <= (90 if self.is_red else 45) and self.is_who(base_num) == \
                        0 and self.is_who(base_num + 9 - 1) < 2 and int((base_num - 1) / 9) == int((base_num - 1 + 1) / 9):
                    self.roads.append(base_num + 9 - 1)
                base_num = current_num - 9 + 1
                if (46 if self.is_red else 1) <= base_num <= (90 if self.is_red else 45) and self.is_who(base_num) == \
                        0 and self.is_who(base_num + 9 + 1) < 2 and int((base_num - 1) / 9) == int((base_num - 1 - 1) / 9):
                    self.roads.append(base_num + 9 + 1)
            elif sign == "s":
                if self.is_red:
                    if current_num != 77 and self.is_who(77) < 2:
                        self.roads.append(77)
                    else:
                        if self.is_who(67) < 2:
                            self.roads.append(67)
                        if self.is_who(69) < 2:
                            self.roads.append(69)
                        if self.is_who(85) < 2:
                            self.roads.append(85)
                        if self.is_who(87) < 2:
                            self.roads.append(87)
                else:
                    if current_num != 14 and self.is_who(14) < 2:
                        self.roads.append(14)
                    else:
                        if self.is_who(4) < 2:
                            self.roads.append(4)
                        if self.is_who(6) < 2:
                            self.roads.append(6)
                        if self.is_who(22) < 2:
                            self.roads.append(22)
                        if self.is_who(24) < 2:
                            self.roads.append(24)
            elif sign == "js":
                row, column = self.get_rc_by_num(current_num)
                if self.is_red:
                    if row - 1 >= 8 and self.is_who(current_num - 9) < 2:
                        self.roads.append(current_num - 9)
                    if row + 1 <= 10 and self.is_who(current_num + 9) < 2:
                        self.roads.append(current_num + 9)
                    if column - 1 >= 4 and self.is_who(current_num - 1) < 2:
                        self.roads.append(current_num - 1)
                    if column + 1 <= 6 and self.is_who(current_num + 1) < 2:
                        self.roads.append(current_num + 1)
                else:
                    if row - 1 >= 1 and self.is_who(current_num - 9) < 2:
                        self.roads.append(current_num - 9)
                    if row + 1 <= 3 and self.is_who(current_num + 9) < 2:
                        self.roads.append(current_num + 9)
                    if column - 1 >= 4 and self.is_who(current_num - 1) < 2:
                        self.roads.append(current_num - 1)
                    if column + 1 <= 6 and self.is_who(current_num + 1) < 2:
                        self.roads.append(current_num + 1)
            elif sign == "p":
                # 上
                next_num = current_num - 9
                while 1 <= next_num <= 90 and self.is_who(next_num) == 0:
                    self.roads.append(next_num)
                    next_num = next_num - 9
                next_num = next_num - 9
                while 1 <= next_num <= 90 and self.is_who(next_num) < 2:
                    if self.is_who(next_num) == 1:
                        self.roads.append(next_num)
                        break
                    next_num = next_num - 9
                # 下
                next_num = current_num + 9
                while 1 <= next_num <= 90 and self.is_who(next_num) == 0:
                    self.roads.append(next_num)
                    next_num = next_num + 9
                next_num = next_num + 9
                while 1 <= next_num <= 90 and self.is_who(next_num) < 2:
                    if self.is_who(next_num) == 1:
                        self.roads.append(next_num)
                        break
                    next_num = next_num + 9
                # 左
                next_num = current_num - 1
                while int((next_num - 1) / 9) == int((next_num - 1 + 1) / 9) and self.is_who(next_num) == 0:
                    self.roads.append(next_num)
                    next_num = next_num - 1
                next_num = next_num - 1
                while int((next_num - 1) / 9) == int((next_num - 1 + 1) / 9) and self.is_who(next_num) < 2:
                    if self.is_who(next_num) == 1:
                        self.roads.append(next_num)
                        break
                    next_num = next_num - 1
                # 右
                next_num = current_num + 1
                while int((next_num - 1) / 9) == int((next_num - 1 - 1) / 9) and self.is_who(next_num) == 0:
                    self.roads.append(next_num)
                    next_num = next_num + 1
                next_num = next_num + 1
                while int((next_num - 1) / 9) == int((next_num - 1 - 1) / 9) and self.is_who(next_num) < 2:
                    if self.is_who(next_num) == 1:
                        self.roads.append(next_num)
                        break
                    next_num = next_num + 1
            elif sign == "b":
                if self.is_red:
                    if current_num >= 46 and self.is_who(current_num - 9) < 2:
                        self.roads.append(current_num - 9)
                    else:
                        if current_num - 9 >= 1 and self.is_who(current_num - 9) < 2:
                            self.roads.append(current_num - 9)
                        if int((current_num - 1) / 9) == int((current_num - 1 - 1) / 2) and self.is_who(current_num - 1) < 2:
                            self.roads.append(current_num - 1)
                        if int((current_num - 1) / 9) == int((current_num - 1 + 1) / 2) and self.is_who(current_num + 1) < 2:
                            self.roads.append(current_num + 1)
                else:
                    if current_num <= 45 and self.is_who(current_num + 9) < 2:
                        self.roads.append(current_num + 9)
                    else:
                        if current_num + 9 <= 90 and self.is_who(current_num + 9) < 2:
                            self.roads.append(current_num + 9)
                        if int((current_num - 1) / 9) == int((current_num - 1 - 1) / 2) and self.is_who(current_num - 1) < 2:
                            self.roads.append(current_num - 1)
                        if int((current_num - 1) / 9) == int((current_num - 1 + 1) / 2) and self.is_who(current_num + 1) < 2:
                            self.roads.append(current_num + 1)

    # 判断当前位置是己方棋子2,对方棋子1,没有棋子0
    # 参数为当前数字位置
    def is_who(self, current_num):
        if self.is_red:
            for subscript1 in range(16, 32):
                if self.is_live[subscript1] and self.locations[subscript1] == current_num:
                    return 2
            for subscript1 in range(16):
                if self.is_live[subscript1] and self.locations[subscript1] == current_num:
                    return 1
            return 0
        else:
            for subscript2 in range(16):
                if self.is_live[subscript2] and self.locations[subscript2] == current_num:
                    return 2
            for subscript2 in range(16, 32):
                if self.is_live[subscript2] and self.locations[subscript2] == current_num:
                    return 1
            return 0

    # 根据坐标返回棋盘数字位置,如果不是棋子数字位子返回空格位置及"nothing"
    def get_num_by_xy(self, current_x, current_y):
        row = int((current_y + 25) / 50)
        column = int((current_x + 25) / 50)
        current_num = (row - 1) * 9 + column
        sign = 0
        for num in self.locations:
            sign = sign + 1
            if num == current_num and self.is_live[sign - 1]:
                if sign == 1 or sign == 9 or sign == 24 or sign == 32:
                    return num, "j"
                elif sign == 2 or sign == 8 or sign == 25 or sign == 31:
                    return num, "m"
                elif sign == 3 or sign == 7 or sign == 26 or sign == 30:
                    return num, "x"
                elif sign == 4 or sign == 6 or sign == 27 or sign == 29:
                    return num, "s"
                elif sign == 5 or sign == 28:
                    return num, "js"
                elif sign == 10 or sign == 11 or sign == 22 or sign == 23:
                    return num, "p"
                else:
                    return num, "b"
        return current_num, "nothing"

    # 根据棋盘数字位置返回行列,真的只是返回任意一个位置的行列
    @staticmethod
    def get_rc_by_num(num):
        column = num % 9
        row = int(num / 9) + 1
        if column == 0:
            column = 9
            row = int((num - 1) / 9) + 1
        return row, column

    def bind_b_and_r(self):
        self.canvas.bind("<Button-1>", self.move_decision)


check = Checkerboard()
check.bind_b_and_r()
check.mainloop()

