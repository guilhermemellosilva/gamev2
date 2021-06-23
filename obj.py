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

    def drawing(self, window):
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

    def move_midoriya(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0]
            self.sprite.rect[1] = pygame.mouse.get_pos()[1]
    
    def colision(self, group, name):
        name = name
        colison = pygame.sprite.spritecollide(self.sprite, group, False)

        if name == "Livro1" and colison:
            print("Livro")
        elif name == "Spider" and colison:
            print("Spider")

    def anim(self):
        self.tick += 1
        if self.tick >= 8:
            self.tick = 0
            self.frame += 1

        if self.frame > 4:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/personagem.png")
