import customtkinter as ctk
from tkinter import Canvas


def create_fields(canvas:Canvas, rows=20, cols=16,x_size=80, y_size=80,padding=0):
    id_list=[]
    for r in range(cols):
        next_x = r * x_size+padding*r
        for c in range(rows):
            next_y = c*y_size+padding*c
            id_list.append(create_field(canvas, next_x, next_y, x_size, y_size))
            # id_list.append(canvas.create_rectangle(next_x, next_y, next_x+x_size, next_y+y_size
            #                         , fill='light blue',
            #                         activeoutline='yellow')
            #                 )
        
    return id_list

def create_field(canvas:Canvas, pos_x, pos_y, x_size, y_size):
    return canvas.create_rectangle(pos_x, pos_y, pos_x+x_size, pos_y+y_size
                                    , fill='light blue',
                                    activeoutline='yellow')