from common import Datas
from function import Function
import numpy as np


def error(function,datas):
	return

class ReaderKernalForComputer:
	
	def __readAndWrite(self,indexOfTheState,function,datas):
		self.__bufferOfTheValue += function.getCurrentTransition()
		self.__transitionsArrays[indexOfTheState][ord(function.getNextTransition())](function,datas)
		
	def start(self,function,datas):
		self.__tArray[ord(function.getNextTransition())](function,datas)
		
	def __firstState0(self,function,datas):
		self.__readAndWrite(0,function,datas)
		
	def __firstState1(self,function,datas):
		self.__readAndWrite(1,function,datas)
	
	def __state2(self,function,datas):
		self.__readAndWrite(2,function,datas)
	
	def __finalState3(self,function,datas):
		datas.buf = np.full((datas.yInt,datas.xInt),float(self.__bufferOfTheValue),dtype=float)
		self.__bufferOfTheValue = ''
		self.__transitionsArrays[3][ord(function.getNextTransition())](function,datas)
	
	def upgradeFinalState(self,transition,state):
		self.__transitionsArrays[3][ord(transition)] = state
	
	def link(self,transitionsArray):
		transitionsArray[ord('0')] = self.__firstState0
		transitionsArray[ord('1')] = self.__firstState0
		transitionsArray[ord('2')] = self.__firstState0
		transitionsArray[ord('3')] = self.__firstState0
		transitionsArray[ord('4')] = self.__firstState0
		transitionsArray[ord('5')] = self.__firstState0
		transitionsArray[ord('6')] = self.__firstState0
		transitionsArray[ord('7')] = self.__firstState0
		transitionsArray[ord('8')] = self.__firstState0
		transitionsArray[ord('9')] = self.__firstState0
		
		transitionsArray[ord('+')] = self.__firstState1
		transitionsArray[ord('-')] = self.__firstState1
		
	def __setTransitions(self):
		self.__transitionsArrays[0][ord('0')] = self.__firstState0
		self.__transitionsArrays[0][ord('1')] = self.__firstState0
		self.__transitionsArrays[0][ord('2')] = self.__firstState0
		self.__transitionsArrays[0][ord('3')] = self.__firstState0
		self.__transitionsArrays[0][ord('4')] = self.__firstState0
		self.__transitionsArrays[0][ord('5')] = self.__firstState0
		self.__transitionsArrays[0][ord('6')] = self.__firstState0
		self.__transitionsArrays[0][ord('7')] = self.__firstState0
		self.__transitionsArrays[0][ord('8')] = self.__firstState0
		self.__transitionsArrays[0][ord('9')] = self.__firstState0
		self.__transitionsArrays[0][ord('.')] = self.__state2
		self.__transitionsArrays[0][ord(' ')] = self.__finalState3
		
		self.__transitionsArrays[1][ord('0')] = self.__firstState0
		self.__transitionsArrays[1][ord('1')] = self.__firstState0
		self.__transitionsArrays[1][ord('2')] = self.__firstState0
		self.__transitionsArrays[1][ord('3')] = self.__firstState0
		self.__transitionsArrays[1][ord('4')] = self.__firstState0
		self.__transitionsArrays[1][ord('5')] = self.__firstState0
		self.__transitionsArrays[1][ord('6')] = self.__firstState0
		self.__transitionsArrays[1][ord('7')] = self.__firstState0
		self.__transitionsArrays[1][ord('8')] = self.__firstState0
		self.__transitionsArrays[1][ord('9')] = self.__firstState0
		
		self.__transitionsArrays[2][ord('0')] = self.__state2
		self.__transitionsArrays[2][ord('1')] = self.__state2
		self.__transitionsArrays[2][ord('2')] = self.__state2
		self.__transitionsArrays[2][ord('3')] = self.__state2
		self.__transitionsArrays[2][ord('4')] = self.__state2
		self.__transitionsArrays[2][ord('5')] = self.__state2
		self.__transitionsArrays[2][ord('6')] = self.__state2
		self.__transitionsArrays[2][ord('7')] = self.__state2
		self.__transitionsArrays[2][ord('8')] = self.__state2
		self.__transitionsArrays[2][ord('9')] = self.__state2
		self.__transitionsArrays[2][ord(' ')] = self.__finalState3
		
		self.link(self.__tArray)
				
	def __init__(self):
		self.__bufferOfTheValue = ''
		
		self.__tArray = [error for transition in range(0,256)]
		self.__transitionsArrays = [[error for transition in range(0,256)] for state in range(0,4)]
		self.__setTransitions()


class Computer:

	def __init__(self):
		self.__rk0 = ReaderKernalForComputer()
		self.__rk1 = ReaderKernalForComputer()
		self.__transitionsArrays = [[error for transition in range(0,256)] for state in range(0,13)]
		self.__setTransitions()
		
	def __setTransitions(self):
		
		self.__transitionsArrays[0][ord('(')] = self.__state1
		
		self.__transitionsArrays[1][ord('(')] = self.__state1
		self.__transitionsArrays[1][ord('x')] = self.__state9
		self.__transitionsArrays[1][ord('y')] = self.__state10
		
		self.__rk0.link(self.__transitionsArrays[1])
		
		self.__rk0.upgradeFinalState(',',self.__state2)
		
		self.__transitionsArrays[2][ord('(')] = self.__state1
		self.__transitionsArrays[2][ord('x')] = self.__state11
		self.__transitionsArrays[2][ord('y')] = self.__state12
		
		self.__rk1.link(self.__transitionsArrays[2])
		
		self.__rk1.upgradeFinalState(')',self.__state3)
		
		self.__transitionsArrays[3][ord('+')] = self.__state4
		self.__transitionsArrays[3][ord('-')] = self.__state5
		self.__transitionsArrays[3][ord('*')] = self.__state6
		self.__transitionsArrays[3][ord('/')] = self.__state7
		self.__transitionsArrays[3][ord('^')] = self.__state8
		
		self.__transitionsArrays[4][ord(',')] = self.__state2
		self.__transitionsArrays[4][ord(')')] = self.__state3
		
		self.__transitionsArrays[5][ord(',')] = self.__state2
		self.__transitionsArrays[5][ord(')')] = self.__state3
		
		self.__transitionsArrays[6][ord(',')] = self.__state2
		self.__transitionsArrays[6][ord(')')] = self.__state3
		
		self.__transitionsArrays[7][ord(',')] = self.__state2
		self.__transitionsArrays[7][ord(')')] = self.__state3
		
		self.__transitionsArrays[8][ord(',')] = self.__state2
		self.__transitionsArrays[8][ord(')')] = self.__state3
		
		self.__transitionsArrays[9][ord(',')] = self.__state2
		
		self.__transitionsArrays[10][ord(',')] = self.__state2
		
		self.__transitionsArrays[11][ord(')')] = self.__state3
		self.__transitionsArrays[12][ord(')')] = self.__state3
		
		
	def __read(self,indexOfTheState,function,datas):
		self.__transitionsArrays[indexOfTheState][ord(function.getNextTransition())](function,datas)
	
	def state0(self,function,datas):
		self.__read(0,function,datas)
	
	def __state1(self,function,datas):
		function.indexOfBrackets += 1
		self.__read(1,function,datas)
	
	def __state2(self,function,datas):
		datas.bufX[function.indexOfBrackets] = datas.buf
		self.__read(2,function,datas)
	
	def __state3(self,function,datas):
		datas.bufY[function.indexOfBrackets] = datas.buf
		function.indexOfBrackets -= 1
		self.__read(3,function,datas)
		
	def __state4(self,function,datas):
		datas.buf = datas.bufX[function.indexOfBrackets + 1] + datas.bufY[function.indexOfBrackets + 1]
		self.__read(4,function,datas)
	
	def __state5(self,function,datas):
		datas.buf = datas.bufX[function.indexOfBrackets + 1] - datas.bufY[function.indexOfBrackets + 1]
		self.__read(5,function,datas)
	
	def __state6(self,function,datas):
		datas.buf = datas.bufX[function.indexOfBrackets + 1] * datas.bufY[function.indexOfBrackets + 1]
		self.__read(6,function,datas)
	
	def __state7(self,function,datas):
		datas.buf = datas.bufX[function.indexOfBrackets + 1] / datas.bufY[function.indexOfBrackets + 1]
		self.__read(7,function)
	
	def __state8(self,function,datas):
		datas.buf = datas.bufX[function.indexOfBrackets + 1] ** datas.bufY[function.indexOfBrackets + 1]
		self.__read(8,function,datas)
	
	def __state9(self,function,datas):
		datas.buf = datas.xv
		self.__read(9,function,datas)
	
	def __state10(self,function,datas):
		datas.buf = datas.yv
		self.__read(10,function,datas)
	
	def __state11(self,function,datas):
		datas.buf = datas.xv
		self.__read(11,function,datas)
	
	def __state12(self,function,datas):
		datas.buf = datas.yv
		self.__read(12,function,datas)
		
		
		 
