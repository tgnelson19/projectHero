import pygame

class Card():
        
    def __init__(self, HP= 20, ATT= 15, PX= 250, PY= 900, R= 0, G= 0, B= 255): #Parameterized CONSTRUCTOR
        
        ##
        # Basic attributes for each card
        ##
        self.health = HP
        self.attack = ATT
        
        self.posX = PX
        self.posY = PY
        
        
        ##
        # Asthetic Attributes for the card
        ##
        
        self.RGB = (R, G, B)
        self.fontSize = 15
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)
        
        self.cardBackgroundColor = (50,50,50) #Grey background color
        
        self.cardWidth = 80
        self.cardHeight = 100
        
        self.cardInsertWidth = 60
        self.cardInsertHeight = 60
        
        self.xOff = 0
        self.yOff = 0
        
        self.healthText = self.font.render(str(self.health), True, (0,255,0))
        self.attackText = self.font.render(str(self.attack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()
        
        self.healthRect.topleft = (self.posX + 5, self.posY + self.fontSize - 12)
        self.attackRect.topright = (self.posX + self.cardWidth - 5, self.posY + self.fontSize - 12)
        
        self.cardBody = pygame.Rect(self.posX + ((self.cardWidth - self.cardInsertWidth) / 2), self.posY + 25, self.cardInsertWidth, self.cardInsertHeight)
        self.cardBackgroundBody = pygame.Rect(self.posX, self.posY, self.cardWidth, self.cardHeight)

    def updateCard(self):
        
        self.healthRect.topleft = (self.posX + 5- self.xOff, self.posY + self.fontSize - 12- self.yOff)
        self.attackRect.topright = (self.posX + self.cardWidth - 5- self.xOff, self.posY + self.fontSize - 12- self.yOff)
        
        self.cardBody = pygame.Rect(self.posX + ((self.cardWidth - self.cardInsertWidth) / 2)- self.xOff, self.posY + 25- self.yOff, self.cardInsertWidth, self.cardInsertHeight)
        self.cardBackgroundBody = pygame.Rect(self.posX - self.xOff, self.posY- self.yOff, self.cardWidth, self.cardHeight)
        

    def drawCard(self, screen):

        pygame.draw.rect(screen, self.cardBackgroundColor, self.cardBackgroundBody)
        pygame.draw.rect(screen, self.RGB, self.cardBody)
        
        screen.blit(self.healthText, self.healthRect)
        screen.blit(self.attackText, self.attackRect)
        
    def mouseClicked(self, mouseX, mouseY):
        
        self.posX = mouseX - (self.cardWidth / 2)
        self.posY = mouseY - (self.cardHeight / 2)


        