import pygame

class Card():

    def __init__(self):
        self.health = 20
        self.attack = 15
        
        self.posX = 250
        self.posY = 900
        self.moving = False
        self.offsetX = 0
        self.offsetY = 0

        

        self.isPlayerCard = True

        self.font = pygame.font.Font('media/freeFont.otf', 15)

        self.healthText= self.font.render(str(self.health), True, (0,255,0))
        self.attackText= self.font.render(str(self.attack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()

        self.healthRect.topleft = (self.posX, self.posY + 20)
        self.attackRect.topright = (self.posX + 60, self.posY + 20)

        self.cardColor = (0,0,255)
        self.cardBody = pygame.Rect(self.posX + 10, self.posY + 25, 60, 60)

        self.cardBackgroundColor = (50,50,50)
        self.cardBackgroundBody = pygame.Rect(self.posX, self.posY, 80, 100)

    def drawCard(self, screen):

        pygame.draw.rect(screen, self.cardBackgroundColor, self.cardBackgroundBody)
        pygame.draw.rect(screen, self.cardColor, self.cardBody)
        
        screen.blit(self.healthText, self.healthRect)
        screen.blit(self.attackText, self.attackRect)

    def cardGrabbed(self, screen):
        mouseX, mouseY = pygame.mouse.get_pos()

        if (self.cardBackgroundBody.collidepoint(mouseX, mouseY)):

            if not self.moving:
                self.moving = True
                self.offsetX = mouseX - self.cardBackgroundBody.left
                self.offsetY = mouseX - self.cardBackgroundBody.left

            self.posX, self.posY = (mouseX + self.offsetX, mouseY + self.offsetY)



        