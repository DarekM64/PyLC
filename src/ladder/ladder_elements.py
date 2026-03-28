class Element():
    '''Single element in ladder'''
    def __init__(self,type='basic'):
        self.connected_elements = []
        self.type = type
        
    
class Coil(Element):
    def __init__(self, connected_data_type='M', connected_data_address: int=0):
        self.type='coil'
        self.connected_elements = []
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
        self.reached = False
     
class Contact(Element):
    def __init__(self, connected_data_type='M', connected_data_address: int=0, coil_type='NO'):
        self.type='contact'
        self.coil_type=coil_type
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
    
    def get_value(self):
        if self.coil_type=='NO':
            return self.connected_data
        elif self.coil_type=='NC':
            return not self.connected_data
        return self.connected_data


'''types of elements in graphic ladder:
    contact, coil, node split, node join, line vertical, function block
'''

class Rung():
    '''List of elements creating rung'''
    def __init__(self,start_element=None, outputs=None):
        self.start_element = start_element
        self.coils=[] #creates empty list of Coils affected by rung

class Program():
    '''List of rungs creating program'''
    def __init__(self):
        self.rungs=[]