class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"My name is {self.name} and I am {self.age}yrs old.")
student1 = student("Musa", "10")
student2 = student("Juma", "11")

form = [
    student1,
    student2
]

for student in form:
    student.speak()    
        



        