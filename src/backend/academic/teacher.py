from .person import Person

class Teacher(Person):
    def __init__(self, name, id, subject) -> None:
        super().__init__(name, id)
        self.subject = subject

    def __str__(self) -> str:
        return f'Teacher: {self.name} ({self.id}) - Subject: {self.subject}'
