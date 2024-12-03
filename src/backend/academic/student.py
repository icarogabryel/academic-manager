from .person import Person

class Student(Person):
    def __init__(self, name, id, enrollment):
        super().__init__(name, id)
        self.enrollment = enrollment

    def __str__(self) -> str:
        return f'Student: {self.name} ({self.id}) - Enrollment: {self.enrollment}'
