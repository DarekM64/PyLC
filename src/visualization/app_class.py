import customtkinter as ctk
from tkinter import filedialog


from tkinter import *

#in project imports
#visual
from src.visualization.menu import AppMenu
from src.visualization.tools import create_frame_tools
from src.visualization.workspace_canvas import init_workspace

from src.visualization.canvas_elements import *
from src.program.model import Model

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        menu = AppMenu(self)
        #Core app program
        self.ladder_model= Model()
        
        menu.connectCompile(self.ladder_model.compile)
        menu.connectExportJson(self.ladder_model.save_to_json)
        menu.connectImportJson(self.ladder_model.read_from_json)
        self.title("PyLC")
        self.geometry("1060x800")

        #Frames inside main window, tool section bar, scrollable canvas below for creating ladder

        self.tools_frame = create_frame_tools(self)
        _list_buttons = self.tools_frame.winfo_children()
        _list_buttons[0].bind("<Button-1>", lambda event: self.ladder_model.select_tool('coil'))
        _list_buttons[1].bind("<Button-1>", lambda event: self.ladder_model.select_tool('contact'))
        _list_buttons[2].bind("<Button-1>", lambda event: self.ladder_model.select_tool('line_horizontal'))
        _list_buttons[3].bind("<Button-1>", lambda event: self.ladder_model.select_tool('line_vertical'))
        _list_buttons[4].bind("<Button-1>", lambda event: self.ladder_model.select_tool('delete_element'))
        _list_buttons[5].bind("<Button-1>", lambda event: self.ladder_model.select_tool('delete_vertical'))
        _list_buttons[6].bind("<Button-1>", lambda event: self.ladder_model.select_tool('cursor'))
        _list_buttons[7].bind("<Button-1>", lambda event: self.ladder_model.select_plc_action('stop'))
        _list_buttons[8].bind("<Button-1>", lambda event: self.ladder_model.select_plc_action('start'))

        canvas_frame = init_workspace(self)
        self.ladder_model.attach_canvas(canvas_frame)
        self.element_settings = None
        self.ladder_model.initialize_program(20, 16, 80)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        '''
        Called when a window closes.
        Sets conditions for other application threads to terminate properly.
        '''
        print('!!! EXIT EVENT !!!')
        self.ladder_model.plc.close_thread = True
        self.ladder_model.close_update_canvas = True
        self.destroy()
       
        
              

        
        
            

    

        

        



    