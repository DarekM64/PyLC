class ModelGridElement():
    '''Class used in model, represents 1 square.
        Hold element displayed in workspace canvas.
        Hold element data adress.
        Hold node (vertical line).
        Used to build rung program on compile.
    '''
    def __init__(self,pos_x, pos_y, element_canvas_id=None, element=None, node_canvas_id=None, node = None, label = None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.element_canvas_id=element_canvas_id
        self.element_canvas_value = None
        self.element = element
        self.node_canvas_id=node_canvas_id
        self.node = node
        self.label = label

    def __getstate__(self):
        """Define what to pickle."""
        state = self.__dict__.copy()
        # Remove non-picklable attributes
        del state['element_canvas_id']
        del state['element_canvas_value']
        del state['node_canvas_id']
        del state['label']
        return state

    def __setstate__(self, state):
        """Define how to restore from pickle."""
        self.__dict__.update(state)
        # Initialize after unpickling
        self.element_canvas_id = None   
        self.element_canvas_value = None   
        self.node_canvas_id = None   
        self.label = None   
