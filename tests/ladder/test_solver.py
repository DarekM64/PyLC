from src.ladder.ladder_elements import Contact, Coil
from src.ladder.ladder_solver import *

def test_1():
    contact_1 = Contact(connected_data=True)
    contact_2 = Contact(connected_data=False)
    node_1 = Element(connected_data=True,type='split')
    contact_3 = Contact(connected_data=False)
    contact_4 = Contact(connected_data=True)
    node_2 = Element(connected_data=True,type='join')
    coil_1 = Coil(connected_data=True)
    coil_2 = Coil(connected_data=True)

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

test_1()