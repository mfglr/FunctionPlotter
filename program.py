from common import Datas
from code import Code
from function import Function
from reader import Reader
from computer import Computer

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

r = Reader()
c = Computer()
fig = plt.figure()
ax = plt.axes(projection='3d')



from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()
window.title('')

window.geometry("600x600")
T = Text(window, height = 10, width = 70)

def split(t):
	code = ''
	function = ''
	i = 0
	
	while t[i] != ';':
		code += t[i]
		i += 1
	code += ';'
	i += 1
	
	while t[i] != ';':
		function += t[i]
		i += 1
	function += ';'
	
	return code,function

def runCode():
	t = T.get('1.0', 'end-1c').split('\n')
	global ax
	global canvas
	plt.cla()
	for i in t:
		cString,fString = split(i)
		code = Code(cString)
		r.start(code)
		datas = r.getDatas()
		function = Function(fString)
		c.state0(function,datas)
		ax.contour3D(datas.xv, datas.yv, datas.buf, 50, cmap='binary')
	canvas.draw()


B = Button(window, text ="run", command = runCode)

T.pack()
B.pack()
canvas = FigureCanvasTkAgg(fig,master = window)
canvas.get_tk_widget().pack()



window.mainloop()



