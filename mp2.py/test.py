class Student:
    def __init__(self, name, degree):
        if not name:
            raise ValueError("Missing name")
        if degree not in ["ECE", "BIO", "MECH", "EEE"]:
            raise ValueError("Invalid degree")
        self.name=name
        self.degree=degree

def main():
    student=get_student()
    print(f"{student.name} from {student.degree}")

def get_student():
    name=input("Name: ")
    degree=input("degree: ")
    return Student(name, degree)