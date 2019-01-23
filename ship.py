import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """"初始化飞船位置并设置其初始位置"""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储最小数值
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed_factor
            # self.rect.centerx+=1
        if self.moving_left and self.rect.left > 0:
            self.center1 -= self.ai_settings.ship_speed_factor
            # self.rect.centerx-=1
        if self.moving_up and self.rect.top > self.screen_rect.top:  # 为什么是大于号
            self.center2 -= self.ai_settings.ship_speed_factor
            # self.rect.bottom-=1     注意坐标是从顶端开始
        if self.moving_down and self.rect.bottom < 700:  # ?????应该用什么表示
            self.center2 += self.ai_settings.ship_speed_factor
            # self.rect.bottom+=1

        # 根据self.center更新rect对象
        self.rect.centerx = self.center1
        self.rect.bottom = self.center2

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center1= self.screen_rect.centerx
        self.center2 = self.screen_rect.bottom

