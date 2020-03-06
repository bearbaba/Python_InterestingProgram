import pygame
from game_sprite import *
SCREEN=pygame.Rect(0,0,333,500)
class Game():
    def __init__(self):
        print("游戏初始化")
        #1.设置游戏窗口
        self.screen=pygame.display.set_mode(SCREEN.size)
        #2.创建游戏时钟
        self.clock=pygame.time.Clock()
        #3.调用私有方法，精灵和精灵组的创建
        self.__create_sprite()
    def game_start(self):
        print("游戏开始")
    def __create_sprite(self):
        pass



if __name__ == '__main__':
    game=Game()
    game.game_start()
