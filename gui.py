#!/usr/bin/python
import Tkinter
import tkMessageBox
import os

top = Tkinter.Tk()
def genData():
   os.system('python dataSetGenerator.py')
   os.system('python trainer.py')
def recogFace():
   os.system('python detector.py')

B1 = Tkinter.Button(top, text = "Add new person", command = genData)
B1.pack()
B2 = Tkinter.Button(top, text = "Recognize a face", command = recogFace)
B2.pack()
top.mainloop()
