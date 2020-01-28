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
	def __init__(self,center,radius,color,speed,angle,surface):
		self.center = center
		self.radius = radius
		self.color = color
		self.speedx = speed*math.cos(angle)
		self.speedy = speed*math.sin(angle)
		self.surface = surface

	def move(self):
		self.center=int(self.center[0]+self.speedx),int(self.center[1]+self.speedy)

	def rebound1(self):        #撞左的墙
		self.speedx=abs(self.speedx)
	def rebound2(self):
		self.speedx = -1*abs(self.speedx)  #撞右的墙
	def rebound3(self):        #撞上的墙
		self.speedy=abs(self.speedy)
	def rebound4(self):      #撞了下的墙
		self.speedy = -1*abs(self.speedy)


	def fall(self):
		if self.center[1]>WindowHeight:
			return True
		else:
			return False
	def draw(self):
		pygame.draw.circle(self.surface,self.color,self.center,self.radius)

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

	def get_pos(self,x):
		if x<0:
			self.left = 0
		elif x>WindowWidth-self.width:
			self.left = WindowWidth-self.width
		else:
			self.left = x

	def draw(self):
			rectangle = self
			pygame.draw.rect(self.surface,self.color,rectangle)


class Button(object):
	def __init__(self,surface,color,location,text):
		self.surface = surface
		self.fontstyle = pygame.font.SysFont('comicsansms',60)
		self.font = self.fontstyle.render(text,1,color)
		self.text = text
		self.location = location

	def is_overed(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		width,height = self.font.get_size()
		if mouse_x>self.location[0] and mouse_x<self.location[0]+width and mouse_y>self.location[1] and mouse_y<self.location[1]+height:
			return True
		else:
			return False


	def ButtonBlit(self):
		self.surface.blit(self.font,self.location)