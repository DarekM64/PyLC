import customtkinter as ctk
from tkinter import Canvas
from src.visualization.canvas_elements import *

def create_button(master, shape_type='coil',size = 80):
    button_frame = Canvas(master, width = size, height=size)
    button_frame.create_rectangle(0, 0, size, size, 
                                fill='grey',
                                activeoutline='yellow')
    draw_element(button_frame, 0, size/2, shape_type=shape_type)
    # match element_type:
    #     case 'coil':
    #         draw_coil(button_frame,0,size/2)
    #     case 'contact':
    #         draw_contact(button_frame,0,size/2)
    #     case 'line':
    #         draw_line(button_frame,0,size/2)

    return button_frame


    
        
