from src.program.model import *

from src.ladder.ladder_elements import *
from src.ladder.ladder_solver import *

__search_call_counter:int = 0

def model_search(ladder_model_grid, size):
    '''Creating rungs from model presentation'''
    print('Search model !')
    rungs=[]
    rungs_ids=[]
    delete_connections(ladder_model_grid)
    for x in range(size):
        if (x, 0) in ladder_model_grid:
            global __search_call_counter
            __search_call_counter = 0
            start_element=ladder_model_grid[x, 0].element
            rung = Rung(start_element)

            search_element(x, 0, ladder_model_grid, start_element, rung)
            rungs.append(rung)
            rungs_ids.append(ladder_model_grid[x, 0].pos_x)

    return rungs, rungs_ids

def search_element(grid_x, grid_y, ladder_model_grid, element,rung:Rung):
    '''Check if element is connected with elements and search deeper if needed'''

    global __search_call_counter
    __search_call_counter += 1
    print(f'__search_call_counter:{__search_call_counter}')

    #If there is node on the right connect it to element
    element_to_right=(grid_x, grid_y+1)
    if (element_to_right) in ladder_model_grid:
        if ladder_model_grid[element_to_right].node is not None:
            element.connected_elements.add(ladder_model_grid[element_to_right].node)
            search_node(*element_to_right, ladder_model_grid, ladder_model_grid[element_to_right].node, rung)
        #If there is element on the right connect it to element
        elif ladder_model_grid[element_to_right].element is not None:
            element.connected_elements.add(ladder_model_grid[element_to_right].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[element_to_right].element,Coil):
                rung.coils.add(ladder_model_grid[element_to_right].element)
            else:
                search_element(*element_to_right, ladder_model_grid, ladder_model_grid[element_to_right].element, rung)

    #If there is node 'join' type on right up grid next to element
    if (grid_x-1, grid_y+1) in ladder_model_grid:
        if ladder_model_grid[grid_x-1, grid_y+1].node is not None:
            element.connected_elements.add(ladder_model_grid[grid_x-1, grid_y+1].node)
            search_node(grid_x-1, grid_y+1, ladder_model_grid, ladder_model_grid[grid_x-1, grid_y+1].node, rung)

def search_node(grid_x:int, grid_y:int, ladder_model_grid, node, rung:Rung):
    '''Check if node is connected with elements and search deeper if needed'''
    global __search_call_counter
    __search_call_counter += 1
    print(f'__search_call_counter:{__search_call_counter}')
    #If there is element on same grid connect node to it
    if (grid_x, grid_y) in ladder_model_grid:
        if ladder_model_grid[grid_x, grid_y].element is not None:
            node.connected_elements.add(ladder_model_grid[grid_x, grid_y].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[grid_x, grid_y].element,Coil):
                rung.coils.add(ladder_model_grid[grid_x, grid_y].element)
            else:
                search_element(grid_x, grid_y, ladder_model_grid, ladder_model_grid[grid_x, grid_y].element, rung)
    
    #If there is node below node connect to node
    if (grid_x+1, grid_y) in ladder_model_grid:
        if ladder_model_grid[grid_x+1, grid_y].node is not None:
            node.connected_elements.add(ladder_model_grid[grid_x+1, grid_y].node)
            search_node(grid_x+1, grid_y, ladder_model_grid, ladder_model_grid[grid_x+1, grid_y].node, rung)
        #It there is no node but element connect to element
        elif ladder_model_grid[grid_x+1, grid_y].element is not None:
            node.connected_elements.add(ladder_model_grid[grid_x+1, grid_y].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[grid_x+1, grid_y].element,Coil):
                rung.coils.add(ladder_model_grid[grid_x+1, grid_y].element)
            else:
                search_element(grid_x+1, grid_y, ladder_model_grid, ladder_model_grid[grid_x+1, grid_y].element, rung)



    

    
def delete_connections(ladder_model_grid):
     for grid in ladder_model_grid.values():
          if grid.element is not None:
               grid.element.connected_elements = set()
          if grid.node is not None:
               grid.node.connected_elements = set()
