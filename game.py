import pygame
from obj import Obj, Midoriya
import random

class Game:

    def __init__(self):

        self.bg = Obj("assets/telafundo.png", 0, 0)
        self.bg2 = Obj("assets/telafundo.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)
        self.livro1 = Obj("assets/livro1.png", random.randrange(0, 300), -50)
        self.midoriya =Midoriya("assets/personagem.png", 150, 500)

        self.change_scene = False
    
    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.spider.drawing(window)
        self.livro1.drawing(window)
        self.midoriya.drawing(window)

    def update(self):
        self.move_bg()
        self.spider.anim()
        self.midoriya.anim()
        self.move_spiders()
        self.move_livro1()
    
    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)

    def move_livro1(self):
        self.livro1.sprite.rect[1] += 8

        if self.livro1.sprite.rect[1] >= 700:
            self.livro1.sprite.kill()
            self.livro1 = Obj("assets/livro1.png", random.randrange(0, 300), -50)


