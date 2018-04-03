# python3.6
# MineSweeper Ver0.1.0
# By Tianqi W

import random


class Game:
    def __init__(self, size, number):
        self.x = size[0]
        self.y = size[1]
        self.number = number
        self.__check()
        self.board = self.__create()
        self.__lay_mine()
        # self.__print()

    class Cell:
        def __init__(self, parent, cid):
            self.id = cid
            self.opened = False
            self.is_mine = False
            self.status = 0
            self.parent = parent

        def open(self):
            if not self.opened:
                if self.is_mine:
                    self.parent.game_over(0)
                else:
                    self.status = self.parent.calculate(self.id)
                    self.opened = True

        def __str__(self):
            if not self.opened:
                return '*'
            else:
                if not self.status:
                    return '`'
                else:
                    return str(self.status)

        def __unicode__(self):
            if not self.opened:
                return '*'
            else:
                return str(self.status)


    def __check(self):
        area = self.x * self.y
        if self.number >= area:
            raise ArithmeticError('Mines out of range')

    def __create(self):
        board = []
        num = 0
        self.area = self.x * self.y
        for i in range(self.area):
            board.append(self.Cell(self, num))
            num += 1

        return board

    def __lay_mine(self):
        choice = []
        for i in range(self.area):
            choice.append(i)
        for i in range(self.number):
            mine = random.choice(choice)
            choice.remove(mine)
            self.board[mine].is_mine = True

    def __print(self):
        for i in range(self.y):
            temp = []
            for j in range(self.x):
                temp.append(str(self.board[i*self.x + j]))
            print(" ".join(temp))

    def get_board(self):
        self.__print()

    def show_mine(self):
        for i in range(self.y):
            temp = []
            for j in range(self.x):
                if self.board[i*self.x + j].is_mine:
                    temp.append("@")
                else:
                    temp.append(str(self.board[i*self.x + j]))
            print(" ".join(temp))

    def check_board(self):
        opened = 0
        for i in self.board:
            if i.opened:
                opened += 1
        if self.area - opened == self.number:
            self.game_over(1)

    def game_over(self, code):
        if code == 0:
            self.show_mine()
            print("GameOver!")
            exit()
        if code == 1:
            print("Win!")
            exit()

    def calculate(self, cid):
        cell = self.board[cid]
        if not cell.opened:
            up = False
            down = False
            left = False
            right = False

            sum = 0

            if self.board[cid].is_mine:
                return 1
            else:
                if open:
                    self.board[cid].opened = True
                if cid % self.x:
                    if self.board[cid-1].is_mine:
                        sum += 1
                    left = True
                if cid % self.x != self.x-1:
                    if self.board[cid+1].is_mine:
                        sum += 1
                    right = True
                if cid - self.x >= 0:
                    if self.board[cid-self.x].is_mine:
                        sum += 1
                    up = True
                if cid + self.x < self.area:
                    if self.board[cid+self.x].is_mine:
                        sum += 1
                    down = True

                if up and left:
                    if self.board[cid-1-self.x].is_mine:
                        sum += 1
                if up and right:
                    if self.board[cid+1-self.x].is_mine:
                        sum += 1
                if down and left:
                    if self.board[cid-1+self.x].is_mine:
                        sum += 1
                if down and right:
                    if self.board[cid+1+self.x].is_mine:
                        sum += 1

                self.board[cid].status = sum
                if sum:
                    return sum
                else:
                    if left:
                        self.calculate(cid-1)
                    if right:
                        self.calculate(cid+1)
                    if up:
                        self.calculate(cid-self.x)
                    if down:
                        self.calculate(cid+self.x)

                    if up and left:
                        self.calculate(cid-1-self.x)
                    if up and right:
                        self.calculate(cid+1-self.x)
                    if down and left:
                        self.calculate(cid-1+self.x)
                    if down and right:
                        self.calculate(cid+1+self.x)
                    return 0
        else:
            return 0


def main():
    cfg = input("输入大小 和雷的数量（例子：10 10 10）")
    cfg = cfg.split()

    game = Game((10,10),10)
    game.get_board()
    pos = input()
    while True:
        if game.board[int(pos) - 1].is_mine:
            game = Game((int(cfg[0]), int(cfg[1])), int(cfg[2]))
        else:
            game.board[int(pos) - 1].open()
            game.get_board()
            break

    while True:
        pos = input()
        game.board[int(pos)-1].open()
        game.get_board()
        game.check_board()


if __name__ == '__main__':
    main()
