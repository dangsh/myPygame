import pygame
import sys

size = width , height = 600 , 400

bg=(255,255,255);
speed=[5,3];

clock=pygame.time.Clock();

pygame.init();

screen = pygame.display.set_mode(size,pygame.RESIZABLE);

pygame.display.set_caption("第一个游戏");

wuKong = pygame.image.load("4.jpg");

fullScreen=False;

l_head=wuKong;
l_right=pygame.transform.flip(wuKong,True,False);

position = wuKong.get_rect();

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # print("用户要退出游戏。。。");
            sys.exit();

        if event.type == pygame.VIDEORESIZE:
            #屏幕大小发生改变
            size=event.size;
            width,height=size;
            screen =pygame.display.set_mode(size,pygame.RESIZABLE);

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wuKong=l_head;
                speed = [-5,0];

            if event.key == pygame.K_RIGHT:
                wuKong=l_right;
                speed = [5,0];
            if event.key == pygame.K_UP:
                speed = [0,-3];
            if event.key == pygame.K_DOWN:
                speed = [0,3];
            if event.key == pygame.K_F7:
                fullScreen = not fullScreen;
                if fullScreen:
                    screen = pygame.display.set_mode(size);
                else:
                    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN|pygame.HWSURFACE);

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



