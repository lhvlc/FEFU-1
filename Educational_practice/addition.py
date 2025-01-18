import pygame
import sys

def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    rocket = rocket(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        rocket.output()
        pygame.display.flip()
run()
class rocket():
    def __init__(self, screen):
        """инициализация ракеты"""
        self.screen = screen
        self.image = pygame.image.load('images\rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
    def output(self):
        """рисование ракеты"""
        self.screen.blit(self.image, self.rect)
