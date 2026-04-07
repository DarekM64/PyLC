from src.program.model import *

def model_search(ladder_model_grid):
    print('Search model !')
    for v,k in ladder_model_grid.items():
        if k.element is not None:
        #if k.element.type is not None:
            print(f'{v}:{k.element.type}')

    