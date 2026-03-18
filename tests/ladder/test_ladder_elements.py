from src.ladder.ladder_elements import *


#create class instance testing
def test_create_Element():
    element = Element()
    assert isinstance(element,Element)== True, "Couldn't create Element class instance"

def test_create_Coil():
    coil = Coil()
    assert isinstance(coil,Coil)== True, "Couldn't create Coil class instance"

def test_create_Contact():
    contact = Contact()
    assert isinstance(contact,Contact)== True, "Couldn't create Contact class instance"

def test_create_Rung():
    rung = Rung()
    assert isinstance(rung,Rung)== True, "Couldn't create Rung class instance"

def test_create_Program():
    program = Program()
    assert isinstance(program,Program)== True, "Couldn't create Program class instance"


def test_NC_NO_Contact():
    contact = Contact(connected_data = True)
    assert contact.coil_type == 'NO', "Wrong type of default contact"
    assert contact.get_value() == True, "NO True returned False should True"
    contact = Contact(connected_data = True, coil_type='NC')
    assert contact.get_value() == False, "NC True returned True should False"
    
if __name__ == "__main__":
    test_NC_NO_Contact()
