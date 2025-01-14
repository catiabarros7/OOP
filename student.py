class Student:
    def __init__ (self, name, age, grade, height):
        self.name = name
        self.age = age
        self.grade = grade
        self.height = height


    def __str__ (self):
        return f"Student: {self.name} Age: {self.age}, Grade: {self.grade}, Height: {self.height}" 
    
    
new_student = Student('Cátia', 19, 'A', 171)
old_student = Student('Kelly', 18, 'B', 150)

print(new_student)