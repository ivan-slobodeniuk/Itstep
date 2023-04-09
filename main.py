class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name is not None

    def __len__(self):
        return self.height

    def grow(self, height=1):
        self.height += height


nick = Student(name='Nick')
kate = Student(name='Kate')
print(bool(nick))
print(len(kate))
