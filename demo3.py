import pygame,sys,time,random
from pygame.locals import *		
from static_params import *   #引入所有静态参数
from demo4 import *


pygame.init()   #初始化游戏
mainclock = pygame.time.Clock() #时钟设置

windowScreen = pygame.display.set_mode([WindowWidth,WindowHeight],0,32) #窗口设置
pygame.display.set_caption('打砖块游戏')    #设置窗口标题
print(BrickColor)

# 设置一个砖块类的矩阵
BrickMatrix = [[Brick(i,j,BrickWidth,BrickHeight,BrickHitNumber,BrickColor,windowScreen) for i in range(0,640,BrickWidth+3) if i+BrickWidth<640]\
for j in range(0,150,BrickHeight+2)]

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			pygame.quit()
			exit()
	windowScreen.fill((0,0,0))
	# 更新显示，消除旧图像，绘制新图像 
	for item in BrickMatrix:
		for x in item:
			x.draw()	

	pygame.display.update()
	#每秒钟执行30次该代码,用来控制游戏循环频率
	mainclock.tick(30)