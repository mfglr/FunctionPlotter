from common import error
from code import Code

class ReaderKernal:
	
	def __readAndWrite(self,indexOfTheState,code):
		self.__bufferOfTheValue += code.getCurrentTransition()
		self.__transitionsArrays[indexOfTheState][ord(code.getNextTransition())](code)
		
	def start(self,code):
		self.__tArray[ord(code.getNextTransition())](code)
		
	def __firstState0(self,code):
		self.__readAndWrite(0,code)
		
	def __firstState1(self,code):
		self.__readAndWrite(1,code)
	
	def __state2(self,code):
		self.__readAndWrite(2,code)
	
	def __finalState3(self,code):
		self.value = float(self.__bufferOfTheValue)
		self.__bufferOfTheValue = ''
		self.__transitionsArrays[3][ord(code.getNextTransition())](code)
	
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
		self.value = 0
		self.__bufferOfTheValue = ''
		
		self.__tArray = [error for transition in range(0,256)]
		self.__transitionsArrays = [[error for transition in range(0,256)] for state in range(0,4)]
		self.__setTransitions()


