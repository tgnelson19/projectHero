###
# Import List
###
import pygame
from classes.card import Card
from classes.background import Background
from classes.variables import Variables
from classes.buttons import Buttons

###
# Window Initializers
###

pygame.init() #Initializes a window

vars = Variables()

screen = pygame.display.set_mode([vars.sW, vars.sH]) #Makes a screen that's that wide

currentHeldCard = 0

newCard = Card()

cardList = [ newCard]

cardMakerButton = Buttons(500, 520, 100, 120, 0, 200, 0, "Make", 15, 0,0,0)

battlerButton = Buttons(650, 550, 100, 50, 200, 100, 0, "Battle", 15, 0,0,0)

healthUpButton = Buttons(500, 250, 25, 25,0,255,0,"^", 20,0,0,0)
healthDownButton = Buttons(535, 250, 25, 25,255,0,0,"v", 20,0,0,0)
attackUpButton = Buttons(600, 250, 25, 25,0,255,0,"^", 20,0,0,0)
attackDownButton = Buttons(635, 250, 25, 25,255,0,0,"v", 20,0,0,0)

tempEdmg = 0
tempPdmg = 0

buttonList = [cardMakerButton, battlerButton, healthUpButton, healthDownButton, attackUpButton,attackDownButton]

testingBackground = Background() #Basic background helper

cardsOnTheField = [0,0,0,0,0,0,0,0]

while not vars.done: #While the game hasn't been closed (Main loop of the game, determines what is done each frame)

    tempEdmg = 0
    tempPdmg = 0

    testingBackground.drawBackground(screen)

    vars.eventHandler()

    if healthUpButton.isClicked(vars.mouseDown):
        vars.tempHealth += 1
    if healthDownButton.isClicked(vars.mouseDown):
        vars.tempHealth -= 1
    if attackUpButton.isClicked(vars.mouseDown):
        vars.tempAttack += 1
    if attackDownButton.isClicked(vars.mouseDown):
        vars.tempAttack -= 1
    
    vars.updateHealthAttackAndUpdate(screen)



    for button in buttonList:
        button.isHoveredOver()
        button.drawButton(screen)

    if cardMakerButton.isClicked(vars.mouseDown):
        newCard = Card(vars.tempHealth, vars.tempAttack, 200, 800, 0, 0, 255)
        cardList.append(newCard)


    if len(cardList) != 0:
        for card in cardList:
            card.updateCard() 
            card.drawCard(screen)
            if card.cardMovementHandler(vars.mouseDown, cardsOnTheField) == 0:
                cardList.remove(card)
                del card

    if battlerButton.isClicked(vars.mouseDown):

        for i in range(4):
            if cardsOnTheField[i] != 0:
                if cardsOnTheField[i+4] == 0:
                    tempEdmg += cardsOnTheField[i].attack
                else:
                    cardsOnTheField[i].health -= cardsOnTheField[i+4].attack

                    
        for i in range(4):
            if cardsOnTheField[i+4] != 0:
                if cardsOnTheField[i] == 0:
                    tempPdmg += cardsOnTheField[i+4].attack
                else:
                    cardsOnTheField[i+4].health -= cardsOnTheField[i].attack
                   
        for i in range(8):
            if cardsOnTheField[i] != 0:
                if cardsOnTheField[i].health <= 0:
                    card = cardsOnTheField[i]
                    cardList.remove(cardsOnTheField[i])
                    cardsOnTheField[i] = 0
                    del card
    
    vars.updatePlayerAndEnemyHealth(screen, tempEdmg, tempPdmg)

    pygame.display.flip() #Displays currently drawn frame
    screen.fill(pygame.Color(0,0,0)) #Clears screen with a black color
    vars.clock.tick(60) #Keeps screen updated to 60 frames per second