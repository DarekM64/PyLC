import customtkinter as ctk
from tkinter import filedialog


from tkinter import *

#in project imports
#visual
from src.visualization.menu import AppMenu
from src.visualization.tools import create_frame_tools

from src.visualization.canvas_elements import *
from ladder_canvas import create_fields
from src.program.model import Model
from tool_button import create_button
from element_parameter import create_setting_window


#TODO Clean class for more organized code
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        menu = AppMenu(self)
        #program
        ladder_grid= Model()
        
        self.title("PyLC")
        self.geometry("1060x800")

        #Functions

        
        
        #frames inside main window, tool section bar, scrollable canvas below for creating ladder

        tools_frame = create_frame_tools(self)
        canvas_frame = ctk.CTkFrame(master=self,
                                    bg_color='green',
                                    fg_color='green',)


        
        canvas_frame.pack(side='bottom',fill='both', expand=True)

        canvas_frame.grid_rowconfigure(0, weight=1) 
        canvas_frame.grid_columnconfigure(0, weight=1)

        # create scrollable textbox
        canvas = Canvas(master=canvas_frame,scrollregion=(0,0,1000,3000))
        canvas.grid(row=0, column=0, sticky="nsew",padx=0,pady=0)
        # create CTk scrollbar
        ctk_canvas_scrollbar = ctk.CTkScrollbar(canvas_frame, command=canvas.yview, )
        ctk_canvas_scrollbar.grid(row=0, column=1, sticky="ns")

        # connect textbox scroll event to CTk scrollbar
        canvas.configure(yscrollcommand=ctk_canvas_scrollbar.set)
        self.element_settings = None
        self.field_width=80
        self.field_height=80
        self.field_padding=0
        self.field_list = create_fields(canvas, 
                                        rows=LADDER_ROWS,
                                        cols=LADDER_COLUMNS,
                                        x_size=self.field_width, y_size = self.field_width, padding = self.field_padding)
        
        def click_handler(event):
            '''calculate x,y index  of clickecd field'''
            print(f'x={event.x}, y={event.y}')


            x_width = self.field_width + self.field_padding
            y_height = self.field_height + self.field_padding
            aligned_x = event.x - (event.x-1) % x_width
            aligned_y = event.y - event.y % y_height + self.field_width//2
            print(f'To function x:{(event.y-1) // y_height}, y:{(event.x-1) // x_width}')

            if self.selected_tool !='pointer':
                ladder_grid.set_element((event.y-1) // y_height, (event.x-1) // x_width, self.selected_tool)
                draw_element(canvas, aligned_x, aligned_y, shape_type=self.selected_tool)      
            else:
                if self.element_settings is not None:
                   self.element_settings.destroy()
                element = ladder_grid.get_element((event.y-1) // y_height, (event.x-1) // x_width)
                self.element_settings = create_setting_window(canvas,element)
                geometry_string=f'+{event.x}+{int(event.y+tools_frame._current_height)}'
                self.element_settings.geometry(geometry_string)
            #draw_coil(canvas,aligned_x,aligned_y)


        canvas.bind("<Button-1>", click_handler)

        self.selected_tool='coil'
        self.selected_action='none'
        def select_tool(tool):
              self.selected_tool=tool
              print(self.selected_tool)
        def select_plc_action(action):
              self.selected_action=action
              



        button1.bind("<Button-1>", lambda event: select_tool('coil'))
        button2.bind("<Button-1>", lambda event: select_tool('contact'))
        button3.bind("<Button-1>", lambda event: select_tool('line'))
        button4.bind("<Button-1>", lambda event: select_tool('split'))
        button5.bind("<Button-1>", lambda event: select_tool('join'))
        button6.bind("<Button-1>", lambda event: select_tool('clear'))
        button7.bind("<Button-1>", lambda event: select_tool('pointer'))

        

        button_plc_1.bind("<Button-1>", lambda event: select_plc_action('stop'))
        button_plc_2.bind("<Button-1>", lambda event: select_plc_action('start'))

        



    