import pygame

class Buttons():

    def __init__(self, topLeft, topRight, width, height, R, G, B):
        self.buttonRect = pygame.Rect(topLeft, topRight, width, height)
        self.buttonRGB = (R,G,B)
        self.canBeClickedAgain = True

    def drawButton(self, screen):
        pygame.draw.rect(screen,self.buttonRGB, self.buttonRect) 

    def isClicked(self, mouseDown):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseDown:
            if self.buttonRect.collidepoint(mouseX,mouseY) and self.canBeClickedAgain:
                self.canBeClickedAgain = False
                return True
        else:
            self.canBeClickedAgain = True
            return False