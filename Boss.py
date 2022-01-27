import pygame


class Boss:
    def __init__(self, level):
        self.level = level
        self.gold = level * 2
        self.heal = level * 2
        self.font = pygame.font.SysFont('arial', 30)
        self.block_picture = self.font.render(str(level), False, (0, 180, 0))
        self.block_pos = (block_pos + 30, 30)
        self.picture = pygame.image.load('img/boss.jpg')
        self.pos = (100, 100)

    def draw_block(self, screen):
        screen.blit(self.block_picture, self.pos)