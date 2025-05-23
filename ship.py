import pygame


class Ship:
    def __init__(self,ai_game):
        self.screen =ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('./snail.bmp')
        #get dim of ship
        self.rect = self.image.get_rect()
        #starts ship atht eh bottom center of the scrren
      
     

        self.settings = ai_game.settings
        self.rect.midbottom =  self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False 
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        #draw the ship at its current location 
        self.screen.blit(self.image,self.rect)
        