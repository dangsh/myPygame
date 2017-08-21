import pygame
import sys

size = width , height = 600 , 400

bg=(255,255,255);
speed=[2,1];

clock=pygame.time.Clock();

pygame.init();

screen = pygame.display.set_mode(size);

pygame.display.set_caption("第一个游戏");

wuKong = pygame.image.load("5.jpg");

position = wuKong.get_rect();

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # print("用户要退出游戏。。。");
            sys.exit();

        

    position = position.move(speed);

    if position.left<=0 or position.right>=width:
        wuKong = pygame.transform.flip(wuKong,True,False);
        speed[0]=-speed[0]

    if position.top<=0 or position.bottom>=height:
        speed[1]= -speed[1]

    screen.fill(bg);
    screen.blit(wuKong,position);
    pygame.display.flip();
    # pygame.time.delay(10);
    clock.tick(100);



