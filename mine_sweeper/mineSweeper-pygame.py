# python3.6
# MineSweeper Ver0.2.1
# By Tianqi W

import random
import pygame
from pygame.locals import *



class Game:
    def __init__(self, size=(10, 10), number=10):
        self.x = size[0]
        self.y = size[1]
        self.number = number
        self.gameover = False
        self.__check()
        self.board = self.__create()
        self.__lay_mine()
        sizes = {"start": (360, 400), "1": (400, 400), "2": (600, 500), "3": (830, 720)}
        if number == 10:
            self.window = pygame.display.set_mode(sizes["1"])
        elif number == 50:
            self.window = pygame.display.set_mode(sizes["2"])
        else:
            self.window = pygame.display.set_mode(sizes["3"])
        self.font = pygame.font.SysFont('Helvetica Bold', 25)

    def draw_tile(self, value, i, j):
        if value == "*":
            pygame.draw.rect(self.window, (196, 211, 202), self.board[i * self.x + j].rect)
        if value == "`":
            pygame.draw.rect(self.window, (156, 255, 157), self.board[i * self.x + j].rect)
        elif value.isdecimal():
            pygame.draw.rect(self.window, (196, 211, 202), self.board[i * self.x + j].rect)
            value = int(value)
            if value == 1:
                self.window.blit(self.font.render('1', True, (0, 0, 190)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))
            elif value == 2:
                self.window.blit(self.font.render('2', True, (0, 160, 0)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 3:
                self.window.blit(self.font.render('3', True, (240, 240, 0)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 4:
                self.window.blit(self.font.render('4', True, (240, 180, 0)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 5:
                self.window.blit(self.font.render('5', True, (255, 50, 0)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 6:
                self.window.blit(self.font.render('6', True, (184, 67, 239)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 7:
                self.window.blit(self.font.render('7', True, (84, 60, 84)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

            elif value == 8:
                self.window.blit(self.font.render('8', True, (57, 55, 58)),
                                 (self.board[i * self.x + j].rect.x+5, self.board[i * self.x + j].rect.y+2))

        elif value == "@":
            pygame.draw.rect(self.window, (255, 1, 0), self.board[i * self.x + j].rect)
            self.window.blit(self.font.render('X', True, (0, 0, 0)),
                             (self.board[i * self.x + j].rect.x + 5, self.board[i * self.x + j].rect.y + 2))
        elif value == "P":
            pygame.draw.rect(self.window, (255, 119, 0), self.board[i * self.x + j].rect)
            self.window.blit(self.font.render('P', True, (0, 0, 0)),
                             (self.board[i * self.x + j].rect.x + 5, self.board[i * self.x + j].rect.y + 2))








    class Cell:
        def __init__(self, parent, cid, pos):
            self.id = cid
            self.opened = False
            self.is_mine = False
            self.flagged = False
            self.status = 0
            self.parent = parent
            self.rect = Rect(pos[0],pos[1],pos[2],pos[3])

        def open(self):
            if not self.opened:
                if not self.flagged:
                    if self.is_mine:
                        self.parent.game_over(0)
                    else:
                        self.status = self.parent.calculate(self.id)
                        self.opened = True

        def flag(self):
            if not self.opened:
                if not self.flagged:
                    self.flagged = True
                else:
                    self.flagged = False

        def __str__(self):
            if self.flagged:
                return 'P'
            elif not self.opened:
                return '*'

            else:
                if not self.status:
                    return '`'
                else:
                    return str(self.status)

        def __unicode__(self):
            if self.flagged:
                return 'P'
            elif not self.opened:
                return '*'

            else:
                if not self.status:
                    return '`'
                else:
                    return str(self.status)

    def __check(self):
        area = self.x * self.y
        if self.number >= area:
            raise ArithmeticError('Mines out of range')

    def __create(self):
        board = []
        num = 0
        x = 8
        y = 28
        count = 0
        self.area = self.x * self.y
        for i in range(self.area):
            if count < self.x:
                x += 22
                count += 1
            else:
                x = 30
                y += 22
                count = 1
            pos = (x, y, 20, 20)
            board.append(self.Cell(self, num, pos))
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
                self.draw_tile(str(self.board[i*self.x + j]), i, j)

            print(" ".join(temp))

        pygame.display.flip()

    def get_board(self):
        self.__print()

    def show_mine(self):
        for i in range(self.y):
            temp = []
            for j in range(self.x):
                if self.board[i*self.x + j].is_mine:
                    temp.append("@")
                    self.draw_tile("@", i, j)

                else:
                    temp.append(str(self.board[i*self.x + j]))
                    self.draw_tile(str(self.board[i * self.x + j]), i, j)
            print(" ".join(temp))

        pygame.display.flip()

    def check_board(self):
        opened = 0
        for i in self.board:
            if i.opened:
                opened += 1
        if self.area - opened == self.number:
            self.game_over(1)

    def game_over(self, code):
        offset = self.window.get_width()
        font = pygame.font.SysFont('Comic Sans MS', 20)

        if code == 0:
            surface = font.render('YOU LOSE', True, (255, 0, 0))
            self.window.blit(surface, (offset-120, 100))
            print("GameOver!")
            self.gameover = True

        if code == 1:
            surface = font.render('YOU WIN', True, (0, 255, 0))
            self.window.blit(surface, (offset-120, 100))
            print("Win!")
            self.gameover = True





    def calculate(self, cid):
        cell = self.board[cid]
        if not cell.opened and not cell.flagged:
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

    def get_input(self):
        while not self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.__dict__["button"] == 1:
                        x, y = event.__dict__["pos"]
                        for i in self.board:
                            if i.rect.collidepoint(x, y):
                                print(i.id+1)
                                return i.id+1
                    elif event.__dict__["button"] == 3:
                        x, y = event.__dict__["pos"]
                        for i in self.board:
                            if i.rect.collidepoint(x, y):
                                print(str(i.id+1), 'flagged')
                                i.flag()
                                self.get_board()
                                return None
                else:
                    return

        self.show_mine()

        while self.gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()




def main():
    _easy = (10, 10, 10)  # x, y , mines
    _normal = (20, 15, 50)
    _hard = (30, 20, 100)
    pygame.init()
    pygame.font.init()
    sizes = {"start": (360, 400), "1": (400, 400), "2": (720, 500), "3": (1000, 720)}
    screen = pygame.display.set_mode(sizes["start"])
    rect_easy = Rect(105, 100, 150, 50)
    rect_normal = Rect(105, 160, 150, 50)
    rect_hard = Rect(105, 220, 150, 50)
    screen.fill((100, 200, 100))
    pygame.draw.rect(screen, (25, 190, 250), rect_easy, 0)
    pygame.draw.rect(screen, (230, 200, 100), rect_normal, 0)
    pygame.draw.rect(screen, (175, 50, 45), rect_hard, 0)
    title = pygame.font.SysFont('Comic Sans MS', 30)
    difficulty = pygame.font.SysFont('Helvetica', 30)
    easy_surface = difficulty.render('Easy', True, (250, 250, 250))
    normal_surface = difficulty.render('Normal', True, (250, 250, 250))
    hard_surface = difficulty.render('Hard', True, (250, 250, 250))
    title_surface = title.render('MineSweeper', False, (0, 0, 0))

    screen.blit(title_surface, (80, 30))
    screen.blit(easy_surface, (152, 105))
    screen.blit(normal_surface, (141, 165))
    screen.blit(hard_surface, (152, 225))

    about = pygame.font.SysFont('Helvetica', 15)
    about_surface = about.render('By TianqiW', True, (0, 0, 0))
    screen.blit(about_surface, (290,380))

    try:
        mine = pygame.image.load("mine.png")
        screen.blit(mine, (270, 30))
    except:
        pass
    _continue = True
    mode = (10, 10, 10)

    while _continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.__dict__["pos"]
                if rect_easy.collidepoint(x, y):
                    print("Easy")
                    mode = _easy
                    pygame.display.quit()
                    _continue = False
                elif rect_normal.collidepoint(x, y):
                    print("Normal")
                    mode = _normal
                    pygame.display.quit()
                    _continue = False
                elif rect_hard.collidepoint(x, y):
                    print("Hard")
                    mode = _hard
                    pygame.display.quit()
                    _continue = False
        if _continue:
            pygame.display.flip()

    game = Game((mode[0], mode[1]), mode[2])
    game.get_board()
    pos = game.get_input()
    while pos == None:
        pos = game.get_input()

    while True:
        if game.board[pos - 1].is_mine:
            game = Game((mode[0], mode[1]), mode[2])
        else:
            game.board[pos - 1].open()
            game.get_board()
            break

    while True:
        pos = game.get_input()
        while pos == None:
            pos = game.get_input()
        game.board[pos-1].open()
        game.get_board()
        game.check_board()


if __name__ == '__main__':
    main()
