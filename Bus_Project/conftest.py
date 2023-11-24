import pytest
class Bus:
    def __init__(self,owner,driver,conductor):
        self._owner = owner
        self._driver = driver
        self._conductor = conductor

    def owner(self,o_name,o_age,o_salary):
        self.o_name = o_name
        self.o_age = o_age
        self.o_salary = o_salary
        print(f'Owner Name:- {self.o_name},Owner Age :- {self.o_age}, Owner salary :- {self.o_salary}')
    def driver(self,d_name,d_age,d_salary):
        self.d_name = d_name
        self.d_age = d_age
        self.d_salary = d_salary
        print(f'driver Name:- {self.d_name},driver Age :- {self.d_age}, driver salary :- {self.d_salary}')
    def conductor(self,c_name,c_age,c_salary):
        self.c_name = c_name
        self.c_age = c_age
        self.c_salary = c_salary
        print(f'conductor Name:- {self.c_name},conductor Age :- {self.c_age}, conductor salary :- {self.c_salary}')

    def total_salary(self):
        total = self.o_salary+self.d_salary+self.c_salary
        return total

@pytest.fixture(scope='class')
def bus_details():
    return Bus('Manikeswari Owner', 'Manikeswari Driver', 'Manikeswari Conductor')