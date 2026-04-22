from CTkMenuBar import *        
from tkinter import filedialog

class AppMenu():
        def __init__(self,master):
            menu = CTkMenuBar(master=master)
            button_1 = menu.add_cascade("File")
            button_2 = menu.add_cascade("Edit")
            button_3 = menu.add_cascade("Compile")
            button_4 = menu.add_cascade("Settings")
            button_5 = menu.add_cascade("About")

            self.dropdown1 = CustomDropdownMenu(widget=button_1)
            #self.dropdown1.add_option(option="Open", command= self.open_file)
            #self.dropdown1.add_option(option="Save", command= self.save_file)

            self.dropdown1.add_separator()

            self.sub_menu = self.dropdown1.add_submenu("Export As")
            self.sub_menu.add_option(option=".TXT")
            self.sub_menu.add_option(option=".PDF")

            #TODO create cut copy paste mechanic
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

        def connectCompile(self, function):
            self.dropdown3.add_option(option="Compile", command=function )#partial(function, model))
        
        def connectExportJson(self, function):
            self.dropdown1.add_option(option="Save ladder to Json", command=function )

        def connectImportJson(self, function):
            self.dropdown1.add_option(option="Read ladder from Json", command=function )


        

        
