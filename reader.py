from common import error,Datas
from code import Code
from readerKernal import ReaderKernal
import numpy as np

class ReaderPartial:
	def __read(self,indexOfTheState,code):
		self.__transitionsArrays[indexOfTheState][ord(code.getNextTransition())](code)
	
	def start(self,code):
		self.__tArray[ord(code.getNextTransition())](code)
	
	def state0(self,code):
		self.__read(0,code)
	
	def __state1(self,code):
		self.x = self.__rk0.value
		self.__read(1,code)
	
	def __state2(self,code):
		self.y = self.__rk1.value
		self.__read(2,code)
		
	def __state3(self,code):
		self.interval = self.__rk2.value
		self.__read(3,code)
	
	def upgradeFinalState(self,transition,state):
		self.__transitionsArrays[3][ord(transition)] = state
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.interval = 0
		self.__tArray = [error for transition in range(0,256)]
		self.__transitionsArrays = [[error for transition in range(0,256)] for state in range(0,4)]
		self.__rk0 = ReaderKernal()
		self.__rk1 = ReaderKernal()
		self.__rk2 = ReaderKernal()

		self.__setTransitions()
				
	def __setTransitions(self):
	
		self.__rk0.link(self.__transitionsArrays[0])
		self.__rk0.upgradeFinalState(',',self.__state1)
		
		self.__rk1.link(self.__transitionsArrays[1])
		self.__rk1.upgradeFinalState(',',self.__state2)
		
		self.__rk2.link(self.__transitionsArrays[2])
		self.__rk2.upgradeFinalState(']',self.__state3)
		
		self.__tArray[ord('[')] = self.state0

def end(code):
	return
	
class Reader:
	def __init__(self):
		self.__transitionsArrays = [[error for transition in range(0,256)] for state in range(0,4)]
		self.__r0 = ReaderPartial()
		self.__r1 = ReaderPartial()
		self.__setTransitions()
	
	def __read(self,indexOfTheState,code):
		self.__transitionsArrays[indexOfTheState][ord(code.getNextTransition())](code)
		
	
	def __state0(self,code):
		self.__read(0,code)
	
	def __state1(self,code):
		self.__read(1,code)
	
	def __state2(self,code):
		self.__read(2,code)
		
	def __setTransitions(self):
		self.__transitionsArrays[0][ord('[')] = self.__r0.state0
		self.__r0.upgradeFinalState(',',self.__state1)
		
		self.__transitionsArrays[1][ord('[')] = self.__r1.state0 
		self.__r1.upgradeFinalState(';',end)
	
	def getDatas(self):
		xInt = int(self.__r0.interval)
		yInt = int(self.__r1.interval)
		return Datas(self.__r0.x,self.__r0.y,xInt,self.__r1.x,self.__r1.y,yInt)
		
	def start(self,code):
		self.__state0(code)

