import pygame
pygame.init()
screen=pygame.display.set_mode((333,500))
bg=pygame.image.load("img/下载.jpg")
screen.blit(bg,(0,0))
# pygame.display.update()
cxk=pygame.image.load("img/cxk.jpg")
screen.blit(cxk,(150,460))
pygame.display.update()
cxk_rect=pygame.Rect(150,460,20,31)

clock=pygame.time.Clock()
while True:
    cxk_rect.y-=1
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(cxk,cxk_rect)
    pygame.display.update()
pygame.quit()
