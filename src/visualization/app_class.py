import customtkinter as ctk
from tkinter import filedialog
from CTkMenuBar import *

from tkinter import *

#in project imports
from src.visualization.canvas_elements import *
from ladder_canvas import create_fields
from src.program.model import Ladder_grid
from tool_button import create_button


LADDER_ROWS = 20
LADDER_COLUMNS = 16

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #program
        ladder_grid= Ladder_grid(rows=LADDER_ROWS, cols=LADDER_COLUMNS)
        
        self.title("PyLC")
        self.geometry("1060x800")

        #Functions

        menu = CTkMenuBar(master=self)
        button_1 = menu.add_cascade("File")
        button_2 = menu.add_cascade("Edit")
        button_3 = menu.add_cascade("Settings")
        button_4 = menu.add_cascade("About")

        dropdown1 = CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="Open", command=self.open_file)
        dropdown1.add_option(option="Save")

        dropdown1.add_separator()

        sub_menu = dropdown1.add_submenu("Export As")
        sub_menu.add_option(option=".TXT")
        sub_menu.add_option(option=".PDF")

        dropdown2 = CustomDropdownMenu(widget=button_2)
        dropdown2.add_option(option="Cut")
        dropdown2.add_option(option="Copy")
        dropdown2.add_option(option="Paste")

        dropdown3 = CustomDropdownMenu(widget=button_3)
        dropdown3.add_option(option="Preferences")
        dropdown3.add_option(option="Update")

        dropdown4 = CustomDropdownMenu(widget=button_4)
        dropdown4.add_option(option="Hello World")
        
        #frames inside main window, tool section bar, scrollable canvas below for creating ladder

        tools_frame = ctk.CTkFrame(master=self,
                                   height=100,
                                   bg_color='dark grey',
                                   fg_color='dark grey')
        canvas_frame = ctk.CTkFrame(master=self,
                                    bg_color='green',
                                    fg_color='green',)


        tools_frame.pack(side='top',fill='x')
        canvas_frame.pack(side='bottom',fill='both', expand=True)

        canvas_frame.grid_rowconfigure(0, weight=1) 
        canvas_frame.grid_columnconfigure(0, weight=1)

        # create scrollable textbox
        #tk_textbox = tkinter.Text(app, highlightthickness=0)
        #tk_textbox.grid(row=0, column=0, sticky="nsew")
        canvas = Canvas(master=canvas_frame,scrollregion=(0,0,1000,3000))
        canvas.grid(row=0, column=0, sticky="nsew",padx=0,pady=0)
        # create CTk scrollbar
        ctk_canvas_scrollbar = ctk.CTkScrollbar(canvas_frame, command=canvas.yview, )
        ctk_canvas_scrollbar.grid(row=0, column=1, sticky="ns")

        # connect textbox scroll event to CTk scrollbar
        canvas.configure(yscrollcommand=ctk_canvas_scrollbar.set)
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
            ladder_grid.set_element((event.y-1) // y_height, (event.x-1) // x_width)
            if self.selected_tool !='pointer':
                draw_element(canvas, aligned_x, aligned_y, shape_type=self.selected_tool)
            #draw_coil(canvas,aligned_x,aligned_y)


        canvas.bind("<Button-1>", click_handler)

        self.selected_tool='coil'
        self.selected_action='none'
        def select_tool(tool):
              self.selected_tool=tool
              print(self.selected_tool)
        def select_plc_action(action):
              self.selected_action=action
              

        button1=create_button(tools_frame,shape_type='coil',size = 80)
        button2=create_button(tools_frame,shape_type='contact',size = 80)
        button3=create_button(tools_frame,shape_type='line',size = 80)
        button4=create_button(tools_frame,shape_type='split',size = 80)
        button5=create_button(tools_frame,shape_type='join',size = 80)
        button6=create_button(tools_frame,shape_type='clear',size = 80)
        button7=create_button(tools_frame,shape_type='pointer',size = 80)

        button1.bind("<Button-1>", lambda event: select_tool('coil'))
        button2.bind("<Button-1>", lambda event: select_tool('contact'))
        button3.bind("<Button-1>", lambda event: select_tool('line'))
        button4.bind("<Button-1>", lambda event: select_tool('split'))
        button5.bind("<Button-1>", lambda event: select_tool('join'))
        button6.bind("<Button-1>", lambda event: select_tool('clear'))
        button7.bind("<Button-1>", lambda event: select_tool('pointer'))
        tools_frame.grid_rowconfigure(0, weight=1) 
        tools_frame.grid_columnconfigure(0, weight=1)
        button1.grid(row=0, column=0,padx=5,pady=5, sticky='e')
        button2.grid(row=0, column=1,padx=5,pady=5, sticky='e')
        button3.grid(row=0, column=2,padx=5,pady=5, sticky='e')
        button4.grid(row=0, column=3,padx=5,pady=5, sticky='e')
        button5.grid(row=0, column=4,padx=5,pady=5, sticky='e')
        button6.grid(row=0, column=5,padx=5,pady=5, sticky='e')
        button7.grid(row=0, column=6,padx=5,pady=5, sticky='e')
        
        button_plc_1=create_button(tools_frame,shape_type='stop',size = 80)
        button_plc_2=create_button(tools_frame,shape_type='start',size = 80)
        button_plc_1.bind("<Button-1>", lambda event: select_plc_action('stop'))
        button_plc_2.bind("<Button-1>", lambda event: select_plc_action('start'))

        button_plc_1.grid(row=0, column=7,padx=5,pady=5, sticky='e')
        button_plc_2.grid(row=0, column=8,padx=5,pady=5, sticky='e')



    def open_file(self):
            return filedialog.askopenfilename()
    
    def save_file():
            return filedialog.asksaveasfilename()