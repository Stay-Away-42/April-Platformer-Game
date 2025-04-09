import pygame
pygame.init()
pygame.display.set_caption("Platformer game")
Game_Screen = pygame.display.set_mode((1000, 600))
Tick_Speed = pygame.time.Clock()
Time = 0
Playing_Game = True

class Player:
    def __init__(self):
        self.HP = 100
        self.light = 100
        self.ST = 1
        self.X_Pos = 400
        self.Y_Pos = 400
        self.Width = 60
        self.Height = 60
        self.X_Vol = 0
        self.Y_Vol = 0
        self.MoveLeft = False
        self.MoveRight = False
        self.jumpnum = 2
        self.OnGround = False
    def Input(self, Key1, Key2, Key3):
        if event.type == pygame.KEYDOWN:
            if event.key == Key1:
                self.MoveLeft = True
            elif event.key == Key2:
                self.MoveRight = True
            elif event.key == Key3:
                self.Jump()
        elif event.type == pygame.KEYUP:
            if event.key == Key1:
                self.MoveLeft = False
            elif event.key == Key2:
                self.MoveRight = False
    def Jump(self):
         if self.OnGround == True or self.jumpnum > 0:
            self.Y_Vol -= 5
            print("jump")
            if self.OnGround == False:
                self.jumpnum -= 1
            self.OnGround = False
    def Physics(self):
        if self.Y_Pos + self.Height >= 550:
            self.OnGround = True
            self.jumpnum = 2
        else:
            self.OnGround = False
        if self.MoveLeft:
            self.X_Vol = -3
        elif self.MoveRight:
            self.X_Vol = 3
        else:
            self.X_Vol = 0
        if self.OnGround == False:
            self.Y_Vol += .1
        elif self.OnGround == True and self.Y_Vol > 0:
            self.Y_Vol = 0
        self.X_Pos += self.X_Vol
        self.Y_Pos += self.Y_Vol
    def Draw(self):
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos, self.Y_Pos, self.Width, self.Height))

player = Player()

while Playing_Game:
    Tick_Speed.tick(60)
    Time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
        player.Input(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
    player.Physics()
    Game_Screen.fill((0, 0, 0))
    pygame.draw.rect(Game_Screen, (100, 100, 100), (0, 550, 1000, 50))
    player.Draw()
    pygame.display.flip()
    
pygame.quit
