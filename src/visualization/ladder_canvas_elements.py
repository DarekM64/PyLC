from tkinter import *


def draw_contact(canvas:Canvas,x1,y1,color='black', size=80):
    '''Function to draw coil in canvas'''
    clear_canvas(canvas, x1, y1, size)
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
    
def draw_coil(canvas:Canvas,x1,y1,color='black', size=80):
    '''Function to draw coil in canvas'''
    clear_canvas(canvas, x1, y1, size)
    line_width = size/10
    test_column_color = 'blue'
    #code below should produce -| |- sign
    #first horizontal segment
    canvas.create_line(x1, y1, x1+line_width*2, y1, fill=color,width=line_width) 
    #second horizontal segment
    canvas.create_line(x1+line_width*8, y1, x1+size, y1, fill=color, width=line_width) 
    #first arc segment
    canvas.create_arc(x1+line_width*2, y1-line_width*3, x1+line_width*8, y1+line_width*3, 
                      start=-45,
                      extent=90,
                      style='arc',
                      fill=test_column_color, width=line_width)
    #second arc segment
    canvas.create_arc(x1+line_width*2, y1-line_width*3, x1+line_width*8, y1+line_width*3, 
                      start=135,
                      extent=90,
                      style='arc',
                      fill=test_column_color, width=line_width)

def draw_line(canvas:Canvas,x1,y1,color='black', size=80):
    '''Function to draw coil in canvas'''
    clear_canvas(canvas, x1, y1, size)
    line_width = size/10
    test_column_color = 'blue'
    #code below should produce -| |- sign
    #horizontal line
    canvas.create_line(x1, y1, x1+size, y1, fill=color,width=line_width) 


def clear_canvas(canvas:Canvas, x1, y1, size=80):
    '''Clear ladder field before drawing element'''
    canvas.create_polygon((x1,y1), (x1+size, y1+size),fill='red')