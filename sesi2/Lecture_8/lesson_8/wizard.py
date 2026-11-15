class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
    def __str__(self):
        return f"{self.name}" 
        
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    def __str__(self):
        return f"{super().__str__()} and {self.house}" 
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return f"{super().__str__()} and {self.subject}" 
def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against The Dark Arts")
    print(wizard)
    print(student)
    print(professor)

if __name__ == "__main__":
    main()

