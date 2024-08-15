class Human:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def humanData(self):
        print(f"hello I am {self.name} and I have {self.age} years old.")


class Employee():
    def __init__(self, name, age, job):
      self.name = name  
      self.age = age  
      self.job=job
    def EmpData(self):
        print(f"hello I am {self.name} and I have {self.age} years old. i work as a {self.job}")

   

human = Human("shrouk", 23)
human.humanData() 


employee = Employee("Ahmed", 25, "Software Engineer")
employee.EmpData()  

