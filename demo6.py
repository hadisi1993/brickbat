import pygame,sys,time,random
from pygame.locals import *		#
from static_params import *   #引入所有静态参数
from GameClass import *


pygame.init()
mainclock = pygame.time.Clock() #时钟设置

windowScreen = pygame.display.set_mode([WindowWidth,WindowHeight],0,32) #窗口设置
print(type(pygame.display),type(pygame.display))
pygame.display.set_caption('打砖块游戏')    #设置窗口标题

StartImage = pygame.image.load('intro_ball.png').convert_alpha() #开始图像的界面
Font1 =pygame.font.SysFont('宋体',60).render('StartGame',1,(255,0,0))
windowScreen.fill((0,0,0))
while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			pygame.quit()
			exit()
		if event.type == MOUSEBUTTONUP:
			ex,ey = pygame.mouse.get_pos()
			if ex>200 and ex<404 and ey>290 and ey<330:
				pygame.quit()
				exit()
	
	windowScreen.blit(StartImage,(WindowWidth/2-60,WindowHeight/2-90))
	windowScreen.blit(Font1,(WindowWidth/2-120,WindowHeight/2+50))
	pygame.display.update()
	mainclock.tick(100)