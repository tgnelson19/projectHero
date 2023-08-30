import pygame

class Variables():

    def __init__(self):
        self.sW, self.sH = 800, 950 #Determines (s)creen (W)idth, and (s)creen (H)eigth

        self.clock = pygame.time.Clock() #Main time keeper

        self.done = False #Determines if the game is over or not
        self.mouseDown = False

        self.tempAttack = 1
        self.tempHealth = 1

        self.fontSize = 30
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)
        
        self.healthText = self.font.render(str(self.tempHealth), True, (0,255,0))
        self.attackText = self.font.render(str(self.tempAttack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()

        

    def eventHandler(self):
        for event in pygame.event.get(): #Main event handler

            if event.type == pygame.QUIT: self.done = True #Close the entire program

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: self.done = True
                
            if event.type == pygame.MOUSEBUTTONDOWN: self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP: self.mouseDown = False

    def updateHealthAttackAndUpdate(self, screen):

        self.healthText = self.font.render(str(self.tempHealth), True, (0,255,0))
        self.attackText = self.font.render(str(self.tempAttack), True, (255,0,0))

        self.healthRect = self.healthText.get_rect()
        self.attackRect = self.attackText.get_rect()

        self.healthRect.topleft = (510, 300 + self.fontSize - 20)
        self.attackRect.topright = (650, 300 + self.fontSize - 20)

        screen.blit(self.healthText, self.healthRect)
        screen.blit(self.attackText, self.attackRect)