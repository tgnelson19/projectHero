import pygame

class Background():
    
    def __init__(self):
        
        self.lane1 = pygame.Rect(20, 20, 100, 750)
        self.lane2 = pygame.Rect(140, 20, 100, 750)
        self.lane3 = pygame.Rect(260, 20, 100, 750)
        self.lane4 = pygame.Rect(380, 20, 100, 750)

        self.laneList = [self.lane1, self.lane2, self.lane3, self.lane4]

        self.cardSpotTopLane1 = pygame.Rect(30, 30, 80, 100)
        self.cardSpotTopLane2 = pygame.Rect(150, 30, 80, 100)
        self.cardSpotTopLane3 = pygame.Rect(270, 30, 80, 100)
        self.cardSpotTopLane4 = pygame.Rect(390, 30, 80, 100)
        self.cardSpotBottomLane1 = pygame.Rect(30, 660, 80, 100)
        self.cardSpotBottomLane2 = pygame.Rect(150, 660, 80, 100)
        self.cardSpotBottomLane3 = pygame.Rect(270, 660, 80, 100)
        self.cardSpotBottomLane4 = pygame.Rect(390, 660, 80, 100)

        self.cardPlacementSlotList = [self.cardSpotTopLane1, self.cardSpotTopLane2,self.cardSpotTopLane3,self.cardSpotTopLane4,self.cardSpotBottomLane1,self.cardSpotBottomLane2,self.cardSpotBottomLane3,self.cardSpotBottomLane4]
        
    def drawBackground(self,screen):
        for lane in self.laneList:
            pygame.draw.rect(screen,(100,100,100), lane) 

        for cardSlot in self.cardPlacementSlotList:
            pygame.draw.rect(screen,(20,20,20), cardSlot) 