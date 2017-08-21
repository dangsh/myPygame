import pygame
import sys

size = width , height = 600 , 400
bg = (0 , 0 , 0);
speed = [2 , 1]

clock = pygame.time.Clock();


pygame.init();

screen = pygame.display.set_mode(size);

pygame.display.set_caption("第一个游戏");

wuKong = pygame.image.load("kong.jpg");

# position = wuKong.get_rect();
position = 0;
print(position);

# f = open("eventLog.txt" , "w");

font = pygame.font.Font(None , 20);
lineheight = font.get_linesize();

while True:
    for event in pygame.event.get():
        
        eventStr = str(event);

        fontSurface = font.render(eventStr , True , (0 , 255 , 0));

        screen.blit(fontSurface , (0 , position));

        position += lineheight;

        if position > height:
            position = 0;
            screen.fill(bg);

        if event.type == pygame.QUIT:
            print("用户要退出游戏。。。。");
            sys.exit();


    # screen.fill(bg);
    # screen.blit(wuKong , position);
    
    pygame.display.flip();
    # pygame.time.delay(500);
    clock.tick(100);

