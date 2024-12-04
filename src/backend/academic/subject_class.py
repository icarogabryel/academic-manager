from .student import Student
from .test import Test


class SubjectClass:
    def __init__(self, id) -> None:
        self.id = id
        self.students: set[Student] = set()
        self.tests: dict[str, list[Test]] = {}

    def add_student(self, student: Student) -> None:
        self.students.add(student)
        self.tests[student] = []

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)
        del self.tests[student]

    def add_test(self, student: Student, score, weight) -> None:
        if student in self.students:
            self.tests[student].append(Test(score, weight))
        else:
            raise ValueError("Student not in class")

    def show_students(self) -> None:
        for student in self.students:
            print(student)

    def show_tests(self) -> None:
        for student, tests in self.tests.items():
            print(f'Student: {student}, scores: {tests}')
