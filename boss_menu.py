import pygame
from Boss import Boss
from level_change import LevelChanger

class BossMenu:
    def __init__(self):
        self.blocks = []
        self.fill_boss_info()


    def fill_boss_info(self):
        for i in range(1, 5):
            self.blocks.append(Boss(i))

    def fill_level_changer(self):
        self.blocks.insert(0, LevelChanger('left'))
        self.blocks.append(LevelChanger('right'))

    def draw_blocks(self, screen):
        for block in self.blocks:
            block.draw_block(screen)


















































































