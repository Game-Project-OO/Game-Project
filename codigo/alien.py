import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        file_path = '../imagens/' + image + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

        self.alvo_y = y
        self.speed = 1.75

        if image == 'enemy':
            self.value = 100
        elif image == 'enemy_blue':
            self.value = 200
        elif image == 'enemy_red': 
            self.value = 300

    def define_alvo_y(self, novo_y):
        self.alvo_y = novo_y

    def update(self,direction):
        if self.rect.y < self.alvo_y:
            self.rect.y += self.speed
        elif self.rect.y > self.alvo_y:
            self.rect.y -= self.speed

        self.rect.x += direction
