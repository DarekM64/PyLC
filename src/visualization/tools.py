from tkinter import Canvas
import customtkinter as ctk
from canvas_elements import *

def create_frame_tools(master):
    tools_frame =ctk.CTkFrame(master=master,
                height=100,
                bg_color='dark grey',
                fg_color='dark grey')
     
    tools_frame.pack(side='top',fill='x')
    tools_frame.grid_rowconfigure(0, weight=1) 
    tools_frame.grid_columnconfigure(0, weight=1)

    button1=create_button(tools_frame,shape_type='coil',size = 80)
    button2=create_button(tools_frame,shape_type='contact',size = 80)
    button3=create_button(tools_frame,shape_type='line_horizontal',size = 80)
    button4=create_button(tools_frame,shape_type='line_vertical',size = 80)
    button5=create_button(tools_frame,shape_type='delete_element',size = 80)
    button6=create_button(tools_frame,shape_type='delete_vertical',size = 80)
    button7=create_button(tools_frame,shape_type='cursor',size = 80)

    button1.grid(row=0, column=0,padx=5,pady=5, sticky='e')
    button2.grid(row=0, column=1,padx=5,pady=5, sticky='e')
    button3.grid(row=0, column=2,padx=5,pady=5, sticky='e')
    button4.grid(row=0, column=3,padx=5,pady=5, sticky='e')
    button5.grid(row=0, column=4,padx=5,pady=5, sticky='e')
    button6.grid(row=0, column=5,padx=5,pady=5, sticky='e')
    button7.grid(row=0, column=6,padx=5,pady=5, sticky='e') 


    button_plc_1=create_button(tools_frame,shape_type='stop',size = 80)
    button_plc_2=create_button(tools_frame,shape_type='start',size = 80)
    
    button_plc_1.grid(row=0, column=7,padx=5,pady=5, sticky='e')
    button_plc_2.grid(row=0, column=8,padx=5,pady=5, sticky='e')
    
    return tools_frame


def create_button(master, shape_type='coil',size = 80):
    button_frame = Canvas(master, width=size, height=size)
    button_frame.create_rectangle(0, 0, size, size, 
                                fill='grey',
                                activeoutline='yellow')
    color = 'black'
    pos_y = size//2

    #Draw symbols in tools and action buttons
    match shape_type:
        case 'coil':
            draw_coil(button_frame, 0, pos_y, color=color, size=size)
        case 'contact':
            draw_contact(button_frame, 0, pos_y, color=color, size=size)
        case 'line_horizontal':
            draw_horizontal_line(button_frame, 0, pos_y, color=color, size=size)
        case 'line_vertical':
            draw_vertical_line(button_frame, size//10, size//10, size=size)
        case 'delete_element':
            draw_delete_element(button_frame, size//4, size//4, color='red', size=size//2)
        case 'delete_vertical':
            draw_vertical_line(button_frame, size//10, size//10, color=color, size=size)
            draw_delete_element(button_frame, size//4, size//4, color='red', size=size//2)
        case 'cursor':
            draw_cursor(button_frame, 0, pos_y, color, size=size)
        case 'stop':
            draw_stop(button_frame, 0, pos_y, color, size=size)
        case 'start':
            draw_start(button_frame, 0, pos_y, color, size=size)

    return button_frame