from tkinter import *


def draw_coil(canvas:Canvas,x1,y1,color='black', size=80):
    '''Function to drav coil in canvas'''
    line_width = size/10
    test_column_color = 'blue'
    #code below should produce -| |- sign
    #first horizontal segment
    canvas.create_line(x1, y1, x1+line_width*3, y1, fill=color,width=line_width) 
    #second horizontal segment
    canvas.create_line(x1+line_width*7, y1, x1+size, y1, fill=color, width=line_width) 
    #first vertical segment
    canvas.create_line(x1+line_width*3, y1-line_width*3, x1+line_width*3, y1+line_width*3, fill=test_column_color, width=line_width)
    #second vertical segment
    canvas.create_line(x1+line_width*7, y1-line_width*3, x1+line_width*7, y1+line_width*3, fill=test_column_color, width=line_width)
    
