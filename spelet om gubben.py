
import pygame
import random
from gubben import Gubbe
from svartapricken import Prick
from spöket import Spöke
import time

WHITE = (0, 0, 255)
score = 0
scorespöke = 0
pygame.init()
screen = pygame.display.set_mode([800, 600])
def utskrift(voffvoff,x,y):
    f = pygame.font.Font("arial.ttf", 32)
    surf = f.render(voffvoff,1,(255,255,255))
    screen.blit(surf,[x,y])


pygame.display.set_caption('Gubbe vs. spöke!')
player = Gubbe(0,0)
spöke = Spöke(0,0)
prick = Prick(random.randint(0,800),random.randint(0,590))
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(prick)
all_sprites_list.add(spöke)
prick_list = pygame.sprite.Group()
prick_list.add(prick)
clock = pygame.time.Clock()
more = True
while more:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            more = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not player.left:
                    player.image = pygame.transform.flip(player.image, True, False)
                    player.left = True
                if player.rect.x > 0:
                    player.rect.x -= player.rect.width
            elif event.key == pygame.K_RIGHT:
                if  player.rect.x + player.rect.width < 800:
                    player.rect.x += player.rect.width
                if player.left:
                    player.image = pygame.transform.flip(player.image, True, False)
                    player.left = False
            elif event.key == pygame.K_UP:
                player.rect.y -= player.rect.height
                if player.rect.y < 0:
                    player.rect.y += player.rect.height
            elif event.key == pygame.K_DOWN:
                player.rect.y += player.rect.height
                if player.rect.y > 590:
                    player.rect.y -= player.rect.height
            elif event.key == pygame.K_w:
                spöke.upp()
            elif event.key == pygame.K_s:
                spöke.ner()
            elif event.key == pygame.K_d:
                spöke.höger()
            elif event.key == pygame.K_a:
                spöke.vänster()
            
                
    krock_list = pygame.sprite.spritecollide(player, prick_list, True)
    for krock in krock_list:
        score +=1
        krock.rect.x = random.randint(10,790)
        krock.rect.y = random.randint(10,590)
        all_sprites_list.add(krock)
        prick_list.add(krock)
    krock_list_spöke = pygame.sprite.spritecollide(spöke, prick_list, True)
    for krockspöke in krock_list_spöke:
        scorespöke +=1
        krockspöke.rect.x = random.randint(10,790)
        krockspöke.rect.y = random.randint(10,590)
        all_sprites_list.add(krockspöke)
        prick_list.add(krockspöke)
        pygame.display.flip()
        
    screen.fill(WHITE)
    utskrift("Gubben: " + str(score), 0, 0)
    utskrift("Spöket: " + str(scorespöke),0,500)
    all_sprites_list.draw(screen)
    pygame.display.flip()

    clock.tick(40)
    if scorespöke > 14 or score > 14:
        if scorespöke > 14:
            utskrift("Spöket vann!", 400, 300)
        if score > 14:
            utskrift("Gubben vann!", 400, 300)
        all_sprites_list.draw(screen)
        pygame.display.flip()
        time.sleep(2)
        more = False

pygame.quit()

