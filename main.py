###
# Import List
###
import pygame
from classes.card import Card
from classes.background import Background

###
# Window Initializers
###
pygame.init() #Initializes a window

sW, sH = 500, 1000 #Determines (s)creen (W)idth, and (s)creen (H)eigth
screen = pygame.display.set_mode([sW, sH]) #Makes a screen that's that wide

defaultCardWidth = 80
defaultCardHeight = 100

clock = pygame.time.Clock() #Main time keeper

done = False #Determines if the game is over or not
mouseDown = False
currentHeldCard = 0

testingCard = Card() #Basic card helper
greenCard = Card(12, 3, 100, 250, 0, 255, 0)

cardList = [testingCard, greenCard]

testingBackground = Background() #Basic background helper

#playingCardList = [0]*10 #will this work?

while not done: #While the game hasn't been closed (Main loop of the game, determines what is done each frame)

    for event in pygame.event.get(): #Main event handler

        if event.type == pygame.QUIT: done = True #Close the entire program

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: done = True
            
        if event.type == pygame.MOUSEBUTTONDOWN: mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP: mouseDown = False
        
    for card in cardList:
        
        mouseX, mouseY = pygame.mouse.get_pos()
        
        if not mouseDown:
            currentHeldCard = 0
        
        if (card.cardBackgroundBody.collidepoint(mouseX, mouseY) and ((currentHeldCard == 0) or (currentHeldCard == card))):
            
            card.cardWidth = defaultCardWidth * 1.2
            card.cardHeight = defaultCardHeight * 1.2
            
            card.xOff = defaultCardWidth / 10
            card.yOff = defaultCardHeight / 10
            
            if (mouseDown):
                card.mouseClicked(mouseX, mouseY)
                currentHeldCard = card
            
        else:
            
            card.cardWidth = defaultCardWidth
            card.cardHeight = defaultCardHeight
            
            card.xOff = 0
            card.yOff = 0
            
            

    # for card in playingCardList: #draws 10 cards without any variable for them, no arguments for drawcard yet
    #     testingCard.drawCard(screen)

    testingBackground.drawBackground(screen)
    testingCard.updateCard() 
    testingCard.drawCard(screen)
    greenCard.updateCard() 
    greenCard.drawCard(screen)

    pygame.display.flip() #Displays currently drawn frame
    screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
    clock.tick(60) #Keeps screen updated to 60 frames per second