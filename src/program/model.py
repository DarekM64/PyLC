from src.ladder.ladder_elements import *
from src.plc.plc import *

class Model():
    def __init__(self, rows=20, cols=16):
        self.initialize_program(rows, cols)
        self.plc=PLC()

    def set_Selected_Element(self, selected_element):
        self.selected_element = selected_element

    def initialize_program(self,rows, cols):
        self.ladder_model_grid = [['Empty' for j in range(cols)] for i in range(rows)]

    
  


    def set_element(self, grid_x, grid_y, element):
        new_element=None
        if element=='contact':
            new_element= Contact()
        self.ladder_model_grid[grid_x][grid_y] = new_element

    def get_element(self, grid_x, grid_y):
        return self.ladder_model_grid[grid_x][grid_y]