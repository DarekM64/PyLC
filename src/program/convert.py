import json
import copy
import jsonpickle

def dump_data(grid):
    #result =  json.dumps(grid)
    #print(result)
    #grid_json = copy.deepcopy(grid)
    #board2 = dict((str(k), val) for k, val in board.items())
    # grid_json = dict((str(k), val) for k, val in grid.items())
    # print(grid_json)
    # print(grid_json.items())
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(grid_json, f, ensure_ascii=False, indent=4)
    json_string = jsonpickle.encode(grid, indent=4)
    with open("rung_json.json", "a") as f:
        f.write(json_string)
   #recreated_obj = jsonpickle.decode(json_string)