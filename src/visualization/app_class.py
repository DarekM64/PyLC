import customtkinter as ctk
from tkinter import filedialog


from tkinter import *

#in project imports
#visual
from src.visualization.menu import AppMenu
from src.visualization.tools import create_frame_tools
from src.visualization.workspace_canvas import init_workspace

from src.visualization.canvas_elements import *
from ladder_canvas import create_fields
from src.program.model import Model
from element_parameter import create_setting_window
from src.program.model_search import model_search

#TODO Clean class for more organized code
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        menu = AppMenu(self)
        
        #program
        self.ladder_model= Model()
        
        menu.connectCompile(model_search, self.ladder_model.ladder_model_grid)
        self.title("PyLC")
        self.geometry("1060x800")

        
        #frames inside main window, tool section bar, scrollable canvas below for creating ladder

        self.tools_frame = create_frame_tools(self)
        _list_buttons = self.tools_frame.winfo_children()
        _list_buttons[0].bind("<Button-1>", lambda event: self.ladder_model.select_tool('coil'))
        _list_buttons[1].bind("<Button-1>", lambda event: self.ladder_model.select_tool('contact'))
        _list_buttons[2].bind("<Button-1>", lambda event: self.ladder_model.select_tool('line_horizontal'))
        _list_buttons[3].bind("<Button-1>", lambda event: self.ladder_model.select_tool('line_vertical'))
        _list_buttons[4].bind("<Button-1>", lambda event: self.ladder_model.select_tool('delete_element'))
        _list_buttons[5].bind("<Button-1>", lambda event: self.ladder_model.select_tool('delete_vertical'))
        _list_buttons[6].bind("<Button-1>", lambda event: self.ladder_model.select_tool('cursor'))
        _list_buttons[7].bind("<Button-1>", lambda event: self.ladder_model.select_tool('stop'))
        _list_buttons[8].bind("<Button-1>", lambda event: self.ladder_model.select_tool('start'))

        canvas_frame = init_workspace(self)
        self.ladder_model.attach_canvas(canvas_frame)
        self.element_settings = None
        self.ladder_model.initialize_program(20, 16, 80)
        
        # def click_handler(event):
        #     '''calculate x,y index  of clickecd field'''
        #     print(f'x={event.x}, y={event.y}')


        #     x_width = self.field_width + self.field_padding
        #     y_height = self.field_height + self.field_padding
        #     aligned_x = event.x - (event.x-1) % x_width
        #     aligned_y = event.y - event.y % y_height + self.field_width//2
        #     print(f'To function x:{(event.y-1) // y_height}, y:{(event.x-1) // x_width}')

        #     if self.selected_tool !='pointer':
        #         ladder_grid.set_element((event.y-1) // y_height, (event.x-1) // x_width, self.selected_tool)
        #         draw_element(canvas, aligned_x, aligned_y, shape_type=self.selected_tool)      
        #     else:
        #         if self.element_settings is not None:
        #            self.element_settings.destroy()
        #         element = ladder_grid.get_element((event.y-1) // y_height, (event.x-1) // x_width)
        #         self.element_settings = create_setting_window(canvas,element)
        #         geometry_string=f'+{event.x}+{int(event.y+tools_frame._current_height)}'
        #         self.element_settings.geometry(geometry_string)
        #     #draw_coil(canvas,aligned_x,aligned_y)


        # canvas.bind("<Button-1>", click_handler)

       
        
              

        
        
            

    

        

        



    