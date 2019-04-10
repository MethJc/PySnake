import pygame

class Head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Head Setup
        self.image = pygame.Surface((15, 15)) # Create head with 15 width and height
        self.image.fill(BLUE) # Make it blue
        self.rect = self.image.get_rect() # Set the rect to the image rect
        self.rect.center = ((WIDTH / 2, HEIGHT / 2)) #set starting location to middle of the screen
        # Self Variable Setup
        self.vel = 20 # Set the velocity to 20
        self.speedx = -self.vel # Have the head start moving left
        self.speedy = 0 # Have the ehad start without moving up or down
        self.previousDir = None #create previous direction

    def update(self):
        # Moves x and y based off speedx and speedy
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

    def move(self, dir):
        # change the speeds based off what key was pressed, can't turn 180
        if (dir == "UP" and self.previousDir != "DOWN"):
            self.speedx = 0
            self.speedy = -self.vel
            self.previousDir = "UP"
        if (dir == "DOWN" and self.previousDir != "UP"):
            self.speedx = 0
            self.speedy = self.vel
            self.previousDir = "DOWN"
        if (dir == "LEFT" and self.previousDir != "RIGHT"):
            self.speedx = -self.vel
            self.speedy = 0
            self.previousDir = "LEFT"
        if (dir == "RIGHT" and self.previousDir != "LEFT"):
            self.speedx = self.vel
            self.speedy = 0
            self.previousDir = "RIGHT"

    def eat(self):
        global tailSize, tailsX, tailsY
        tailSize += 1 # Add one to tail size
        tailsX.append(self.rect.centerx) # Add a element to tails X
        tailsY.append(self.rect.centery) # Add a element to tails Y
        tailPiece = Tail(tailsX[1], tailsY[1]) # create new tail piece
        tailPieces.add(tailPiece) # Add tail piece to the tail group
