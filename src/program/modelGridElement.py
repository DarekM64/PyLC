class ModelGridElement():

    def __init__(self,pos_x, pos_y, element_canvas_id=None, element=None, node_canvas_id=None, node = None, label = None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.element_canvas_id=element_canvas_id
        self.element_canvas_value = None
        self.element = element
        self.node_canvas_id=node_canvas_id
        self.node = node
        self.label = label
        