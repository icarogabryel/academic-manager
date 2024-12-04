from .teacher import Teacher
from .subject_class import SubjectClass

class Subject:
    def __init__(self, name, teacher: Teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.classes: list[SubjectClass] = []

    def add_class(self, subject_class: SubjectClass) -> None:
        self.classes.append(subject_class)

    def show_classes(self) -> None:
        for subject_class in self.classes:
            print(subject_class.id)
