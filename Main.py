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
        self.light = 300
        self.STM = 1
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
        self.sprint = False
        self.lastmove = "N"
        self.crouch = False
    def Input(self, Key1, Key2, Key3, Key4, Key5, Key6, Key7, Key8):
        if event.type == pygame.KEYDOWN:
            if event.key == Key1:
                self.MoveLeft = True
            elif event.key == Key2:
                self.MoveRight = True
            elif event.key == Key3:
                self.Jump()
            elif event.key == Key4:
                self.sprint = True
            elif event.key == Key5:
                self.dash()
            elif event.key == Key6:
                self.crouch = True
                self.grounding()
                self.Y_Pos += 30
            elif event.key == Key7:
                self.sideattack()
        elif event.type == pygame.KEYUP:
            if event.key == Key1:
                self.MoveLeft = False
            elif event.key == Key2:
                self.MoveRight = False
            elif event.key == Key4:
                self.sprint = False
            elif event.key == Key6:
                self.crouch = False
                self.Y_Pos -= 30
    def Jump(self):
         if self.OnGround == True or self.jumpnum > 0:
            self.Y_Vol = -5
            if self.OnGround == False:
                self.jumpnum -= 1
            self.OnGround = False
    def dash(self):
        if self.STM != 0:
            print(self.lastmove)
            self.STM += -1
            print(self.STM)
            if self.lastmove == "R":
                self.X_Vol += 50
            elif self.lastmove == "L":
                self.X_Vol += -50
    def grounding(self):
        if self.OnGround == False:    
            self.Y_Vol += 10
            pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X_Pos - 10, self.Y_Pos + 45, 80, 15)) # update after platforms
    def sideattack(self):
        if self.lastmove == "R":
            pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X_Pos + 60, self.Y_Pos, 25, 60))
        if self.lastmove == "L":
            pygame.draw.rect(Game_Screen, (255, 255, 255), (self.X_Pos - 25 , self.Y_Pos, 25, 60))

    def Physics(self):
        if self.Y_Pos + self.Height >= 550:
            self.OnGround = True
            self.jumpnum = 2
            self.STM = 3
            
        else:
            self.OnGround = False
        if self.MoveLeft:
            if self.sprint == True and self.crouch != True:
                self.X_Vol = -6
            elif self.crouch == True:
                self.X_Vol = -1.5
            else:
                self.X_Vol = -3
            self.lastmove = "L"
        elif self.MoveRight:
            if self.sprint == True and self.crouch != True:
                self.X_Vol = 6
            elif self.crouch == True:
                self.X_Vol = 1.5
            else:
                self.X_Vol = 3
            self.lastmove = "R"
        else:
            self.X_Vol = 0
        if self.OnGround == False:
            self.Y_Vol += .1
        elif self.OnGround == True and self.Y_Vol > 0:
            self.Y_Vol = 0
            self.Y_Pos = 550 - self.Height
        self.X_Pos += self.X_Vol
        self.Y_Pos += self.Y_Vol
    
    def UI(self):
        pygame.draw.rect(Game_Screen, (255, 255, 255), (0, 5, 300, 30))
        pygame.draw.rect(Game_Screen, (200, 0, 0), (0, 40, self.HP, 10))
        if self.STM == 1:
            pygame.draw.rect(Game_Screen, (0, 200, 0), (0, 55, 30, 10))
        elif self.STM == 2:
            pygame.draw.rect(Game_Screen, (0, 200, 0), (0, 55, 30, 10))
            pygame.draw.rect(Game_Screen, (0, 200, 0), (35, 55, 30, 10))
        elif self.STM == 3:
            pygame.draw.rect(Game_Screen, (0, 200, 0), (0, 55, 30, 10))
            pygame.draw.rect(Game_Screen, (0, 200, 0), (35, 55, 30, 10))
            pygame.draw.rect(Game_Screen, (0, 200, 0), (70, 55, 30, 10))
    
    def Draw(self):
        if self.crouch == True:
            self.Height = 30
        else:
            self.Height = 60
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos, self.Y_Pos, self.Width, self.Height))
        

player = Player()

while Playing_Game:
    Tick_Speed.tick(60)
    Time += 1
    Game_Screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
        player.Input(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_z, pygame.K_x, pygame.K_DOWN, pygame.K_c, pygame.K_f)
    player.Physics()
    pygame.draw.rect(Game_Screen, (100, 100, 100), (0, 550, 1000, 50))
    player.UI()
    player.Draw()
    pygame.display.flip()
    
pygame.quit
