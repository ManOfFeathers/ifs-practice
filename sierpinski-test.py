#                 Sierpinski Triangle
#
#  Programmed by Jean Flaherty and Griffin Myers (06-24-2017)
#
#  The means of implementing the functions from sierpinski.py in a
#  TkInter canvas
#

from sierpinski import Triangle
from sierpinski import Trema
from tkinter import *
import math

width = 729
height = 729

root = Tk()

c = Canvas(root, width = 729, height = 729, bg = "white")
c.pack(expand = YES, fill = BOTH)

triangle = Triangle(root, c, left = 0, top = 0, width = width, height = height,
                    tri_color = "black")

trema = Trema(root, c, left = 0, top = 0, width = width, height = height,
              trema_color = "white")

triangle.draw(0,0,width)
c.update()
trema.draw(0,width,height)
c.update()
