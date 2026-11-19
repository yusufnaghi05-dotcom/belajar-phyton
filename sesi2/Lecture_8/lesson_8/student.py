# # class Student:
# #     def __init__(self, name, house, patronus):
# #         if not name:
# #             raise ValueError("Missing Name")
# #         if house not in ["Gryffindor", "Hufflepuff", "Ravensclaw", "Slytherin"]:
# #             raise ValueError("Invalid House")
# #         self.name = name
# #         self.house = house
# #         self.patronus = patronus
# #     def __str__(self):
# #         return f"{self.name} from {self.house}"
# #     def charm(self):
# #         match self.patronus:
# #             case "Stag":
# #                 return "🐴"
# #             case "Otter":
# #                 return "🐻"
# #             case "Jack Russel terrier":
# #                 return "🐶"
# #             case _:
# #                 return "🖊"
# # def main():
# #     student = get_student()
# #     print(student)
# #     print("Expecto Patronum!")
# #     print(student.charm())
# # def get_student():
# #     name =input("Name: ")
# #     house =input("House: ")
# #     patronus = input("Patronus: ")
# #     return Student(name, house, patronus)
# # if __name__ == "__main__":
# #     main()


# # class Student:
# #     def __init__(self, name, house):
# #         if not name:
# #             raise ValueError("Missing Name")
# #         if house not in ["Gryffindor", "Hufflepuff", "Ravensclaw", "Slytherin"]:
# #             raise ValueError("Invalid House")
# #         self.name = name
# #         self.house = house
# #     def __str__(self):
# #         return f"{self.name} from {self.house}"
    
# # def main():
# #     student = get_student()
# #     student.house = "Number Four, Privet Drive"
# #     print(student)
# # def get_student():
# #     name =input("Name: ")
# #     house =input("House: ")
# #     return Student(name, house)
# # if __name__ == "__main__":
# #     main()

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         self.get_house = house
#     def __str__(self):
#         return f"{self.name} from {self.get_house}"
#     @property
#     def get_house(self):
#         return self._house
    
#     @get_house.setter
#     def get_house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError
#         self._house = house
    
# def main():
#     student = get_student()
#     student.get_house = "Number Four, Privet Drive"
#     print(student)
# def get_student():
#     name =input("Name: ")
#     house =input("House: ")
#     return Student(name, house)
# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, name, house):
        self.name = name
        self.get_house = house
    def __str__(self):
        return f"{self.name} from {self.get_house}"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    @property
    def get_house(self):
        return self._house
     
    @get_house.setter
    def get_house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError
        self._house = house
    
def main():
    student = get_student()
    student._name = "Drive"
    print(student)
def get_student():
    name =input("Name: ")
    house =input("House: ")
    return Student(name, house)
if __name__ == "__main__":
    main()

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)
    
# def main():
#     student = Student.get()
#     print(student)
    
# if __name__ == "__main__":
#     main()
    