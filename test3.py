import pygame
import sys

pygame.init();

WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)

size=width,height=600,400;
screen=pygame.display.set_mode(size);
pygame.display.set_caption("基本图像");


music = pygame.mixer.music.load("longzhu.mp3");
music.play();

clock=pygame.time.Clock();

position=(300,300);
moving = False;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                moving = True;
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button ==1:
                moving = False;

        if moving:
            position = pygame.mouse.get_pos();
    #开始画
    screen.fill(WHITE);

    # pygame.draw.rect(screen,BLACK,(50,50,100,50),1);
    # pygame.draw.ellipse(screen,BLACK,(50,150,100,50),1);
    # pygame.draw.ellipse(screen,BLACK,(50,250,50,50),1);
    
    pygame.draw.circle(screen,RED,position,30,1);
    pygame.draw.circle(screen,RED,position,60,1);
    pygame.draw.circle(screen,RED,position,90,1);

    pygame.display.flip();#更新所有对象到屏幕上
    clock.tick(300);