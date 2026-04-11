import threading
import time

from src.ladder.ladder_elements import *
from src.plc.plc import *

from src.program.modelGridElement import ModelGridElement
from src.program.model_visualizer import *
from src.program.model_search import model_search
import src.visualization.canvas_elements as canvas_elements
import src.visualization.element_parameter as element_parameter

class Model():
    '''Connects data for graphic presentation and rung logic
        ladder_model_grid:  list of elements tied to [x][y] node
                            this provides data to create plc rung logic
                            and canvas drawing
    '''
    def __init__(self, rows=20, cols=16):
        #self.initialize_program(rows, cols)
        self.plc=PLC()
        self.selected_tool='contact'
        self.selected_action='none'
        self.ladder_model_grid={}
        self.canvas:Canvas=None
        self.compiled = False
        self.update_canvas = threading.Thread(target=self.update_canvas)
        self.update_canvas.start()
        self.close_update_canvas=False

    def attach_canvas(self, canvas:Canvas):
        self.canvas=canvas
        canvas.bind("<Button-1>", self.click_handler)

    def set_Selected_Element(self, selected_element):   
        self.selected_element = selected_element

    def initialize_program(self,rows, cols, grid_width):
        #'''Creates empty list of elements for clean ladder'''
        self.grid_width = grid_width
        clear_canvas(self.canvas)
        self.canvas.configure(height=rows*grid_width, width=cols*grid_width)
        create_net(self.canvas,3, rows, cols, grid_width)

    
    def select_tool(self, tool):
        self.selected_tool=tool
            
    def select_plc_action(self, action):
        self.selected_action=action

        if self.selected_action == 'start':
            if not self.compiled:
                not_compiled_box()
            else:
                self.plc.start()
        elif self.selected_action == 'stop':
            self.plc.stop()



    def get_element(self, grid_x, grid_y):
        return self.ladder_model_grid[grid_x][grid_y]
    
   

    def add_element(self,grid_x, grid_y):
        canvas_x,canvas_y= calc_position_element(grid_x, grid_y, self.grid_width)
        #group of elements managed similar way in model

        match self.selected_tool:
            case 'contact':
                element=Contact(connected_data_type='M', connected_data_address = 0, normal_open = True, connected_data=self.plc.M[0]) 
                ids=draw_contact(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)
            case 'coil':
                element=Coil(connected_data_type='M', connected_data_address = 0, normal_open = True, connected_data=self.plc.M[0])
                ids=draw_coil(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)
            case 'line_horizontal':
                element=Line()  
                ids=draw_horizontal_line(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)
        
        use_label = not isinstance(element, Line)
        label=None
        if use_label:
            label_text= element.connected_data_type + ' ' + str(element.connected_data_address)
            label = draw_label(self.canvas, canvas_x, canvas_y, text=label_text)   
        
        #Element exist, remove old add new one
        
        #if self.ladder_model_grid[(grid_x, grid_y)].element != None:
        if (grid_x, grid_y) in self.ladder_model_grid:
            delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id)
            delete_canvas_element(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].label)
            self.ladder_model_grid[(grid_x, grid_y)].element = element
            self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id = ids
            if use_label:
                self.ladder_model_grid[(grid_x, grid_y)].label = label

        #No element or node, create new grid element
        else:
            modelGridElement = ModelGridElement(grid_x, grid_y, element_canvas_id=ids, element=element, label=label)
            self.ladder_model_grid[(grid_x, grid_y)]=modelGridElement

        #update_neighbours(grid_x, grid_y, self.ladder_model_grid, element, action='add_element')

    def add_node(self,grid_x, grid_y):
        canvas_x,canvas_y= calc_position_element(grid_x, grid_y, self.grid_width)
        #group of elements managed similar way in model

        node = Line()
        ids=draw_vertical_line(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)

        if (grid_x,grid_y) in self.ladder_model_grid:
            if self.ladder_model_grid[(grid_x, grid_y)].node != None:
                delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id)
                self.ladder_model_grid[(grid_x, grid_y)].node = node
                self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id = ids
            else:
                #node exist, but no element in grid, add new one       
                self.ladder_model_grid[(grid_x, grid_y)].node = node
                self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id = ids
        #No element or node, create new grid element
        else:
            modelGridElement = ModelGridElement(grid_x, grid_y, node_canvas_id=ids, node=node)
            self.ladder_model_grid[(grid_x, grid_y)]=modelGridElement

    def delete_element(self, grid_x, grid_y):
        '''Deleting element from model'''
        if (grid_x,grid_y) in self.ladder_model_grid:
            if self.ladder_model_grid[(grid_x, grid_y)].element != None:
                delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id)
                delete_canvas_element(self.canvas,  self.ladder_model_grid[(grid_x, grid_y)].label)
                self.ladder_model_grid[(grid_x, grid_y)].element = None

    def delete_node(self, grid_x, grid_y):
        '''Deleting node (vertical_line) from model'''
        if (grid_x,grid_y) in self.ladder_model_grid:
            if self.ladder_model_grid[(grid_x, grid_y)].node != None:
                delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id)
                self.ladder_model_grid[(grid_x, grid_y)].node = None

    def display_settings(self, grid_x, grid_y):
        '''Display element settings'''
        if (grid_x,grid_y) in self.ladder_model_grid:
            if self.ladder_model_grid[(grid_x, grid_y)].element != None:
                element_parameter.create_setting_window2(self.canvas,  self.ladder_model_grid[(grid_x, grid_y)], self.plc )

                

            

    def check_element_exist(self,grid_x, grid_y):
        if (grid_x, grid_y) in self.ladder_model_grid:
            if self.selected_tool != 'node':
                return True
        
        return False


    def click_handler(self, event):
        '''calculate x,y index  of clickecd field'''
        x=self.canvas.canvasx(event.x)
        y=self.canvas.canvasy(event.y)

        print(f'x={x}, y={y}')
        #calc grid index
        grid_y = int(x//self.grid_width)
        grid_x = int(y//self.grid_width)
        print(f'grid_x={grid_x}, grid_y={grid_y}')

        print(f'element exist:{self.check_element_exist(grid_x, grid_y)}')
        if self.selected_tool in _tools_ladder_element:
            self.add_element(grid_x, grid_y)
        elif self.selected_tool in _tools_ladder_node:
            #vertical line not allowed in first grid index
            if grid_x > 0:
                self.add_node(grid_x, grid_y)
        elif self.selected_tool == 'delete_element':
            self.delete_element(grid_x, grid_y)
        elif self.selected_tool == 'delete_vertical':
            self.delete_node(grid_x, grid_y)
        elif self.selected_tool == 'cursor':
            self.display_settings(grid_x, grid_y)

        self.compiled = False

    def compile(self):
        rungs = model_search(self.ladder_model_grid, self.grid_width)
        self.plc.rungs = rungs
        self.compiled = True

    def update_canvas(self):
        while True:
            for grid in self.ladder_model_grid.values():
                if grid.element is not None:
                    if not isinstance(grid.element, Line): 
                        if self.plc.run == True:
                            update_elements_display(self.canvas, grid)
                        else:
                            hide_elements_display(self.canvas, grid)
            time.sleep(.25)

            if self.close_update_canvas:
                break
        print('Close update canvas thread')

    
_tools_set=('coil', 'contact', 'line_vertical', 'line_horizontal',
                'cursor', 'delete_element', 'delete_vertical')

_tools_ladder_element=('coil', 'contact', 'line_horizontal')
_tools_ladder_node=('line_vertical')

_actions_set=('none', 'start', 'stop')
            
    
        
        