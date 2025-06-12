import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        file_path = '../imagens/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        if color == 'enemy':
            self.value = 100
        elif color == 'enemy_blue':
            self.value = 200
        elif color == 'enemy_red': 
            self.value = 300

    def update(self,direction):
        self.rect.x += direction