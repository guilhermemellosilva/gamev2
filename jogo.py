import pygame
from obj import Obj


class Game:

    def __init__(self):

        self.bg = Obj("assets/bg.png", 0, 0)

        self.change_scene = False
    
    def draw(self, window):
        self.bg.drawing(window)

    def update(self):
        pass