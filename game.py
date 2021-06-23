import pygame
from obj import Obj
from menu import Menu

class Main:

    def __init__(self, sizex, sizey, title):

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu()

        self.loop = True

    def draw(self):
        if self.menu.change_scene == False:
            self.menu.draw(self.window)
            
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

            self.menu.events(events)    

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()


game = Main(320, 640, "My Hero Academia")
game.update()

