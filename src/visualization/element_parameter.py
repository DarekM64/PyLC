from tkinter import Toplevel, Label, Entry
from src.ladder.ladder_elements import * 


#class ElementParameter:

   # def __init__(self, parent, element):

def create_setting_window(parent, element):
        top = None 

        if isinstance(element, Contact):
            top = Toplevel(parent,width = 500, height = 300)
            Label(top, text=element.connected_data_type).pack()
            Entry(top, show=element.connected_data_address).pack()


        return top