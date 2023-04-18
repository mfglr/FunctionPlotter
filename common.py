import numpy as np

class Datas:
	def __init__(self,x0,x1,xInt,y0,y1,yInt):
		self.xInt = xInt
		self.yInt = yInt
		
		self.xv,self.yv = np.meshgrid(np.linspace(x0,x1,xInt),np.linspace(y0,y1,yInt))
		
		self.buf = np.full((yInt,xInt),0,dtype=float)
		self.bufX = np.full((100,yInt,xInt),0,dtype=float)
		self.bufY = np.full((100,yInt,xInt),0,dtype=float)
	
	def log(self):
		print('****Vektor x****\n',self.xv)
		print('****Vektor y****\n',self.yv)

def error(function):
	return function


