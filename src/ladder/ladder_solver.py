from src.ladder.ladder_elements import *



def solve_rung(rung:Rung):
    '''solve coils states for single rung
        Rung consist of connected nodes
        If searching reaches coils they are set to True
    '''
    rung_prepare_coils(rung.coils)
    solve_rung_path(rung.start_element)

    coil:Coil
    for coil in rung.coils:
        if coil.reached==True:
            coil.connected_data=True
        else:
            coil.connected_data=False


def rung_prepare_coils(coils:list[Coil]):
    '''set rung coils objects to not reached state before checking path'''
    for coil in coils:
        coil.reached=False

def solve_rung_path(element):
    '''Evaluate node, search from left to right'''
    #Contact solving
    if isinstance(element, Contact):
        #contact is not connected -> wrong structure throw error
        if element.connected_elements is None:
            raise Exception("Contact have no connection")
        else:
            #if contact return True go deeper
            if element.get_value():
                solve_rung_path(element.connected_elements[0])
    
    #Coil solving
    if  isinstance(element, Coil) :
        #coil reached set coil reached to true
        element.reached = True
        print(f'element {element} reached True')
        #return False to conitnue cheking other nodes if exist
        return False

    if element.type == 'line' or element.type == 'join':

        for next_element in element.connected_elements:
            #try path for every next element from split node
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

contact_1.connected_elements.append(contact_2)
contact_2.connected_elements.append(node_1)
node_1.connected_elements.append(contact_3)
node_1.connected_elements.append(contact_4)
contact_3.connected_elements.append(node_2)
contact_4.connected_elements.append(node_2)
node_2.connected_elements.append(coil_1)
node_2.connected_elements.append(coil_2)

'''
-||-----||---+--||----+----+----()
             |        |    |
             +--||----+    +----()
'''
#TODO move test declarations to test module
rung_1 = Rung(start_element=contact_1)
rung_1.coils.append(coil_1)
rung_1.coils.append(coil_2)
solve_rung(rung_1)

