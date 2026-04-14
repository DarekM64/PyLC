from tkinter import *


def draw_contact(canvas:Canvas, x1, y1, color='black', size=80):
    '''Draw contact in canvas'''
    ids=[]
    #clear_canvas(canvas, x1, y1-size/2, size)
    line_width = size/10
    test_column_color = 'black'
    #code below should produce -| |- sign
    #first horizontal segment
    ids.append(canvas.create_line(x1, y1, x1+line_width*3, y1, fill=color,width=line_width)) 
    #second horizontal segment
    ids.append(canvas.create_line(x1+line_width*7, y1, x1+size, y1, fill=color, width=line_width)) 
    #first vertical segment
    ids.append(canvas.create_line(x1+line_width*3, y1-line_width*3, x1+line_width*3, y1+line_width*3, fill=test_column_color, width=line_width))
    #second vertical segment
    ids.append(canvas.create_line(x1+line_width*7, y1-line_width*3, x1+line_width*7, y1+line_width*3, fill=test_column_color, width=line_width))
    #inner rectangle, reflecting value, evaluate True = visible, False = unvisible
    ids.append(canvas.create_line(x1+size/2, y1-size/4, x1+size/2, y1+size/4, fill='blue', width=size/4, state='hidden'))

    return ids


def draw_coil(canvas:Canvas,x1,y1,color='black', size=80):
    '''Draw coil in canvas'''
    ids=[]
    line_width = size/10
    test_column_color = 'blue'
    #code below should produce -( )- sign
    #first horizontal segment
    ids.append(canvas.create_line(x1, y1, x1+line_width*2, y1, fill=color, width=line_width) )
    #second horizontal segment
    ids.append(canvas.create_line(x1+line_width*8, y1, x1+size, y1, fill=color, width=line_width))
    #first arc segment
    ids.append(canvas.create_arc(
                                x1+line_width*2, y1-line_width*3, x1+line_width*8, y1+line_width*3, 
                                start=-45,
                                extent=90,
                                style='arc',
                                fill=test_column_color, width=line_width
                                )
                )
    #second arc segment
    ids.append(canvas.create_arc(
                                x1+line_width*2, y1-line_width*3, x1+line_width*8, y1+line_width*3, 
                                start=135,
                                extent=90,
                                style='arc',
                                fill=test_column_color, width=line_width
                                )
                )
    #inner rectangle, reflecting value, evaluate True = visible, False = unvisible
    ids.append(canvas.create_line(x1+size/2, y1-size/4, x1+size/2, y1+size/4, fill='blue', width=size/4, state='hidden'))
    return ids

def draw_horizontal_line(canvas:Canvas, x1, y1, color='black', size=80):
    '''Draw horizontal line in canvas'''
    ids=[]
    line_width = size/10
    ids.append(canvas.create_line(x1, y1, x1+size, y1, fill=color, width=line_width) )

    return ids


def draw_vertical_line(canvas:Canvas, x1, y1, color='black', color2='black', size=80, line_width=None):
    '''Draw vertical line in canvas'''
    ids=[]
    if line_width is None:
        line_width = size/10
    ids.append(canvas.create_line(x1, y1, x1, y1+size, fill=color, disabledfill=color2, width=line_width) )

    return ids 

def draw_delete_element(canvas:Canvas, x1, y1, color='red', size=80):
    '''Draw x - delete sign'''
    padding_sign = size/10
    
    canvas.create_line(x1+padding_sign, y1+padding_sign, x1+size-padding_sign, y1+size-padding_sign, fill=color,width=padding_sign) 
    canvas.create_line(x1+padding_sign, y1+size-padding_sign, x1+size-padding_sign, y1+padding_sign, fill=color,width=padding_sign) 

    
def draw_cursor(canvas:Canvas, x1, y1, color='yellow', size=80):
    '''Draw cross sign'''
    padding_sign = size/10
    canvas.create_line(x1+padding_sign, y1, x1+size-padding_sign, y1, fill=color,width=padding_sign) 
    canvas.create_line(x1+size/2, y1+size/2-padding_sign, x1+size/2, y1-size/2+padding_sign, fill=color,width=padding_sign) 

def draw_pointer(canvas:Canvas, x1, y1, color='yellow', size=80):
    padding_sign = size/10
    canvas.create_line(x1+padding_sign, y1, x1+size-padding_sign, y1, fill=color,width=padding_sign) 
    canvas.create_line(x1+size/2, y1+size/2-padding_sign, x1+size/2, y1-size/2+padding_sign, fill=color,width=padding_sign) 


def draw_stop(canvas:Canvas, x1, y1, color='yellow', size=80):
    '''Draw stop play pictogram'''
    padding_sign = size/10
    canvas.create_rectangle((x1+padding_sign*2,y1+padding_sign*2-size/2), (x1+4*padding_sign, y1+size/2-padding_sign*2),
                            fill = color)
    canvas.create_rectangle((x1+padding_sign*6,y1+padding_sign*2-size/2), (x1+8*padding_sign, y1+size/2-padding_sign*2),
                            fill = color)
    
def draw_start(canvas:Canvas, x1, y1, color='yellow', size=80):
    '''Draw start play pictogram'''
    padding_sign = size/10
    canvas.create_polygon((x1+padding_sign*2,y1+padding_sign*2-size/2),
                          (x1+2*padding_sign, y1+size/2-padding_sign*2),
                          (x1+8*padding_sign, y1),
                            fill = color)

def draw_label(canvas:Canvas, x1, y1, color='blue', size=80, text='?'):
    label = canvas.create_text(x1+size//2, y1+size//2,text=text)
    return label