# I - IMPORT AND INITIALIZE
import pygame, Mysprites, random
pygame.init()

def main():
    ''' This function defines the 'mainline logic' for our pyTron game'''
    # D - Display configuration
    pygame.display.set_caption("pyTron! v1.0")
    
    # ENTITITIES
    screen = pygame.display.set_mode((960,720))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((111,195,223))
    screen.blit(background,(0,0))
    # Sprites
    player = Mysprites.Player(1,screen)
    player2 = Mysprites.Player(2,screen)
    topwall = Mysprites.TopWall(screen,0)
    botwall = Mysprites.TopWall(screen,1)
    leftwall = Mysprites.SideWall(screen,0)
    rightwall = Mysprites.SideWall(screen,1)
    scoreboard = Mysprites.ScoreKeeper()
    recharges = []
    recharge = pygame.sprite.Group()
    allWalls = pygame.sprite.Group(topwall,botwall,leftwall,rightwall)
    allSprites = pygame.sprite.OrderedUpdates(player,player2,recharge,allWalls,scoreboard)
    
    
    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Loop
    while keepGoing:
        
        # TIME
        clock.tick(30)
        
        # EVENT HANDLING: Player 1 uses the WASD, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_w:
                    player2.go_up()
                if event.key == pygame.K_s:
                    player2.go_down()
                if event.key == pygame.K_a:
                    player2.go_left()
                if event.key == pygame.K_d:
                    player2.go_right()                
                if event.key == pygame.K_f:
                    if scoreboard.get_turbo2() > 0:
                        player2.turbo() 
                        scoreboard.player2_turbo()
                if event.key == pygame.K_l:
                    if scoreboard.get_turbo1() > 0:
                        player.turbo()
                        scoreboard.player1_turbo()
                        
                        
        if random.randint(0,1000) == 7:
            recharges.append(Mysprites.Recharge(screen))
            recharge.add(recharges)
            allSprites.add(recharges)
        if player.rect.colliderect(player2.rect):
            scoreboard.player2_life()
            scoreboard.player1_life()
            player.reset()
            player2.reset()
            background.fill((111,195,223))
            screen.blit(background,(0,0))            
        if pygame.sprite.spritecollide(player,recharge,True):
            scoreboard.player1_getturbo()
        if pygame.sprite.spritecollide(player2,recharge,True):
            scoreboard.player2_getturbo()
                   
            
        for x in range(len(player2.get_pos())-1):
                       
            if player.get_rect() == player2.get_pos()[x]:
                
                scoreboard.player2_life()
                background.fill((111,195,223))
                screen.blit(background,(0,0))                
                player.reset()
                player2.reset() 
                break
            if player2.get_rect() == player2.get_pos()[x]:
                
                scoreboard.player1_life()
                background.fill((111,195,223))
                screen.blit(background,(0,0))                
                player.reset()
                player2.reset() 
                break
        for x in range(len(player.get_pos())-1):
            
            if player.get_rect() == player.get_pos()[x]:
                scoreboard.player2_life()
                background.fill((111,195,223))
                screen.blit(background,(0,0))                
                player.reset()
                player2.reset()
                break
            if player2.get_rect() == player.get_pos()[x]:
                scoreboard.player1_life()
                background.fill((111,195,223))
                screen.blit(background,(0,0))                
                player.reset()
                player2.reset()
                break
        if scoreboard.loser():
            keepGoing = False
                
        # REFRESH SCREEN
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
    # Close the game window
    
    pygame.quit()
    
# Call the main function   
main()