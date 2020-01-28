
import pygame,sys,time,random
from pygame.locals import *		#
from static_params import *   #引入所有静态参数
from GameClass import *


pygame.init()   #初始化游戏
mainclock = pygame.time.Clock() #时钟设置
Exit =0
global Surface 
Surface = pygame.display.set_mode([WindowWidth,WindowHeight],0,32) #窗口设置
Surface.set_caption('打砖块游戏')    #设置窗口标题
def BeforeGame():
	StartImage = pygame.image.load('intro_ball.png').convert_alpha() #开始图像的界面
	button = Button(Surface,FontColor,TextLocation,text)
	while True:
		for event in pygame.event.get():
			if event.type ==QUIT:
				Exit = 1
				pygame.quit()
				exit()
			if event.type == MOUSEBUTTONUP:
				if button.is_overed():
					break
		Surface.blit(StartImage,ImageLocation)
		button.ButtonBlit()
		pygame.display.update()
		mainclock.tick(100)

def Gaming():
	#设置一个暂停函数
	def pause():
		button = Button(Surface,FontColor,TextLocation,'Continue')
		Surface.fill((0,0,0))
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					Exit = 1
					pygame.quit()
					exit()
				if event.type == MOUSEBUTTONUP:
					if button.is_overed():
						break
			button.ButtonBlit()
			pygame.display.update()
			mainclock.tick(100)

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
			if event.type == KEYDOWN:   #按下空格键暂停
				if event.key == K_SPACE:
					pause()
		windowScreen.fill((0,0,0))
		#设置鼠标为不可见状态
		pygame.mouse.set_visible(False)
		#判断球的运动
		#判断是否撞上了边界或者挡板
		if ball.center[1]+ball.radius+paddle.height > WindowHeight:
			if ball.center[0]>paddle.left and ball.center[0]<paddle.left+paddle.width:
				ball.rebound4()
		#判断是否装上了左边界
		elif ball.center[0]-ball.radius<interval:
			ball.rebound1()
		elif ball.center[0]+ball.radius>WindowWidth-interval:
			ball.rebound2()
		#判断是否撞上了上边界
		elif ball.center[1]-ball.radius<interval:
			ball.rebound3()
		for brickline in BrickMatrix:
			for brick in brickline:	
				if brick.exist == 1:	
					if brick.top >ball.center[1] and brick.top-ball.center[1]-ball.radius<interval and ball.speedy>0 and ball.center[0]>brick.left and ball.center[0]<brick.right:
						print(1,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
						ball.rebound4()
						brick.hitnumber =brick.hitnumber-1
					if ball.center[1]>brick.bottom and ball.center[1]-ball.radius-brick.bottom<interval and ball.speedy<0 and ball.center[0]>brick.left and ball.center[0]<brick.right:
						print(2,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
						ball.rebound3()
						brick.hitnumber =brick.hitnumber-1
					if ball.center[0]< brick.left and brick.left-ball.center[0]-ball.radius<interval and ball.speedx>0 and ball.center[1]>brick.top and ball.center[1]<brick.bottom:
						print(3,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
						ball.rebound2()
						brick.hitnumber =brick.hitnumber-1
					if ball.center[0]>brick.right and ball.center[0]-ball.radius-brick.right<interval and ball.speedx<0 and ball.center[1]>brick.top and ball.center[1]<brick.bottom:
						print(4,ball.center,brick.left,brick.right,brick.top,brick.bottom,ball.radius)
						ball.rebound1()
						brick.hitnumber =brick.hitnumber-1
					if brick.hitnumber <= 0:
						brick.exist = 0
		#所有的砖块都不存在了，则游戏胜利
		if all([not any([brick.exist for brick in line]) for line in BrickMatrix] ):
			return 'Win'
		# print(brick.hitnumber,brick.exist)
		ball.move()
		paddle.get_pos(mouse_x)
		if ball.fall():
			return 'Fail'
		#画出图形
		for brickline in BrickMatrix:
			for brick in brickline:
				brick.draw()
		ball.draw()
		paddle.draw()
		pygame.display.update()
		#每秒钟执行100次该代码,用来控制游戏循环频率
		mainclock.tick(100)
	

def AfterGame(text):
	result = pygame.font.SysFont('comicsansms',100).render(text,1,(0,255,0))
	Surface.Blit(result,ImageLocation)
	button1 = Button(Surface,FontColor,TextLocation,'PLAY IT AGAIN')
	button2 = Button(Surface,FontColor,TextLocation,'QUIT')
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				Exit = 1
				pygame.quit()
				exit()
			if event.type == MOUSEBUTTONUP:
				if button1.is_overed():
					break
				if button2.is_overed():
					Exit = 1
					pygame.quit()
					exit()
		button1.ButtonBlit()
		button2.ButtonBlit()
		pygame.display.update()
		mainclock.tick(100)


def main():
	#展示游戏开始前的信息
	BeforeGame()
	#开始游戏循环
	while not Exit:
		com=Gaming()
		AfterGame(com)


if __name__ =='__main__':
	main()
