class Element():
    '''Single element in ladder'''
    def __init__(self, type='basic'):
        self.connected_elements = []
        self.type = type
        self.normal_open:bool = True
        self.connected_data = True
        
    def get_value(self):
        if self.normal_open==True:
            return self.connected_data
        else:
            return not self.connected_data
    


class Coil(Element):
    def __init__(self, connected_data_type='M', connected_data_address: int=0, normal_open: bool=True):
        self.type ='coil'
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
        self.normal_open = normal_open
        self.reached:bool = False
        self.connected_data = True
     
class Contact(Element):
    #TODO add reading data from PLC
    def __init__(self, connected_data_type='M', connected_data_address: int=0, normal_open: bool=True):
        self.connected_elements = []
        self.type ='contact'
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
        self.normal_open = normal_open
        self.reached:bool = False
        self.connected_data = True
    
class Line(Element):
    def __init__(self):
        self.type ='line'
        self.connected_elements = []
        self.reached = False

    def get_value(self):
        return True

class Node(Element):
    def __init__(self):
        self.type = 'node'
        self.connected_elements = []
        self.reached = False


'''types of elements in graphic ladder:
    contact, coil, node split, node join, line vertical, function block
'''

class Rung():
    '''List of elements creating rung'''
    def __init__(self, start_element=None, outputs=None):
        self.start_element = start_element
        self.coils=[] #creates empty list of Coils affected by rung

class Program():
    '''List of rungs creating program'''
    def __init__(self):
        self.rungs=[]