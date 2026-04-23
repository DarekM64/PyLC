import json
import copy
import jsonpickle
from src.program.modelGridElement import ModelGridElement
from src.program.model_visualizer import *
from src.ladder.ladder_elements import *
from tkinter import filedialog

def encode_workspace(grid:dict[tuple, ModelGridElement]):

    '''Fields to save:
        pos_x
        pos_y
        element:
                "type": "coil",
                "connected_data_type": "M",
                "connected_data_address": 2,
                "normal_open": true,
        node:
                "type": "coil",
                "connected_data_type": "M",
                "connected_data_address": 2,
                "normal_open": true,
    '''
    json_string = jsonpickle.encode(grid, indent=4, keys=True)
    file= filedialog.asksaveasfilename()
    
    #with open("rung_json.json", "w") as f:
    with open(file, "w") as f:
        f.write(json_string)
    # Save to file
    #with open('rung_json.pkl', 'w') as f:  # Note: 'wb' for write binary
     #   jsonpickle.dumps(grid, f)

#def encode_workspace(json_string, grid):
def decode_workspace():
    # Load from file
    file= filedialog.askopenfilename()
    with open(file, 'r') as f:  # Note: 'rb' for read binary
        loaded_data = f.read()
    recreated_obj = jsonpickle.decode(loaded_data,  keys=True)
    return recreated_obj



def build_workspace(grid: dict[tuple, ModelGridElement], canvas, grid_width, plc):
    '''Creates objects in workspace canvas for ladder loaded from file'''
    
    for tile in grid.values():
        canvas_x,canvas_y= calc_position_element(tile.pos_x, tile.pos_y, grid_width)
        if tile.element is not None:
            
            match tile.element.type:
                case 'contact':
                    
                    ids=draw_contact(canvas, canvas_x, canvas_y, color='black',  size = grid_width)
                case 'coil':
                    #element=Coil(connected_data_type='M', connected_data_address = 0, normal_open = True, connected_data=self.plc.M[0])
                    ids=draw_coil(canvas, canvas_x, canvas_y, color='black',  size = grid_width)
                case 'line':
                    #element=Line()  
                    ids=draw_horizontal_line(canvas, canvas_x, canvas_y, color='black',  size = grid_width)

            #Label to display assigned value if element use one
            use_label = not isinstance(tile.element, Line)
            label=None
            if use_label:
                tile.element.connected_data = plc.bind_data(tile.element.connected_data_type, tile.element.connected_data_address)
                label_text= tile.element.connected_data_type + ' ' + str(tile.element.connected_data_address)
                label = draw_label(canvas, canvas_x, canvas_y, text=label_text)   
            tile.element_canvas_id = ids
            if use_label:
                tile.label = label

        if tile.node is not None:
            ids=draw_vertical_line(canvas, canvas_x, canvas_y, size = grid_width)
            tile.node_canvas_id = ids