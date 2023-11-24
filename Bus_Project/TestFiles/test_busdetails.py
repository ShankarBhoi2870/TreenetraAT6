import pytest

# @pytest.fixture(scope="class")
class TestBus():
    @pytest.fixture(autouse=True)
    def setup(self, bus_details):
        self.bus_details = bus_details
        yield

    def test_owner(self):
        self.bus_details.owner('Tesla', 50, 90000)
        assert self.bus_details.o_name == 'Tesla'

    def test_driver(self):
        self.bus_details.driver('Shankar', 30, 58000)
        assert self.bus_details.d_name == 'Shankar'

    def test_conductor(self):
        self.bus_details.conductor('Bhoi', 35, 1500)
        assert self.bus_details.c_name == 'Bhoi'

    def test_total_salary(self):
        self.bus_details.owner('Tesla', 50, 90000)
        self.bus_details.driver('Shankar', 30, 58000)
        self.bus_details.conductor('Bhoi', 35, 15000)
        assert self.bus_details.total_salary() == 163000