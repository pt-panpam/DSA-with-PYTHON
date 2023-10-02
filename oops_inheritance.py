class Employee:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def show_details(self):
        print("details are:")
        print("Name is",self.name)
        print("Gender is",self.gender)
class Personal(Employee):
    def __init__(self,salary,MobileNo):
        self.salary=salary
        self.MobileNo=MobileNo
    def show_personal_details(self):
        print("Salary is:",self.salary)
        print("MObile Number is:",self.MobileNo)
e1=Employee("Abhijeet","Male")
e1.show_details()
e1=Personal(55000,9026009641)
e1.show_personal_details()