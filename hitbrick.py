import pygame,sys,time,random
from pygame.locals import *		#
from static_params import *   #引入所有静态参数
from GameClass import *


pygame.init()   #初始化游戏
mainclock = pygame.time.Clock() #时钟设置

windowScreen = pygame.display.set_mode([WindowWidth,WindowHeight],0,32) #窗口设置
pygame.display.set_caption('打砖块游戏')    #设置窗口标题


ball = ball(BallCenter,BallRadius,BallColor,BallSpeed,MoveAngle,windowScreen)
paddle = Paddle(0,WindowHeight-PaddleHeight,PaddleWidth,PaddleHeight,PaddleColor,windowScreen)
# 设置一个砖块类的矩阵
BrickMatrix = [[Brick(i,j,BrickWidth,BrickHeight,BrickHitNumber,BrickColor,windowScreen) for i in range(0,640,BrickWidth+3) if i+BrickWidth<640]\
for j in range(0,150,BrickHeight+2)]
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		if event.type == MOUSEMOTION:
			mouse_x, mouse_y = event.pos  #判断鼠标的位置
	windowScreen.fill((0,0,0))
	#判断球的运动
	#判断是否撞上了边界或者挡板
	if ball.center[1]+ball.radius+paddle.height > WindowHeight:
		if ball.center[0]>paddle.left and ball.center[0]<paddle.left+paddle.width:
			ball.rebound4()
	#判断是否装上了左边界
	elif ball.center[0]-ball.radius<0.005:
		ball.rebound1()
	elif ball.center[0]+ball.radius>WindowWidth-0.005:
		ball.rebound2()
	#判断是否撞上了上边界
	elif ball.center[1]-ball.radius<0.005:
		ball.rebound3()
	for brickline in BrickMatrix:
		for brick in brickline:	
			if brick.exist == 1:	
				if brick.top >ball.center[1] and brick.top-ball.center[1]-ball.radius<0.005 and ball.speedy>0 and ball.center[0]>brick.left and ball.center[0]<brick.right:
					print(1,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
					ball.rebound4()
					brick.hitnumber =brick.hitnumber-1
				if ball.center[1]>brick.bottom and ball.center[1]-ball.radius-brick.bottom<0.005 and ball.speedy<0 and ball.center[0]>brick.left and ball.center[0]<brick.right:
					print(2,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
					ball.rebound3()
					brick.hitnumber =brick.hitnumber-1
				if ball.center[0]< brick.left and brick.left-ball.center[0]-ball.radius<0.005 and ball.speedx>0 and ball.center[1]>brick.top and ball.center[1]<brick.bottom:
					print(3,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
					ball.rebound2()
					brick.hitnumber =brick.hitnumber-1
				if ball.center[0]>brick.right and ball.center[0]-ball.radius-brick.right<0.005 and ball.speedx<0 and ball.center[1]>brick.top and ball.center[1]<brick.bottom:
					print(4,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
					ball.rebound1()
					brick.hitnumber =brick.hitnumber-1
			if brick.hitnumber <= 0:
				brick.exist = 0
	# print(brick.hitnumber,brick.exist)
	ball.move()
	paddle.get_pos(mouse_x)
	if ball.fall():
		print('The ball is fell!')
	#画出图形
	for brickline in BrickMatrix:
		for brick in brickline:
			brick.draw()
	ball.draw()
	paddle.draw()
	pygame.display.update()
	#每秒钟执行30次该代码,用来控制游戏循环频率
	mainclock.tick(30)
	

