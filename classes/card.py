import pygame

class Card():
        
    def __init__(self, HP= 20, ATT= 15, PX= 200, PY= 800, R= 0, G= 0, B= 255): #Parameterized CONSTRUCTOR
        
        ##
        # Basic attributes for each card
        ##
        self.health = HP
        self.attack = ATT
        
        self.posX = PX
        self.posY = PY

        self.slotTheCardIsIn = "NA"
        
        ##
        # Asthetic Attributes for the card
        ##
        
        self.RGB = (R, G, B)
        self.fontSize = 15
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)

        self.cardSlotPositions = [(20,30), (140,30), (260,30), (380, 30), (20,660), (140,660), (260,660), (380, 660)]
        
        self.cardBackgroundColor = (50,50,50) #Grey background color
        
        self.defaultCardWidth = 80
        self.defaultCardHeight = 100
        self.defaultCardInsertWidth = 60

        self.cardWidth = 80
        self.cardHeight = 100
        self.cardInsertWidth = 60
        
        self.xOff = 0
        self.yOff = 0
        
        self.healthText = self.font.render(str(self.health), True, (0,255,0))
        self.attackText = self.font.render(str(self.attack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()
        
        self.healthRect.topleft = (self.posX + 5, self.posY + self.fontSize - 12)
        self.attackRect.topright = (self.posX + self.cardWidth - 5, self.posY + self.fontSize - 12)
        
        self.cardBody = pygame.Rect(self.posX + ((self.cardWidth - self.cardInsertWidth) / 2), self.posY + 25, self.cardInsertWidth, self.cardInsertWidth)
        self.cardBackgroundBody = pygame.Rect(self.posX, self.posY, self.cardWidth, self.cardHeight)

    def updateCard(self):

        self.healthText = self.font.render(str(self.health), True, (0,255,0))
        self.attackText = self.font.render(str(self.attack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()
        
        self.healthRect.topleft = (self.posX + 5- self.xOff, self.posY + self.fontSize - 12 - self.yOff)
        self.attackRect.topright = (self.posX + self.cardWidth - 5 - self.xOff, self.posY + self.fontSize - 12- self.yOff)
        
        self.cardBody = pygame.Rect(self.posX + ((self.cardWidth - self.cardInsertWidth) / 2) - self.xOff, self.posY + 25 - self.yOff, self.cardInsertWidth, self.cardInsertWidth)
        self.cardBackgroundBody = pygame.Rect(self.posX - self.xOff, self.posY- self.yOff, self.cardWidth, self.cardHeight)



    def drawCard(self, screen):

        pygame.draw.rect(screen, self.cardBackgroundColor, self.cardBackgroundBody)
        pygame.draw.rect(screen, self.RGB, self.cardBody)
        
        screen.blit(self.healthText, self.healthRect)
        screen.blit(self.attackText, self.attackRect)



    def cardMovementHandler(self, mouseDown, cardsOnTheField):
        
        mouseX, mouseY = pygame.mouse.get_pos()

        global currentHeldCard
        
        if not mouseDown:
            for pos in self.cardSlotPositions:
                if self.cardBackgroundBody.collidepoint(pos[0] + (self.cardWidth / 2), pos[1] + (self.cardHeight / 2)):
                    self.posX = pos[0] + 10
                    self.posY = pos[1] 

                    try:
                        cardsOnTheField[cardsOnTheField.index(self)] = 0
                        cardsOnTheField[self.cardSlotPositions.index(pos)] = self
                    except ValueError:
                        cardsOnTheField[self.cardSlotPositions.index(pos)] = self

            if self.cardBackgroundBody.collidepoint(500 + (self.cardWidth / 2), 660 + (self.cardHeight / 2)):
                del self
                return 0

            currentHeldCard = 0 #If mouse is not down, not holding any card

        elif currentHeldCard != 0:
            currentHeldCard.posX = mouseX - (self.cardWidth / 2)
            currentHeldCard.posY = mouseY - (self.cardHeight / 2)
        
        if (self.cardBackgroundBody.collidepoint(mouseX, mouseY) and ((currentHeldCard == 0) or (currentHeldCard == self))):
            
            self.cardWidth = self.defaultCardWidth * 1.25
            self.cardHeight = self.defaultCardHeight * 1.2 
            self.cardInsertWidth = self.defaultCardInsertWidth * 1.2
            
            self.xOff = self.defaultCardWidth / 10  + 2
            self.yOff = self.defaultCardHeight / 10

            if (mouseDown): #If card is clicked 
                currentHeldCard = self
            
        else:
            
            self.cardWidth = self.defaultCardWidth
            self.cardHeight = self.defaultCardHeight
            self.cardInsertWidth = self.defaultCardInsertWidth
            
            self.xOff = 0
            self.yOff = 0      
            
        


        