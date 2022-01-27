import pygame
from boss_menu import BossMenu
class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT ))
        self.boss_menu = BossMenu()



    def launch(self):
        while True:
            self.dtaw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.boss_menu.draw_blocks(self.screen)







main = Main()
main.launch()
