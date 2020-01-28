from math import *
from random import *
BallColor = (33,42,53)
BallRadius = 7
WindowHeight=480
WindowWidth=640
StartHeight = 120 # 
EndHeight =90
BallCenter =choice([(int(i),int(j)) for i in range(0,WindowWidth) for j in range(StartHeight,WindowHeight-EndHeight)]) 
BallSpeed = 5
PaddleHeight = 10
PaddleWidth = 80
PaddleColor = (34,34,34)
BrickColor = (214,39,39)
BrickHeight = 15
BrickWidth = 25
BrickHitNumber = 1
interval = 5e-3
MoveAngle =pi/4
FontColor = (255,0,0)
TextLocation = (150,290)
TextLocation2 = (200,350)
ImageLocation = (260,150)
