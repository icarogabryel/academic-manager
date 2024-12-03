class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f'Person: {self.name} ({self.id})'
    