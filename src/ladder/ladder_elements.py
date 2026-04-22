

class Element():
    '''Single element in ladder'''
    def __init__(self, type='basic'):
        self.connected_elements = set()
        self.type = type
        self.normal_open:bool = True
        self.connected_data = [True]
        
    def get_value(self):
        if self.normal_open==True:
            return self.connected_data[0]
        else:
            return not self.connected_data[0]
    


class Coil(Element):
    def __init__(self, connected_data_type='M', connected_data_address: int=0, normal_open: bool=True, connected_data=[True]):
        self.type ='coil'
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
        self.normal_open = normal_open
        self.reached:bool = False
        self.connected_data = connected_data
    
    def __getstate__(self):
        """Define what to pickle."""
        state = self.__dict__.copy()
        # Remove non-picklable attributes
        del state['reached']
        del state['connected_data']
        return state
    
    def __setstate__(self, state):
            """Define how to restore from pickle."""
            self.__dict__.update(state)
            self.reached = False
            self.connected_data = [True]
     
class Contact(Element):
    def __init__(self, connected_data_type='M', connected_data_address: int=0, normal_open: bool=True, connected_data=[True]):
        self.connected_elements = set()
        self.type ='contact'
        self.connected_data_type = connected_data_type
        self.connected_data_address = connected_data_address
        self.normal_open = normal_open
        self.reached:bool = False
        self.connected_data = connected_data

    def __getstate__(self):
        """Define what to pickle."""
        state = self.__dict__.copy()
        # Remove non-picklable attributes
        del state['connected_elements']
        del state['reached']
        del state['connected_data']
        return state
    
    def __setstate__(self, state):
        """Define how to restore from pickle."""
        self.__dict__.update(state)
        self.connected_elements = set()
        self.reached = False
        self.connected_data = [True]

    
class Line(Element):
    def __init__(self):
        self.type ='line'
        self.connected_elements = set()
        self.reached = False

    def get_value(self):
        return True
    
    def __getstate__(self):
        """Define what to pickle."""
        state = self.__dict__.copy()
        # Remove non-picklable attributes
        del state['connected_elements']
        del state['reached']
        return state

    def __setstate__(self, state):
        """Define how to restore from pickle."""
        self.__dict__.update(state)
        self.connected_elements = set()
        self.reached = False

class Node(Element):
    def __init__(self):
        self.type = 'node'
        self.connected_elements = set()
        self.reached = False

    def __getstate__(self):
        """Define what to pickle."""
        state = self.__dict__.copy()
        # Remove non-picklable attributes
        del state['connected_elements']
        del state['reached']
        return state

    def __setstate__(self, state):
        """Define how to restore from pickle."""
        self.__dict__.update(state)
        self.connected_elements = set()
        self.reached = False


'''types of elements in graphic ladder:
    contact, coil, node split, node join, line vertical, function block
'''

class Rung():
    '''List of elements creating rung'''
    def __init__(self, start_element=None, outputs=None):
        self.start_element = start_element
        self.coils=set() #creates empty list of Coils affected by rung

class Program():
    '''List of rungs creating program'''
    def __init__(self):
        self.rungs=[]