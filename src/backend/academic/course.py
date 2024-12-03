from .student import Student
from .teacher import Teacher

class Course:
    def __init__(self, title) -> None:
        self.title = title
        self.teachers: set[Teacher] = set()
        self.students: set[Student] = set()

    def add_teacher(self, teacher: Teacher) -> None:
        self.teachers.add(teacher)
    def remove_teacher(self, teacher: Teacher) -> None:
        self.teachers.remove(teacher)

    def add_student(self, student: Student) -> None:
        self.students.add(student)

    def remove_student(self, student: Student) -> None:
        self.students.remove(student)

    def __str__(self) -> str:
        info = f'Course: {self.title}\n\n'
        info += 'Teachers:\n'

        for teacher in self.teachers:
            info += f'{teacher}\n'

        info += '\nStudents:\n'

        for student in self.students:
            info += f'{student}\n'

        return info
