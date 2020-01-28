import pygame,sys,time,random,math
from pygame.locals import *		#
from static_params import *   #引入所有静态参数

class Brick(pygame.Rect):
	def __init__(self,left,top,width,height,hitnumber,color,surface):
		super(Brick,self).__init__(left,top,width,height)
		self.color = color
		self.hitnumber = hitnumber
		self.exist = 1       #用来判断是否存在
		self.surface = surface
	
	def draw(self):
		if self.exist ==1:
			rectangle = self
			pygame.draw.rect(self.surface,self.color,rectangle)

class ball(object):
	'''
	球类属性
    1.球体颜色
	2.球体半径
	3.移动速度
	4.移动角度(和横坐标之间的夹角)
	5.圆心位置
	'''
	def __init__(self,center,radius,color,speed,angle):
		self.center = center
		self.radius = radius
		self.color = color
		self.speedx = speed*math.cos(angle)
		self.speedy = speed*math.sin(angle)

	def move(self):
		self.center=int(self.center[0]+self.speedx),int(self.center[1]+self.speedy)

	def rebound1(self):        #撞了左右的墙
		self.speedx=self.speedx*-1
	def rebound2(self):        #撞了上下的墙
		self.speedy=self.speedy*-1

	def fall(self):
		if self.center[1]>WindowHeight:
			return True
		else:
			return False


class Paddle(pygame.Rect):
	def __init__(self,left,top,width,height,color,surface):
		super(Paddle,self).__init__(left,top,width,height)
		self.color = color
		self.surface = surface

	def move(self,events):
		for event in events:
			if event.type == MOUSEMOTION:
				self.left,self.top= event.pos
				self.top =475
				return 


	def draw(self):
			rectangle = self
			pygame.draw.rect(self.surface,self.color,rectangle)


