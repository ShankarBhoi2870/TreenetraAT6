import pytest
class TestStudent:
    @pytest.fixture(autouse=True)
    def setup(self, student_details):
        self.student_details = student_details
        yield

    def test_calculate_marks_Shankar(self):
        math_deduct, science_deduct, history_deduct = 20, 15, 4
        marks = self.student_details.calculate_marks(math_deduct, science_deduct, history_deduct)
        assert marks == (80, 85, 46)

    def test_calculate_marks_Tapan(self):
        math_deduct, science_deduct, history_deduct = 16, 18, 3
        marks = self.student_details.calculate_marks(math_deduct, science_deduct, history_deduct)
        assert marks == (84, 82, 47)

    def test_calculate_marks_Suvam(self):
        math_deduct, science_deduct, history_deduct = 20, 21, 9
        marks = self.student_details.calculate_marks(math_deduct, science_deduct, history_deduct)
        assert marks == (80, 79, 41)