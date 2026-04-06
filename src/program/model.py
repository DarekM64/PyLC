from src.ladder.ladder_elements import *
from src.plc.plc import *

from src.program.model_visualizer import *
import src.visualization.canvas_elements as canvas_elements

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




    def get_element(self, grid_x, grid_y):
        return self.ladder_model_grid[grid_x][grid_y]
    
    def add_element(self,grid_x, grid_y):
        canvas_x,canvas_y= calc_position_element(grid_x, grid_y, self.grid_width)
        #group of elements managed similar way in model
        if self.selected_tool in _tools_ladder_element:
            #Create ladder logic element and canvas elements.  
            match self.selected_tool:
                case 'contact':
                    element=Contact()
                    ids=draw_contact(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)  
                case 'coil':
                    element=Coil()  
                    ids=draw_coil(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)  
                case 'line_horizontal':
                    element=Line()  
                    ids=draw_horizontal_line(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)  
               
            
            #Element exist, remove old add new one
            if (grid_x,grid_y) in self.ladder_model_grid:
                if self.ladder_model_grid[(grid_x, grid_y)].element != None:
                    delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id)
                    self.ladder_model_grid[(grid_x, grid_y)].element = element
                    self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id = ids
                else:
                    #node exist, but no element in grid, add new one       
                    self.ladder_model_grid[(grid_x, grid_y)].element = element
                    self.ladder_model_grid[(grid_x, grid_y)].element_canvas_id = ids
            #No element or node, create new grid element
            else:
                modelGridElement = ModelGridElement(grid_x, grid_y, element_canvas_id=ids, element=element)
                self.ladder_model_grid[(grid_x, grid_y)]=modelGridElement

        #group of elements managedd similwar way in model
        elif self.selected_tool in _tools_ladder_node:
            node = Line()
            ids=draw_vertical_line(self.canvas, canvas_x, canvas_y, color='black',  size = self.grid_width)

            if (grid_x,grid_y) in self.ladder_model_grid:
                if self.ladder_model_grid[(grid_x, grid_y)].element != None:
                    delete_canvas_elements(self.canvas, self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id)
                    self.ladder_model_grid[(grid_x, grid_y)].node = node
                    self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id = ids
                else:
                    #node exist, but no element in grid, add new one       
                    self.ladder_model_grid[(grid_x, grid_y)].element = element
                    self.ladder_model_grid[(grid_x, grid_y)].node_canvas_id = ids
            #No element or node, create new grid element
            else:
                modelGridElement = ModelGridElement(grid_x, grid_y, node_canvas_id=ids, node=node)
                self.ladder_model_grid[(grid_x, grid_y)]=modelGridElement

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
        grid_x = x//self.grid_width
        grid_y = y//self.grid_width
        print(f'grid_x={grid_x}, grid_y={grid_y}')

        print(f'element exist:{self.check_element_exist(grid_x, grid_y)}')
        if self.selected_tool in _tools_ladder_element or self.selected_tool in _tools_ladder_node:
            self.add_element(grid_x, grid_y)

        # if self.selected_tool !='pointer':
        #     ladder_grid.set_element((event.y-1) // y_height, (event.x-1) // x_width, self.selected_tool)
        #     draw_element(canvas, aligned_x, aligned_y, shape_type=self.selected_tool)      
        # else:
        #     if self.element_settings is not None:
        #         self.element_settings.destroy()
        #     element = ladder_grid.get_element((event.y-1) // y_height, (event.x-1) // x_width)
        #     self.element_settings = create_setting_window(canvas,element)
        #     geometry_string=f'+{event.x}+{int(event.y+tools_frame._current_height)}'
        #     self.element_settings.geometry(geometry_string)
        #draw_coil(canvas,aligned_x,aligned_y)


        
    
_tools_set=('coil', 'contact', 'line_vertical', 'line_horizontal',
                'cursor', 'delete_element', 'delete_vertical')

_tools_ladder_element=('coil', 'contact', 'line_horizontal')
_tools_ladder_node=('line_vertical')

_actions_set=('none', 'start', 'stop')
            
class ModelGridElement():

    def __init__(self,pos_x, pos_y, element_canvas_id=None, element=None, node_canvas_id=None, node = None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.element_canvas_id=element_canvas_id
        self.element = element
        self.node_canvas_id=node_canvas_id
        self.node = node
        