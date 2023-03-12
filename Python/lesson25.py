class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()
    
    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.processor = "I7"
            self.memory = 16

    def show(self):
        print(f"{self.name} => {self.notebook.model}, {self.notebook.processor}, {self.notebook.memory}")

student1 = Student("Roman")
student2 = Student("Vladimir")

student1.show()
student2.show()
