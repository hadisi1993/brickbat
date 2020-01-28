import pygame
from pygame import Rect
from pygame.locals import *	
import pygame,sys,time,random

global a
a = Rect(100,100,20,20)

# print(a.center)
# print(a.top,a.left,a.bottom,a.right)
# print(a.size)
# print(a.width,a.height)


pygame.init()   #初始化游戏
windowScreen = pygame.display.set_mode([640,480],0,32) #窗口设置
# print(type(windowScreen))
mainclock = pygame.time.Clock() #时钟设置
#游戏框架
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	
	windowScreen.fill((0,0,0))
	#更新显示，消除旧图像，绘制新图像
	pygame.draw.rect(windowScreen,(34,32,32),a)
	pygame.display.update()
	#每秒钟执行30次该代码,用来控制游戏循环频率
	mainclock.tick(30)
	