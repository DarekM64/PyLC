from src.ladder.ladder_elements import *
from src.plc.plc import *

class Model():
    '''Connects data for graphic presentation and rung logic
        ladder_model_grid:  list of elements tied to [x][y] node
                            this provides data to create plc rung logic
                            and canvas drawing
    '''
    def __init__(self, rows=20, cols=16):
        self.initialize_program(rows, cols)
        self.plc=PLC()
        self.selected_tool='coil'
        self.selected_action='none'

    def set_Selected_Element(self, selected_element):
        self.selected_element = selected_element

    def initialize_program(self,rows, cols):
        '''Creates empty list of elements for clean ladder'''
        self.ladder_model_grid = [['Empty' for j in range(cols)] for i in range(rows)]

    
    def select_tool(self, tool):
        self.selected_tool=tool
            
    def select_plc_action(self, action):
        self.selected_action=action


    def set_element(self, grid_x, grid_y, element):
        new_element=None
        if element=='contact':
            new_element= Contact()
        if element=='coil':
            new_element= Coil()
        self.ladder_model_grid[grid_x][grid_y] = new_element

    def get_element(self, grid_x, grid_y):
        return self.ladder_model_grid[grid_x][grid_y]
    
_tools_set=('coil', 'contact', 'node', 'vertical_line', 'horizontal_line',
            'cursor', 'delete')

_actions_set=('none', 'start', 'stop')
            