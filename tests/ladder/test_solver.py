from src.ladder.ladder_elements import Contact, Coil
from src.ladder.ladder_solver import *

def test_rung_prepare_coils():
    '''Check if prepare_coils clear reached flag'''
    coil_1=Coil(connected_data=True)
    coil_1.reached = True
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    rung_prepare_coils(rung_1.coils)
    assert rung_1.coils[0].reached == False, "Coil reached flag not cleared"


def test_solve_rung_1():
    '''
    -|T|-----()
      NO     
    '''
    contact_1 = Contact(connected_data=True)
    coil_1 = Coil(connected_data=False)
    contact_1.connected_elements.append(coil_1)
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    solve_rung(rung_1)
    assert rung_1.coils[0].connected_data == True, "Coil should be in 1-True state."

def test_solve_rung_2():
    '''
    -|T|-----()
      NO     
    '''
    contact_1 = Contact(connected_data=False)
    coil_1 = Coil(connected_data=False)
    contact_1.connected_elements.append(coil_1)
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    solve_rung(rung_1)
    assert rung_1.coils[0].connected_data == False, "Coil should be in 0-False state."

def test_solve_rung_3():
    '''
    -|T|-----()
      NC     
    '''
    contact_1 = Contact(connected_data=True, coil_type='NC')
    coil_1 = Coil(connected_data=False)
    contact_1.connected_elements.append(coil_1)
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    solve_rung(rung_1)
    assert rung_1.coils[0].connected_data == False, "Coil should be in 0-False state."

def test_solve_rung_4():
    '''
    -|T|-----()
      NC     
    '''
    contact_1 = Contact(connected_data=False, coil_type='NC')
    coil_1 = Coil(connected_data=False)
    contact_1.connected_elements.append(coil_1)
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    solve_rung(rung_1)
    assert rung_1.coils[0].connected_data == True, "Coil should be in 1-True state."



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
    rung_1 = Rung(start_element=contact_1)
    rung_1.coils.append(coil_1)
    rung_1.coils.append(coil_2)
    solve_rung(rung_1)

test_1()