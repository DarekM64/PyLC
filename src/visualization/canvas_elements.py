from tkinter import *

#TODO change drawing logic to remove not used items in canvas instead of drawing on top
#TODO link the appearance of an element to the state of the object from the model

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

# def draw_contact2(canvas:Canvas, x1, y1, color='black', size=80):
#     '''Draw contact in canvas'''
#     ids=[]
    
#     #clear_canvas(canvas, x1, y1-size/2, size)
#     line_width = size/10
#     test_column_color = 'blue'
#     #code below should produce -| |- sign
#     #first horizontal segment
#     ids.append(canvas.create_line(x1, y1, x1+line_width*3, y1, fill=color,width=line_width)) 
#     #second horizontal segment
#     ids.append(canvas.create_line(x1+line_width*7, y1, x1+size, y1, fill=color, width=line_width)) 
#     #first vertical segment
#     ids.append(canvas.create_line(x1+line_width*3, y1-line_width*3, x1+line_width*3, y1+line_width*3, fill=test_column_color, width=line_width))
#     #second vertical segment
#     ids.append(canvas.create_line(x1+line_width*7, y1-line_width*3, x1+line_width*7, y1+line_width*3, fill=test_column_color, width=line_width))
#     #text=ele
#     #canvas.create_text(x1+line_width, y1+size - line_width,text='')

#     return ids

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

def draw_vertical_line(canvas:Canvas, x1, y1, color='black', size=80):
    '''Draw vertical line in canvas'''
    ids=[]
    line_width = size/10
    ids.append(canvas.create_line(x1, y1, x1, y1+size, fill=color, width=line_width) )

    return ids 

def draw_delete_element(canvas:Canvas, x1, y1, color='red', size=80):
    padding_sign = size/10
    
    canvas.create_line(x1+padding_sign, y1+padding_sign, x1+size-padding_sign, y1+size-padding_sign, fill=color,width=padding_sign) 
    canvas.create_line(x1+padding_sign, y1+size-padding_sign, x1+size-padding_sign, y1+padding_sign, fill=color,width=padding_sign) 

    
def draw_cursor(canvas:Canvas, x1, y1, color='yellow', size=80):
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
    # canvas.create_rectangle((x1+padding_sign*6,y1+padding_sign*2-size/2), (x1+8*padding_sign, y1+size/2-padding_sign*2),
    #                         fill = color)
    # 

def draw_label(canvas:Canvas, x1, y1, color='blue', size=80, text='?'):
    label = canvas.create_text(x1+size//2, y1+size//2,text=text)
    return label

def draw_small_text(canvas:Canvas, x1, y1, color='black'):
    canvas.create_rectangle((x1,y1), (x1+size, y1+size),fill='light blue', activeoutline='yellow')




# To remove
def draw_split(canvas:Canvas, x1, y1, color='black', size=80):
    '''Draw split in canvas
            --+--
              |'''
    clear_canvas(canvas, x1, y1-size/2, size)
    clear_canvas(canvas, x1, y1+size/2, size)
    line_width = size/10
    draw_horizontal_line(canvas, x1, y1, color='black', size=size)
    canvas.create_line(x1+size/2, y1, x1+size/2, y1+size, fill=color,width=line_width) 
    canvas.create_line(x1+size/2, y1+size, x1+size, y1+size, fill=color,width=line_width) 

def draw_join(canvas:Canvas, x1, y1, color='black', size=80):
    '''Draw join in canvas
            --+--
              |'''
    clear_canvas(canvas, x1, y1-size/2, size)
    clear_canvas(canvas, x1, y1+size/2, size)
    line_width = size/10
    draw_horizontal_line(canvas, x1, y1, color='black', size=size)
    canvas.create_line(x1+size/2, y1, x1+size/2, y1+size, fill=color,width=line_width) 
    canvas.create_line(x1, y1+size, x1+size/2, y1+size, fill=color,width=line_width) 

def clear_canvas(canvas:Canvas, x1, y1, size=80):
    '''Clear ladder field before drawing element'''
    canvas.create_rectangle((x1,y1), (x1+size, y1+size),fill='light blue', activeoutline='yellow')