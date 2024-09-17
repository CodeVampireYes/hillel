class GroupLimit(Exception):
    pass


class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.gender}, {self.age}, {self.first_name}, {self.last_name}'


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.record_book}'


class Group:

    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student) -> None:
        if len(self.group) >= 10:
            raise GroupLimit('Group is full.')
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student_to_remove = None
        for student in self.group:
            if student.last_name == last_name:
                student_to_remove = student
                break
            if student_to_remove:
                self.group.remove(student_to_remove)

    def find_student(self, last_name: str) -> None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Group Number: {self.number}\nStudents:\n{all_students}'


group: Group = Group('A24')

try:
    for i in range(11):
        group.add_student(Student('Male', 26, 'John', 'Cena',f'A24-{i}'))
except GroupLimit as e:
    print(e)
finally:
    print(group)