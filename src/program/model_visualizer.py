#methods for managing ladder canvas
from tkinter import Canvas
from src.visualization.canvas_elements import *
from tkinter import messagebox
from src.program.modelGridElement import ModelGridElement

def clear_canvas(canvas):
    canvas.delete('all')

def delete_canvas_elements(canvas, ids):
    for id in ids:
        canvas.delete(id)

def delete_canvas_element(canvas, id):
    canvas.delete(id)

def create_net(canvas:Canvas, size_px:int=2, rows:int=20, columns:int=16, space:int=80):
    '''
        Creates dot grid in canvas
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

def create_rungs_lines(canvas:Canvas, rows:int=20, line_width:int=5, space:int=80):
    '''
        Creates rungs lines in canvas
        canvas: target Canvas
        rows: number of program rows
        line_width: px width of vertical line
    '''
    lines=[]
    next_y = 0
    for i in range(rows):
        lines.append(draw_vertical_line(canvas, 0, next_y, color='black', color2='green2', size=80)[0])
        next_y += space
    return lines

def calc_position_element(x, y, grid_width):
        return y*grid_width, x*grid_width+grid_width//2

def not_compiled_box():
     messagebox.showwarning(title='Not compiled program', message='Compile program before run')

def update_elements_display(canvas, grid_element:ModelGridElement):
     if grid_element.element.get_value():
          canvas.itemconfig(grid_element.element_canvas_id[-1], state='normal')
     else:
          canvas.itemconfig(grid_element.element_canvas_id[-1], state='hidden')

def hide_elements_display(canvas, grid_element:ModelGridElement):
     canvas.itemconfig(grid_element.element_canvas_id[-1], state='hidden')
