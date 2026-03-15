class Element():
    '''Single element in ladder'''
    def __init__(self,connected_data=None, type='basic'):
        self.connected_elements = []
        self.type = type
        self.connected_data = connected_data
    
class Coil(Element):
     def __init__(self,connected_data=None, type='coil'):
        Element.__init__(self,connected_data, type)

        self.reached = False
     
class Contact(Element):
    def __init__(self,connected_data=None, type='contact',coil_type='NO'):
        self.coil_type=coil_type
        Element.__init__(self,connected_data, type)
    
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
        self.coils=list[Coil] = list() #creates empty list of Coils affected by rung

class Program():
    '''List of rungs creating program'''
    def __init__(self):
        self.rungs=[]