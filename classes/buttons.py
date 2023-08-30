import pygame

class Buttons():

    def __init__(self, topLeftX, topLeftY, width, height, R, G, B, text, fontSize, textR, textG, textB):
        self.posX = topLeftX
        self.posY = topLeftY

        self.buttonRect = pygame.Rect(topLeftX, topLeftY, width, height)
        self.buttonRGB = (R,G,B)
        self.canBeClickedAgain = True

        self.textRGB = (textR, textG, textB)
        self.text = text
        self.fontSize = fontSize
        self.font = pygame.font.Font('media/freeFont.otf', self.fontSize)
        self.textRender = self.font.render(str(self.text), True, self.textRGB)
        self.textRect = self.textRender.get_rect(center=(self.buttonRect.centerx, self.buttonRect.centery))

    def drawButton(self, screen):
        pygame.draw.rect(screen,self.buttonRGB, self.buttonRect) 
        screen.blit(self.textRender, self.textRect)

    def isClicked(self, mouseDown):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseDown:
            if self.buttonRect.collidepoint(mouseX,mouseY) and self.canBeClickedAgain:
                self.canBeClickedAgain = False
                return True
        else:
            self.canBeClickedAgain = True
            return False