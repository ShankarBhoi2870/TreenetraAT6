import pytest
class Student:
    def subjects(self, math, science, history):
        self.math = math
        self.science = science
        self.history = history

    def calculate_marks(self, math_deduct, science_deduct, history_deduct):
        value_in_math = self.math - math_deduct
        value_in_science = self.science - science_deduct
        value_in_history = self.history - history_deduct
        return value_in_math, value_in_science, value_in_history

@pytest.fixture(scope="class")
def student_details():
    student = Student()
    student.subjects(100, 100, 50)
    return student


