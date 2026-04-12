

from src.program.model import *

from src.ladder.ladder_elements import *
from src.ladder.ladder_solver import *



def model_search(ladder_model_grid, size):
    '''Creating rungs from model presentation'''
    print('Search model !')
    rungs=[]
    rungs_ids=[]
    delete_connections(ladder_model_grid)
    for x in range(size):
        if (x, 0) in ladder_model_grid:
            start_element=ladder_model_grid[x, 0].element
            rung = Rung(start_element)
            
            
            search_element(x, 0, ladder_model_grid, start_element, rung)

            #solve_rung(rung)
            #for coil in rung.coils:
                #print(f'coil data: {coil.connected_data}')

            rungs.append(rung)
            rungs_ids.append(ladder_model_grid[x, 0].pos_x)

    return rungs, rungs_ids

def search_element(grid_x, grid_y, ladder_model_grid, element,rung:Rung):
    '''Check if element is connected with elements and search deeper if needed'''
    #If there is node on the right connect it to element
    if (grid_x, grid_y+1) in ladder_model_grid:
        if ladder_model_grid[grid_x, grid_y+1].node is not None:
            element.connected_elements.append(ladder_model_grid[grid_x, grid_y+1].node)
            search_node(grid_x, grid_y+1, ladder_model_grid, ladder_model_grid[grid_x, grid_y+1].node, rung)
        #If there is element on the right connect it to element
        elif ladder_model_grid[grid_x, grid_y+1].element is not None:
            element.connected_elements.append(ladder_model_grid[grid_x, grid_y+1].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[grid_x, grid_y+1].element,Coil):
                rung.coils.append(ladder_model_grid[grid_x, grid_y+1].element)
            else:
                search_element(grid_x, grid_y+1, ladder_model_grid, ladder_model_grid[grid_x, grid_y+1].element, rung)

def search_node(grid_x, grid_y, ladder_model_grid, node, rung:Rung):
    '''Check if node is connected with elements and search deeper if needed'''
    #If there is element on same grid connect node to it
    if (grid_x, grid_y) in ladder_model_grid:
        if ladder_model_grid[grid_x, grid_y].element is not None:
            node.connected_elements.append(ladder_model_grid[grid_x, grid_y].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[grid_x, grid_y].element,Coil):
                rung.coils.append(ladder_model_grid[grid_x, grid_y].element)
            else:
                search_element(grid_x, grid_y+1, ladder_model_grid, ladder_model_grid[grid_x, grid_y].element, rung)
    
    #If there is node below node connect to nonode
    if (grid_x+1, grid_y) in ladder_model_grid:
        if ladder_model_grid[grid_x+1, grid_y].node is not None:
            node.connected_elements.append(ladder_model_grid[grid_x+1, grid_y].node)
            search_node(grid_x+1, grid_y, ladder_model_grid, ladder_model_grid[grid_x+1, grid_y].node, rung)
        #It there is no node but element connect to element
        elif ladder_model_grid[grid_x+1, grid_y].element is not None:
            node.connected_elements.append(ladder_model_grid[grid_x+1, grid_y].element)
            #When last element is coil end searching path
            if isinstance(ladder_model_grid[grid_x+1, grid_y].element,Coil):
                rung.coils.append(ladder_model_grid[grid_x+1, grid_y].element)
            else:
                search_element(grid_x+1, grid_y, ladder_model_grid, ladder_model_grid[grid_x+1, grid_y].element, rung)



    

    
def delete_connections(ladder_model_grid):
     for grid in ladder_model_grid.values():
          if grid.element is not None:
               grid.element.connected_elements = []
          if grid.node is not None:
               grid.node.connected_elements = []
