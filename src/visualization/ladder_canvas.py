import customtkinter as ctk
from tkinter import Canvas


def create_fields(canvas:Canvas, rows=20, cols=16,x_size=80, y_size=80,padding=1):
    id_list=[]
    for r in range(rows):
        next_x = r * x_size+padding*r
        for c in range(cols):
            next_y = c*y_size+padding*c
            id_list.append(canvas.create_rectangle(next_x, next_y, next_x+x_size, next_y+y_size
                                    , fill='light blue',
                                    activeoutline='yellow')
                            )
        
    return id_list