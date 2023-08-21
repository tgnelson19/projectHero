import pygame

class Card():

    def __init__(self):
        
        ##
        # Basic attributes for each card
        ##
        self.health = 20
        self.attack = 15
        self.posX = 250
        self.posY = 900

    def updateCard(self, R, G, B):
        
        self.font = pygame.font.Font('media/freeFont.otf', 15)

        self.healthText= self.font.render(str(self.health), True, (0,255,0))
        self.attackText= self.font.render(str(self.attack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()

        self.healthRect.topleft = (self.posX, self.posY + 20)
        self.attackRect.topright = (self.posX + 60, self.posY + 20)

        self.cardColor = (R,G,B) #easy 
        self.cardBody = pygame.Rect(self.posX + 10, self.posY + 25, 60, 60)

        self.cardBackgroundColor = (50,50,50) 
        self.cardBackgroundBody = pygame.Rect(self.posX, self.posY, 80, 100)
        

    def drawCard(self, screen):

        pygame.draw.rect(screen, self.cardBackgroundColor, self.cardBackgroundBody)
        pygame.draw.rect(screen, self.cardColor, self.cardBody)
        
        screen.blit(self.healthText, self.healthRect)
        screen.blit(self.attackText, self.attackRect)
        
    def mouseClicked(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        
        if (self.cardBackgroundBody.collidepoint(mouseX, mouseY)):
            self.posX = mouseX - 40
            self.posY = mouseY - 50
            print("True")
        else:
            print("False")



        