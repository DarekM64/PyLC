from src.ladder.ladder_elements import *

class Ladder_grid():
    def __init__(self, rows=20, cols=16):
        self.initialize_program(rows, cols)
        self.selected_element='Coil'

    def set_Selected_Element(self, selected_element):
        self.selected_element = selected_element

    def initialize_program(self,rows, cols):
        self.ladder_model_grid = [['Empty' for j in range(cols)] for i in range(rows)]

    
  


    def set_element(self, grid_x, grid_y):
        self.ladder_model_grid[grid_x][grid_y] = self.selected_element

