# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 800
HEIGHT = 250
FPS = 30

# define colors
GRAY = (224, 224, 224)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Chrome")
clock = pygame.time.Clock()
road = pygame.image.load("Road/road.png")
font = pygame.font.SysFont("Small Fonts", 20, True)
x = 10
vel =  10
acceleration = 0.0100
score = 0
hitbox = [380, 130, 36, 32]
Restart = True

def Road(screen):
    global rel_x
    if rel_x < WIDTH:
        screen.blit(road, (rel_x, 230))
    screen.blit(road, (rel_x - road.get_rect().width, 230))
    
def GameOver(screen):
    game_over = pygame.image.load("GameOver/GameOver.png")
    button = pygame.image.load("Button/restart.png")
    pygame.draw.rect(screen, (0,0,0), hitbox, 2)
    screen.blit(game_over, (300, 100))
    screen.blit(button, (380, 130) )

def Score(screen):
    HighScore = font.render("HI " + str(score), 1, (0,0,0))
    Score = font.render(str(score), 1, (0,0,0))
    screen.blit(Score, (770, 0))
    screen.blit(HighScore, (700, 0))


class Player():
    def __init__(self):
        self.walk = [pygame.image.load("Dinosaur/Trex1.png"), pygame.image.load("Dinosaur/Trex2.png"), pygame.image.load("Dinosaur/Trex3.png"), pygame.image.load("Dinosaur/Dead.png")]
        self.count = 0
        self.x = 10
        self.y = 200
        self.width = 50
        self.height = 50
        self.jump = False
        self.collision = False
        self.jumpcount = 8
        self.hitbox = [self.x, self.y, self.width, self.height]

    def Draw(self, screen):
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.count += 1
        if not self.collision:
            if self.count + 1 >= 10:
                self.count = 0
            screen.blit(self.walk[self.count // 3], (self.x, self.y))
        else:
            screen.blit(self.walk[3], (self.x, self.y))
            
            


class Cactus():
    def __init__(self, x, vel):
        self.x = x
        self.y = 200
        self.vel = 10
        self.acceleration = 0.0100
        self.setter = 0
        self.width = 50
        self.height = 50
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.images = [pygame.image.load("Obstacles/Obs1.png"), pygame.image.load("Obstacles/Obs2.png"), pygame.image.load("Obstacles/Obs3.png"), pygame.image.load("Obstacles/Obs4.png"), pygame.image.load("Obstacles/Obs5.png"), pygame.image.load("Obstacles/Obs66.png")]

    def Draw(self, screen):
        self.x -= self.vel
        self.vel += self.acceleration
        self.hitbox = [self.x, self.y, self.width, self.height]
        screen.blit(self.images[self.setter], (self.x, self.y))
        if self.x < 0:
            self.setter += 1
            self.x = WIDTH
            if self.setter > 5:
                self.setter = 0

    def Colliding(self):
        global rel_x
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                    player.collision = True   
                    self.vel = 0 
                    rel_x = 0 
    


                    





player = Player()
cactus = Cactus(450, 5)










# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            
        

    # Update
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        player.jump = True
        if player.collision:
            player.jump = False
    


    if player.jump:
        if player.jumpcount >= -8:
            neg = 1
            if player.jumpcount < 0:
                neg = -1
            player.y -= (player.jumpcount ** 2) * 0.5 * neg
            player.jumpcount -= 1
        else:
            player.jump = False
            player.jumpcount = 8

    vel += acceleration
    x -= vel
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if not player.collision:
        score += 1
        rel_x = x % road.get_rect().width
    
    



    # Draw / render
    screen.fill(GRAY)
    player.Draw(screen)
    cactus.Draw(screen)
    cactus.Colliding()
    Score(screen)
    Road(screen)
    print(cactus.x)
    if player.collision:
        GameOver(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()