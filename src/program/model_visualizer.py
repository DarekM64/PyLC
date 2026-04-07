#methods for managing ladder canvas
from tkinter import Canvas
from src.visualization.canvas_elements import *

def clear_canvas(canvas):
    canvas.delete('all')

def delete_canvas_elements(canvas, ids):
    for id in ids:
        canvas.delete(id)

def delete_canvas_element(canvas, id):
    canvas.delete(id)

def create_net(canvas:Canvas, size_px:int=2, rows:int=20, columns:int=16, space:int=80):
    '''
        Creates dot net in canvas
        canvas: target Canvas
        size_px: pixel size of dot
        rows: number of dot rows
        columns: number of dot columns
        space: space between dots
    '''
    next_y = space
    for i in range(rows):
        next_x = space
        for j in range(columns):
            canvas.create_oval(next_x, next_y, next_x+size_px, next_y+size_px)
            next_x+= space
        next_y += space

def calc_position_element(x, y, grid_width):
        return x*grid_width, y*grid_width+grid_width//2

# def create_label(grid_x, grid_y, element):
#      text = element.connected_data_type + element.connected_data_address
#      canvas.create_text(x1+line_width, y1+size - line_width,text='')