import pygame,random


class Player(pygame.sprite.Sprite):
    
    def __init__(self,player,screen):
        
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.Surface((5,5))
        self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.rect = self.image.get_rect()
        self.__screen = screen
        if player == 1:
            self.rect.center = (self.__screen.get_width()/1.5, self.__screen.get_height()/2)
            self.__dx = -5
            self.__colour = (223,116,12)
        else:
            self.rect.center = (self.__screen.get_width()/6, self.__screen.get_height()/2)
            self.__dx = 5
            self.__colour = (255,230,77)
        self.prev_pos = []  
        self.__dy = 0
        
    def go_up(self):
        if self.__dy == 5:
            self.__dy = self.__dy
        else:
            self.__dy = -5
        self.__dx = 0

    def go_left(self):
        if self.__dx == 5:
            self.__dx = self.__dx
        else:
            self.__dx = -5
        self.__dy = 0
    def go_right(self):
        if self.__dx == -5:
            self.__dx = self.__dx
        else:
            
            self.__dx = 5
        self.__dy = 0
    def go_down(self):
        if self.__dy == -5:
            self.__dy = self.__dy
        else:
            
            self.__dy = 5
        self.__dx = 0
    def get_pos(self):
        return self.prev_pos
    def get_rect(self):
        return self.rect.center
    def turbo(self):
        self.__dx = self.__dx*2
        self.__dy = self.__dy*2
        
    
    def reset(self):
        self.prev_pos = []
        if self.player == 1:
            self.rect.center = (self.__screen.get_width()/1.5, self.__screen.get_height()/2)
            self.__dx = -5
            self.__dy = 0
            self.__colour = (223,116,12)
        else:
            self.rect.center = (self.__screen.get_width()/6, self.__screen.get_height()/2)
            self.__dx = 5
            self.__dy = 0
            self.__colour = (255,230,77)       
        
        
    def update(self):
        self.rect.top += self.__dy
        self.rect.left += self.__dx   
        self.prev_pos.append(self.rect.center)
        if len(self.prev_pos) > 1:
            pygame.draw.aalines(self.__screen,self.__colour,False,self.prev_pos)
        if self.rect.centerx >= self.__screen.get_width()-100 or self.rect.centerx < 110:
            self.__dx = 0
        if self.rect.centery >= self.__screen.get_height()-100 or self.rect.centery < 100:
            self.__dy = 0
        
class ScoreKeeper(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.__font = pygame.font.SysFont("Arial", 26)
        self.__player1_life = 3
        self.__player2_life = 3
        self.__player1_turbo = 3
        self.__player2_turbo = 3
        
    def player1_life(self):
        '''This method takes away a life from the player when it hits the end zone'''
        self.__player1_life -= 1
    
    def loser(self):
        '''When player life reaches zero it will return a 1 to signify that the game is over.'''
        if self.__player1_life <= 0 or self.__player2_life <= 0:
            return 1
        else:
            return 0
    def get_turbo1(self):
        return self.__player1_turbo
    def get_turbo2(self):
        return self.__player2_turbo 
    def player2_life(self):
        self.__player2_life -= 1
    def player1_turbo(self):
        self.__player1_turbo -= 1
    def player2_turbo(self):
        self.__player2_turbo -= 1 
    def player1_getturbo(self):
        self.__player1_turbo += 1
    def player2_getturbo(self):
        self.__player2_turbo += 1        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Player 1 Life: %d     Player 1 Turbo: %d                  Player 2 Life: %d     Player 2 Turbo: %d                    " %(self.__player1_life,self.__player1_turbo,self.__player2_life,self.__player2_turbo)
        self.image = self.__font.render(message, 1, (230,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (485, 50)    
        
class Recharge(pygame.sprite.Sprite):
    
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = pygame.Surface((5,5))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100,self.__screen.get_width()-100),random.randint(100,self.__screen.get_height()-100))
    

        
        
class TopWall(pygame.sprite.Sprite):
    
    def __init__(self,screen,x):
        
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = pygame.Surface((self.__screen.get_width(),100))
        self.image.fill((12,20,31))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        if x == 1:
            
            self.rect.top = self.__screen.get_height()-100
class SideWall(pygame.sprite.Sprite):
    
    def __init__(self,screen,x):
        
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = pygame.Surface((100,self.__screen.get_height()))
        self.image.fill((12,20,31))
        self.rect = self.image.get_rect()
        if x == 1:
            self.rect.left = 0
        else:
            self.rect.left = self.__screen.get_width()-100