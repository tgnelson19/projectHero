###
# Import List
###
import pygame
from classes.card import Card

###
# Window Initializers
###
pygame.init() #Initializes a window

sW, sH = 500, 1000 #Determines (s)creen (W)idth, and (s)creen (H)eigth
screen = pygame.display.set_mode([sW, sH]) #Makes a screen that's that wide

clock = pygame.time.Clock() #Main time keeper

done = False #Determines if the game is over or not

lane1 = pygame.Rect(20, 20, 100, 750)
lane2 = pygame.Rect(140, 20, 100, 750)
lane3 = pygame.Rect(260, 20, 100, 750)
lane4 = pygame.Rect(380, 20, 100, 750)

laneList = [lane1, lane2, lane3, lane4]

cardSpotTopLane1 = pygame.Rect(30, 30, 80, 100)
cardSpotTopLane2 = pygame.Rect(150, 30, 80, 100)
cardSpotTopLane3 = pygame.Rect(270, 30, 80, 100)
cardSpotTopLane4 = pygame.Rect(390, 30, 80, 100)
cardSpotBottomLane1 = pygame.Rect(30, 660, 80, 100)
cardSpotBottomLane2 = pygame.Rect(150, 660, 80, 100)
cardSpotBottomLane3 = pygame.Rect(270, 660, 80, 100)
cardSpotBottomLane4 = pygame.Rect(390, 660, 80, 100)

cardPlacementSlotList = [cardSpotTopLane1, cardSpotTopLane2,cardSpotTopLane3,cardSpotTopLane4,cardSpotBottomLane1,cardSpotBottomLane2,cardSpotBottomLane3,cardSpotBottomLane4]

testingCard = Card()


while not done: #While the game hasn't been closed

    for event in pygame.event.get(): #Main event handler

        if event.type == pygame.QUIT: #If the quit button is pressed
            done = True #Close the entire program

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.MOUSEBUTTONDOWN:
                testingCard.cardGrabbed(screen)
                    




    for lane in laneList:
        pygame.draw.rect(screen,(100,100,100), lane) 

    for cardSlot in cardPlacementSlotList:
        pygame.draw.rect(screen,(20,20,20), cardSlot) 

    testingCard.drawCard(screen)

    pygame.display.flip() #Displays currently drawn frame
    screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
    clock.tick(60) #Keeps screen updated to 60 frames per second