from CTkMenuBar import *        
from tkinter import filedialog
from functools import partial

class AppMenu():
        def __init__(self,master):
            menu = CTkMenuBar(master=master)
            button_1 = menu.add_cascade("File")
            button_2 = menu.add_cascade("Edit")
            button_3 = menu.add_cascade("Compile")
            button_4 = menu.add_cascade("Settings")
            button_5 = menu.add_cascade("About")

            dropdown1 = CustomDropdownMenu(widget=button_1)
            dropdown1.add_option(option="Open", command= self.open_file)
            dropdown1.add_option(option="Save", command= self.save_file)

            dropdown1.add_separator()

            sub_menu = dropdown1.add_submenu("Export As")
            sub_menu.add_option(option=".TXT")
            sub_menu.add_option(option=".PDF")

            dropdown2 = CustomDropdownMenu(widget=button_2)
            dropdown2.add_option(option="Cut")
            dropdown2.add_option(option="Copy")
            dropdown2.add_option(option="Paste")

            self.dropdown3 = CustomDropdownMenu(widget=button_3)
            

            dropdown4 = CustomDropdownMenu(widget=button_4)
            dropdown4.add_option(option="Preferences")
            dropdown4.add_option(option="Update")

            dropdown5 = CustomDropdownMenu(widget=button_5)
            dropdown5.add_option(option="PyLC")

            self.menu = menu

        def connectCompile(self, function):#, model, size):
            self.dropdown3.add_option(option="Compile", command=function )#partial(function, model))

        def open_file(self):
            return filedialog.askopenfilename()
    
        def save_file(self):
            return filedialog.asksaveasfilename()
        

        
