from src.ladder.ladder_elements import *

__solve_call_counter:int = 0
__f = None
def solve_rung(rung:Rung):
    '''solve coils states for single rung
        Rung consist of connected nodes
        If searching reaches coils they are set to True
    '''
    global __solve_call_counter
    __solve_call_counter=0
    rung_prepare_coils(rung.coils)
    for coil in rung.coils:
        print(f'M connected data:{coil.connected_data_address}')
    global __f
    with open("dump.txt", "a") as __f:
        solve_rung_path(rung.start_element)

    coil:Coil
    for coil in rung.coils:
        if coil.reached==True:
            coil.connected_data[0]=True
        else:
            coil.connected_data[0]=False
        print(f'coil data: {coil.connected_data}')

def rung_prepare_coils(coils:list[Coil]):
    '''set rung coils objects to not reached state before checking path'''
    for coil in coils:
        coil.reached=False

def solve_rung_path(element):
    '''Evaluate node, search from left to right'''

    global __solve_call_counter
    __solve_call_counter += 1
    print(f'solver_rung_call:{__solve_call_counter}')
    print(f'element.type:{element.type}')
    print(f'element.connected_elements:{element.connected_elements}')

    global __f
    __f.write(f'solver_rung_call:{__solve_call_counter}\n')
    __f.write(f'element.type:{element.type}\n')
    __f.write(f'element.connected_elements:{element.connected_elements}\n')
    
    #Contact solving
    if element.type=='contact':
        #contact is not connected -> wrong structure throw error
        if element.connected_elements is None:
            raise Exception("Contact have no connection")
        else:
            #if contact return True go deeper
            if element.get_value():
                for first_item in element.connected_elements: break
                solve_rung_path(first_item)
    
    #Coil solving
    elif element.type=='coil':
        #coil reached set coil reached to true
        element.reached = True
        #print(f'element {element} reached True')
        #return False to conitnue cheking other nodes if exist
        return False

    elif element.type == 'line':

        for next_element in element.connected_elements:
            #Try path for every next element from split node
            #stop if any path reached true (logic OR)
            if solve_rung_path(next_element) == True:
                return True
            
        #every path from split return False
        return False

contact_1 = Contact()
contact_2 = Contact()
node_1 = Node()
contact_3 = Contact()
contact_4 = Contact()
node_2 = Node()
coil_1 = Coil()
coil_2 = Coil()

contact_1.connected_elements.add(contact_2)
contact_2.connected_elements.add(node_1)
node_1.connected_elements.add(contact_3)
node_1.connected_elements.add(contact_4)
contact_3.connected_elements.add(node_2)
contact_4.connected_elements.add(node_2)
node_2.connected_elements.add(coil_1)
node_2.connected_elements.add(coil_2)

'''
-||-----||---+--||----+----+----()
             |        |    |
             +--||----+    +----()
'''
#TODO move test declarations to test module
rung_1 = Rung(start_element=contact_1)
rung_1.coils.add(coil_1)
rung_1.coils.add(coil_2)
solve_rung(rung_1)

