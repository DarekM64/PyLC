import customtkinter as ctk
from tkinter import filedialog, Canvas
from CTkMenuBar import *
from canvas_ladder_elements import *







class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PyLC")
        self.geometry("1024x800")

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
       # tk_textbox = tkinter.Text(app, highlightthickness=0)
        #tk_textbox.grid(row=0, column=0, sticky="nsew")
        canvas = Canvas(master=canvas_frame)
        canvas.grid(row=0, column=0, sticky="nsew")
        # create CTk scrollbar
        ctk_canvas_scrollbar = ctk.CTkScrollbar(canvas_frame, command=canvas.yview, )
        ctk_canvas_scrollbar.grid(row=0, column=1, sticky="ns")

        # connect textbox scroll event to CTk scrollbar
        canvas.configure(yscrollcommand=ctk_canvas_scrollbar.set)

        def click_handler(event):
            print(f'x={event.x}, y={event.y}')
            draw_coil(canvas,event.x,event.y)


        canvas.bind("<Button-1>", click_handler)

        



    def open_file(self):
            return filedialog.askopenfilename()
    
    def save_file():
            return filedialog.asksaveasfilename()