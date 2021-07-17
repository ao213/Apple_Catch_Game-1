import pygame
from setting import *
import numpy as np


class Screen:
    def __init__(self):
        # 画像アセットの読み込み
        logo = pygame.image.load(LOGO_IMG)
        self.bg = pygame.image.load(BG_IMG)
        self.bg_hud = pygame.image.load(BG_HUD_IMG)
        self.bg_game_over = pygame.image.load(BG_GAME_OVER_IMG)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # HUDの設定
        self.font = pygame.font.Font(None, 100)
        self.text_color = (127, 195, 156)
        self.line_x = LINE_X

        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(logo)

    def draw_object(self, Object):
        image = pygame.image.load(Object.image)
        self.screen.blit(image, Object.get_pos())

    def draw_base_screen(self):
        self.screen.fill((100, 100, 100))
        self.screen.blit(self.bg, (0, -300))
        self.screen.blit(self.bg_hud, (0, 600))

    def draw_hud(self, player):

        start_line_x = 27
        line_y = 636
        hp_par = np.round(player.get_hp() / MAX_HP, 2)
        end_line_x = int(LINE * hp_par)
        if end_line_x <= start_line_x:
            end_line_x = 28
        text_x = self.__select_x(player.get_point())

        text = self.font.render(str(player.get_point()), True, self.text_color)
        self.screen.blit(text, (text_x, 700))
        pygame.draw.line(self.screen, self.text_color,
                         (start_line_x, line_y), (end_line_x, line_y), 20)

    def draw_game_over_screen(self):
        self.screen.fill((100, 100, 100))
        self.screen.blit(self.bg_game_over, (0, 0))

    def __select_x(self, x):
        if x < 10:
            return 170
        elif x < 100:
            return 150
        elif x < 1000:
            return 130
        else:
            return 140
