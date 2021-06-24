import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def draw(self, window):
        self.group.draw(window)

    def anim(self):
        self.tick += 1
        if self.tick >= 8:
            self.tick = 0
            self.frame += 1

        if self.frame > 4:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/spider" + str(self.frame) + ".png")


class Midoriya(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)  

        self.life = 3
        self.pts = 0

    def move_midoriya(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 60
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 63
    
    def colision(self, group, name):
        name = name
        colison = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "Livro1" and colison:
            self.pts += 1
        elif name == "Spider" and colison:
            self.life -= 1


    def anim(self):
        self.tick += 1
        if self.tick >= 8:
            self.tick = 0
            self.frame += 1

        if self.frame > 4:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/personagem.png")

class Text:
    
    def __init__(self, size, text):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))

