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

def create_setting_window2(parent, element_model, plc, x, y):
        top = None 
        #Get ladder object from model
        element = element_model.element
        if isinstance(element, Contact) or isinstance(element, Coil):
            top = Toplevel(parent,width = 400, height = 150)
            parent_x = parent.winfo_rootx()
            parent_y = parent.winfo_rooty()
            print(f'Parent x:{parent_x}, y:{parent_y}')
            x_set = int(parent_x + x)
            y_set = int(parent_y + y)
            #geometry_string=f'400x150+{int(x)}+{int(y)}'
            geometry_string=f'400x150+{x_set}+{y_set}'
            top.geometry(geometry_string)
            label = Label(top, text=element.connected_data_type)
            address = IntVar()
            address.set(element.connected_data_address)
            entry = Entry(top, textvariable=address, justify='center')

            
           

            #entry.insert(0,element.connected_data_address)
            
            label.grid(row=0,column=0, pady=20)
            entry.grid(row=0,column=1,pady=20)

            def on_closing():
                element.connected_data_address = address.get()
                element.connected_data = plc.bind_data(element.connected_data_type, element.connected_data_address)
                label_text= element.connected_data_type + ' ' + str(element.connected_data_address)
                parent.itemconfig(element_model.label, text= label_text)
                top.destroy()

            top.protocol("WM_DELETE_WINDOW", on_closing)

        return top