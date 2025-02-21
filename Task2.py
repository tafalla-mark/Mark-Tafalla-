class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}.  {self.age} year-old {self.course} student.")

student1 = Student("Mark",19, "DIP-IT")
student2 = Student("Terry", 20, "DIP-IT")
student3 = Student("Tom", 30, "DIP-IT")

print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()
