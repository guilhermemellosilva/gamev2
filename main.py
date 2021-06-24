import pygame
from obj import Obj
from menu import Menu, GameOver
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):
        
        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/mhasound.wav")
        pygame.mixer.music.play(-1)


        self.window = pygame.display.set_mode([320, 640])
        self.title = pygame.display.set_caption("My Hero Academia")

        self.start_screen = Menu("assets/tela.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False               
            if not self.start_screen.change_scene:
                self.start_screen.events(events)
            elif not self.game.change_scene:
                self.game.midoriya.move_midoriya(events)
            else:
                self.gameover.events(events)

    def draw(self):
        self.window.fill([0, 0, 0])
        if not self.start_screen.change_scene:
            self.start_screen.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.midoriya.life = 3
            self.game.midoriya.pts = 0
            



    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


game = Main(320, 640, "My Hero Academia")
game.update()

