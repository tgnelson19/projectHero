###
# Import List
###
import pygame
from classes.card import Card
from classes.background import Background
from classes.variables import Variables

###
# Window Initializers
###

vars = Variables()

pygame.init() #Initializes a window

screen = pygame.display.set_mode([vars.sW, vars.sH]) #Makes a screen that's that wide

testingCard = Card() #Basic card helper
greenCard = Card(12, 3, 100, 250, 0, 255, 0)

currentHeldCard = 0

cardList = [testingCard, greenCard]

testingBackground = Background() #Basic background helper

while not vars.done: #While the game hasn't been closed (Main loop of the game, determines what is done each frame)

    testingBackground.drawBackground(screen)

    vars.eventHandler()

    for card in cardList:
        card.updateCard() #foreach card would go here instead to get constant updates 
        card.drawCard(screen)
        card.cardMovementHandler(vars.mouseDown)

    pygame.display.flip() #Displays currently drawn frame
    screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
    vars.clock.tick(60) #Keeps screen updated to 60 frames per second