from tkinter import Toplevel, Label, Entry, IntVar
from src.ladder.ladder_elements import * 


#class ElementParameter:

   # def __init__(self, parent, element):

def create_setting_window(parent, element_model):
        top = None 
        #Get ladder object from model
        element = element_model.element
        if isinstance(element, Contact) or isinstance(element, Coil):
            top = Toplevel(parent,width = 700, height = 500)
            label = Label(top, text=element.connected_data_type)
            address = IntVar()
            address.set(element.connected_data_address)
            entry = Entry(top, textvariable=address, justify='center')

            
           

            #entry.insert(0,element.connected_data_address)
            
            label.grid(row=0,column=0, pady=20)
            entry.grid(row=0,column=1,pady=20)

            def on_closing():
                element.connected_data_address = address.get()
                label_text= element.connected_data_type + ' ' + str(element.connected_data_address)
                parent.itemconfig(element_model.label, text= label_text)
                top.destroy()

            top.protocol("WM_DELETE_WINDOW", on_closing)

        return top